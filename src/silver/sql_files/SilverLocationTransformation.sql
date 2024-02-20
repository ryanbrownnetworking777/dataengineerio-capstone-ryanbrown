SELECT 
   locationId as 'Location ID'
  ,allowStorePickup as 'Store Pickup Allowed?'
  ,bufferStock as 'Buffer Stock Setting'
  ,isInactive as 'Inactive?'
  ,latitude as 'Latitude'
  ,longitude as 'Longitude'
  ,mainAddress_id as 'Main Address ID'
  ,makeInventoryAvailable as 'Inventory Available for Purchase?'
  ,name as 'Location Name'
  ,nextPickupCutOffTime as 'Next Pickup Cut Off Time'
  ,timeZone as 'Time Zone'
  ,totalShippingCapacity as 'Total Shipping Capacity'
FROM results
