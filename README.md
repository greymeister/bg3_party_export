bg3_party_export
================

## Description

This was an idea I had based on looking at the unpacked resources under `Baldurs Gate 3/Data/Mods/GustavDev/Story/PartyEditor`
There is a call `Osi.LoadPartyPreset("preset_name", "Target")` that lets you load up one of these pre-defined lsx files.
It seems like a pretty neat thing to be able to dump your character state and then be able to load that into a fresh save,
so this is my attempt at that.

Credits to Norbyte for [BG3SE](https://github.com/Norbyte/bg3se/) and [lslib](https://github.com/Norbyte/lslib) which made this possible.

## Usage

First, this requires [BG3SE](https://github.com/Norbyte/bg3se/) to make use of.  Launch the game with the script console
enabled as per the instructions of that project, and when you have the game loaded, run the following command in the console:

```
entity=Ext.Entity.Get(GetHostCharacter())
Ext.IO.SaveFile("charname.json", Ext.DumpExport(entity:GetAllComponents()))
```

This will create a file `charname.json` in your `AppData/Local/Larian Studios/Baldur's Gate 3/Script Extender` directory.
I suggest you name it after your character, but it really doesn't matter.

**Important** At least one of the characters you export needs to have been an avatar or else the game can't properly load
the party.  It also seems to only assign avatar status to the last such character you combine.  Unlike in MP games, you will
only have one "avatar" character with this setup.

Then using this project you can run using python 3.11+ with either of the following options from the directory you have it:

1. With pipenv available:

```
pipenv install
pipenv shell
```

2. Without pipenv:

```
pip install -r requirements.txt
```

After doing either 1) or 2), then run the following:

```
python convert_party_editor.py charname.json > party.lsx
```

If you'd like to have more than one character, simply export multiple character json files with SE and then run like this:

```
python convert_party_editor.py file1.json file2.json file3.json file4.json > party.lsx
```

Then create a directory in your BG3 Installation directory `Data/Mods/GustavDev/Story/PartyEditor` and place the lsx file
created  from the previous command.  Now start a new with a non-origin character, when the BG3SE console is available run this command in it:

```
LoadPartyPreset("party", GetHostCharacter())
```

**Note** do not append `.lsx` extension here.

After that, save and load (or go to main menu and load if Honour mode is on) as stats and spell slots are wonky.

## Troubleshooting

### Clean character from game

*Note* This has worked for me but messing with the DB contents can cause bugs so unless you specifically need to do this **don't**.

Run the following command from the script console before you load the party preset:

```
_Purge=GetHostCharacter()
```

Then, after loading the party preset and making sure things look right, run the following [source](https://old.reddit.com/r/BaldursGate3/comments/15qb8lu/guide_removing_custom_multiplayer_party_members/):

```
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

This cleans references but I'll need to do more testing to see if anything breaks downstream due to a script bug etc.

**Note** Do this *before* you save/load or else `_Purge` will be undefined.

### Fixing character icon

The character icon will default to an old picture of Karlach.  The data needed is a base64 encoded webp file.  Right now
that data is not exposed by SE so until then it's just a placeholder.  To fix run the following:

```
Osi.StartChangeAppearance(GetHostCharacter())
```

If your party preset is an origin character, you'll need to respec or level up to fix the icon:

```
Osi.StartRespec(GetHostCharacter())
```

If your preset is an Origin Oathbreaker I guess just wait until you level up 💩

## Status *WIP*

This is still very much a work in progress.  Still working on the following:

* Icon Fix (currently need to respec/change appearance to fix)

Would like to fix/implement the following:

* Statuses
* Tadpole Powers
* Inventory

Unfortunately I can only go by existing examples as there is no real specification or guide to what they can contain.