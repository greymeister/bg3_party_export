bg3_party_export
================

## Description

This was an idea I had based on looking at the unpacked resources under `Baldurs Gate 3/Data/Mods/GustavDev/Story/PartyEditor`
There is a call `Osi.LoadPartyPreset("preset_name", "Target")` that lets you load up one of these pre-defined lsx files.
It seems like a pretty neat thing to be able to dump your character state and then be able to load that into a fresh save,
so this is my attempt at that.

Credits to Norbyte for [BG3SE](https://github.com/Norbyte/bg3se/) and [lslib](https://github.com/Norbyte/lslib) which made this possible.
Thanks to the folks in `#scripting-dev-chat` on Larian's discord for some example scripts and advice.
And of course to Larian for making an amazing game.

## Usage

First, this requires [BG3SE](https://github.com/Norbyte/bg3se/) to make use of.  Launch the game with the script console
enabled as per the instructions of that project, and when you have the game loaded, run the following in the console:

```lua
--[[
function getItems()
    local inventory = {}

    for _,item in pairs(_C():GetAllComponents().InventoryOwner.Inventories[2].InventoryContainer.Items) do
        local itemRoot  = item.Item.GameObjectVisual.RootTemplateId
        local itemUuid = item.Item.Uuid.EntityUuid
        local statsId = item.Item.Data.StatsId
        local amount = select(2, Osi.GetStackAmount(itemUuid))
        local slot = item.Item.InventoryMember.EquipmentSlot
        local isKey = item.Item.ServerItem.Template.IsKey
        local key = ""
        if item.Item.Key ~= nil and item.Item.Key.Key ~= nil then key = item.Item.Key.Key end
        local itemGroup = "Common"
        if item.Item.Value.Unique then itemGroup = "Unique" end
        local lockDc = item.Item.ServerItem.Template.LockDifficultyClassID
        itemInfo = {
            Amount=amount, ID=itemRoot, InventorySlot=slot, IsEquipped="true", IsKey=isKey,
            ItemGroup=itemGroup, Key=key, LockDifficultyClassID=lockDc, StatsID=statsId, UUID=itemUuid
        }
        table.insert(inventory, itemInfo)
    end

    for _,item in pairs(_C():GetAllComponents().InventoryOwner.PrimaryInventory.InventoryContainer.Items) do
        local itemRoot  = item.Item.GameObjectVisual.RootTemplateId
        local itemUuid = item.Item.Uuid.EntityUuid
        local statsId = item.Item.Data.StatsId
        local amount = select(2, Osi.GetStackAmount(itemUuid))
        local slot = item.Item.InventoryMember.EquipmentSlot + 18 -- Equipment overlap
        local isKey = item.Item.ServerItem.Template.IsKey
        local key = ""
        if item.Item.Key ~= nil and item.Item.Key.Key ~= nil then key = item.Item.Key.Key end
        local itemGroup = "Common"
        if item.Item.Value.Unique then itemGroup = "Unique" end
        local lockDc = item.Item.ServerItem.Template.LockDifficultyClassID
        itemInfo = {
            Amount=amount, ID=itemRoot, InventorySlot=slot, IsEquipped="false", IsKey=isKey,
            ItemGroup=itemGroup, Key=key, LockDifficultyClassID=lockDc, StatsID=statsId, UUID=itemUuid
        }
        table.insert(inventory, itemInfo)
    end

    return inventory
end

character=_C():GetAllComponents()
inventory=getItems()
character.ImportedInventory=inventory
]]--
```
Then finally run this command:
```lua
Ext.IO.SaveFile("charname.json", Ext.DumpExport(character))
```

This will create a file `charname.json` in your `AppData/Local/Larian Studios/Baldur's Gate 3/Script Extender` directory.
I suggest you name it after your character, but it really doesn't matter.

**Important** At least one of the characters you export needs to have been an avatar or else the game can't properly load
the party.  It also seems to only assign avatar status to the last such character you combine.  Unlike in MP games, you will
only have one "avatar" character with this setup.

Then using this project you can run using python 3.11+ with either of the following options from the directory you have it:

1. With pipenv available:

```shell
pipenv install
pipenv shell
```

2. Without pipenv:

```shell
pip install -r requirements.txt
```

After doing either 1) or 2), then run the following:

