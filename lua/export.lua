character=_C():GetAllComponents()
inventory=getItems()
character.ImportedInventory=inventory
Ext.IO.SaveFile("charname.json", Ext.DumpExport(character))