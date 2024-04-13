bg3_party_export
================

## Description

This was an idea I had based on looking at the unpacked resources under `Baldurs Gate 3/Data/Mods/GustavDev/Story/PartyEditor`
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
I suggest you name it after your character but it really doesn't matter. 

Then using this project you can run using either of the following options from the location you have it locally:

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
python convert_party_editor.py charname.json > <your-party-editor.lsx>
```

Then create a directory in your BG3 Installation directory `Data/Mods/GustavDev/Story/PartyEditor` and place the lsx file
created  from the previous command.  Now start a new game and when the BG3SE console is available run this command in it:

**Note** do not append `.lsx` here

```
LoadPartyPreset("<your-party-editor>", "true")
```

## Status *IN Progress*

This is still very much a work in progress.  Items are not being handled properly, and it only handles single character
export.  Still working on the following:

* Icon Fix (currently need to respec/change appearance to fix)
* Inventory
* Specifying Teleport Location

Would like to have the following:

* Statuses
* Tadpole Powers

Unfortunately I can only go by existing examples as there is no real specification or guide to what they can contain.