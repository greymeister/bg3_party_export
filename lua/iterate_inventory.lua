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
        _P("[ROOT] (".. itemRoot .. ") [slot] " .. slot .. " [statsId] " .. statsId .. " [amount] " .. amount)
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
        _P("[ROOT] (".. itemRoot .. ") [slot] " .. slot .. " [statsId] " .. statsId .. " [amount] " .. amount)
        itemInfo = {
            Amount=amount, ID=itemRoot, InventorySlot=slot, IsEquipped="false", IsKey=isKey,
            ItemGroup=itemGroup, Key=key, LockDifficultyClassID=lockDc, StatsID=statsId, UUID=itemUuid
        }
        table.insert(inventory, itemInfo)
    end

    return inventory
end