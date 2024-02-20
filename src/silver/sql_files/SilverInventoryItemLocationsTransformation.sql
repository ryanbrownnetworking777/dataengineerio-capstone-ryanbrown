SELECT
   inventoryItemLocationsId as 'Inventory Item Location ID'
  ,inventoryLocationDisplayName as 'Display Name'
  ,location as 'Location'
  ,quantityAvailable as 'Quality Available'
  ,quantityBackOrdered as 'Quantity Backordered'
  ,quantityCommitted as 'Quantity Committed'
  ,quantityOnHand as 'Quantity On Hand'
  ,quantityOnOrder as 'Quantity On Order'
FROM results