```shell
python convert_party_editor.py charname.json > party.lsx
```

If you'd like to have more than one character, simply export multiple character json files with SE and then run like this:

```shell
python convert_party_editor.py file1.json file2.json file3.json file4.json > party.lsx
```

Then create a directory in your BG3 Installation directory `Data/Mods/GustavDev/Story/PartyEditor` and place the lsx file
created by the script.  Now start a new game with a **Custom** (Tav) character.  When the BG3SE console is available run this:

```lua
_Purge=_C().ServerCharacter.Template.Name .. "_" .. GetHostCharacter()
LoadPartyPreset("party", GetHostCharacter())
```

**Note** `.lsx` extension is not used with the parameter

Then, after loading the party preset run the following:

```lua
--[[
MakeNPC(_Purge)
SetFaction(_Purge, "NPC_cfb709b3-220f-9682-bcfb-6f0d8837462e")
SetHasDialog(_Purge, 0)
SetOnStage(_Purge, 0)
Osi.DB_Players:Delete(_Purge)
Osi.DB_Avatars:Delete(_Purge)
Osi.DB_PartOfTheTeam:Delete(_Purge)
Osi.DB_IsOrWasInParty:Delete(_Purge)
Osi.DB_GLO_PartyMembers_InPartyDialog:Delete(_Purge, "NULL_00000000-0000-0000-0000-000000000000")
Osi.PROC_RemoveAllPolymorphs(_Purge)
Osi.PROC_RemoveAllDialogEntriesForSpeaker(_Purge)
SetImmortal(_Purge, 0)
Die(_Purge, 0, "NULL_00000000-0000-0000-0000-000000000000", 0, 0)
Osi.PROC_CheckPartyFull()
]]--
```

This cleans references to your initial character. If it is found that anything breaks downstream due to a script bug I will amend the instructions.

After that, save and load (or go to main menu and load if Honour mode is on) as stats and spell slots are wonky after import.

## Troubleshooting

### Inventory

The script now tries to populate inventory, but will not handle nested containers.

For example, if you have a camp supply sack with food items in it, the food items will not be
transferred over.  The camp supply sack will be imported, just not their contents.

### Fixing character icon

**Note** With a build of BG3SE that has the ScratchBuffer exposed for CustomIcon elements, this is no longer necessary.

If the CharacterIcon WEBP buffer is not available, it will default to a picture of Karlach.  To fix run the following:

```lua
Osi.StartChangeAppearance(GetHostCharacter())
```

If your party preset is an origin character, you'll need to respec or level up to fix the icon:

```lua
Osi.StartRespec(GetHostCharacter())
```

If your preset is an Origin Oathbreaker I guess just level up 💩

### Fixing Avatar Status

If you import multiple Tavs only the last one in the resulting lsx file will be marked as an avatar.  It seems like the
`LoadPartyPreset` function strips the avatar tag off of the other characters.  It also can cause issues where these
characters aren't able to travel to camp.  Fix by running the following  script with the character selected:

```lua
--[[
_UUID=_C().ServerCharacter.Template.Name .. "_" .. GetHostCharacter()
Osi.DB_Players(_UUID)
Osi.DB_Avatars(_UUID)
Osi.DB_PartOfTheTeam(_UUID)
SetTag(GetHostCharacter(), "306b9b05-1057-4770-aa17-01af21acd650")
Osi.PROC_CheckPartyFull()
]]--
```

Then save and reload, your characters should be marked as avatars and be able to visit camp etc.

### Wizard Spellbook Learned Spells

I have not had a chance to use the new Larian Toolkit, and not sure if that will help but right now I have not been able to
read a wizard's learned spells and populate the party preset and have it import properly.

What I plan to do is generate the scrolls for a character's learned spells and add those to the inventory.

## Status *WIP*

This is still very much a work in progress.  Still working on the following:

* Apply dyes used on items
* Wizard Learned Spells -> create scrolls to replace

Would be nice to fix/implement the following:

* Statuses
* Tadpole Powers

Unfortunately I can only go by existing examples as there is no specification or guide to party presets.