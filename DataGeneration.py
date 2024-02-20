#!/usr/bin/env python
# coding: utf-8

# In[4]:


import duckdb
import polars as pl
from datetime import datetime


# In[2]:


def read_from_duckdb(query, db_path):
    conn = duckdb.connect(db_path)
    return conn.execute(query).fetchall()


# In[3]:


db_path = "ERPSourceMockup.db"


# # In[4]:


# query = "SELECT * FROM LOCATION;"


# # In[5]:


# read_from_duckdb(query, db_path)


# In[ ]:


def write_to_duckdb(db_path, create_table_ddl, insert_into_ddl):
    """ DuckDBにデータを書き込むカスタム関数 """
    conn = duckdb.connect(db_path)
    conn.execute("CREATE TABLE IF NOT EXISTS {} (...);".format(table_name))  # 適切なスキーマで置き換える

# DuckDBのファイルパスとクエリ


# # In[6]:


# # CashSaleテーブルの定義に基づいてPolarsデータフレームを作成
# cash_sale_df = pl.DataFrame(
#     {
#         "account_id": pl.Int64,
#         "altHandlingCost": pl.Float64,
#         "altShippingCost": pl.Float64,
#         "authCode": pl.Utf8,
#         "billAddressList_id": pl.Int64,
#         "billingAccount_id": pl.Int64,
#         "billingAddress_id": pl.Int64,
#         "billingSchedule_id": pl.Int64,
#         "canHaveStackable": pl.Boolean,
#         "ccApproved": pl.Boolean,
#         "ccAvsStreetMatch": pl.Utf8,
#         "ccAvsZipMatch": pl.Utf8,
#         "ccExpireDate": pl.Date,
#         "ccIsPurchaseCardBin": pl.Boolean,
#         "ccName": pl.Utf8,
#         "ccNumber": pl.Utf8,
#         "ccProcessAsPurchaseCard": pl.Boolean,
#         "ccSecurityCode": pl.Utf8,
#         "ccSecurityCodeMatch": pl.Utf8,
#         "ccStreet": pl.Utf8,
#         "ccZipCode": pl.Utf8,
#         "chargeIt": pl.Boolean,
#         "checkNumber": pl.Utf8,
#         "class_id": pl.Int64,
#         "contribPct": pl.Utf8,
#         "createdDate": pl.Datetime,
#         "createdFrom_id": pl.Int64,
#         "creditCard_id": pl.Int64,
#         "creditCardProcessor_id": pl.Int64,
#         "currency_id": pl.Int64,
#         "currencyName": pl.Utf8,
#         "customFieldList_id": pl.Int64,
#         "customForm_id": pl.Int64,
#         "debitCardIssueNo": pl.Utf8,
#         "deferredRevenue": pl.Float64,
#         "department_id": pl.Int64,
#         "discountItem_id": pl.Int64,
#         "discountRate": pl.Utf8
#     }
# )

# # 空のデータフレームを表示
# print(cash_sale_df)


# # In[8]:


# new_sale_data = {
#     "account_id": [101],
#     "altHandlingCost": [2.50],
#     "altShippingCost": [5.00],
#     "authCode": ["AUTH123"],
#     "billAddressList_id": [1],
#     "billingAccount_id": [1],
#     "billingAddress_id": [1],
#     "billingSchedule_id": [1],
#     "canHaveStackable": [True],
#     "ccApproved": [True],
#     "ccAvsStreetMatch": ["Match"],
#     "ccAvsZipMatch": ["Match"],
#     "ccExpireDate": [datetime(2024, 12, 31)],
#     "ccIsPurchaseCardBin": [False],
#     "ccName": ["John Doe"],
#     "ccNumber": ["1234567890123456"],
#     "ccProcessAsPurchaseCard": [False],
#     "ccSecurityCode": ["123"],
#     "ccSecurityCodeMatch": ["Match"],
#     "ccStreet": ["123 Main St"],
#     "ccZipCode": ["12345"],
#     "chargeIt": [True],
#     "checkNumber": ["Check123"],
#     "class_id": [1],
#     "contribPct": ["10%"],
#     "createdDate": [datetime.now()],
#     "createdFrom_id": [1],
#     "creditCard_id": [1],
#     "creditCardProcessor_id": [1],
#     "currency_id": [1],
#     "currencyName": ["USD"],
#     "customFieldList_id": [1],
#     "customForm_id": [1],
#     "debitCardIssueNo": ["DC123"],
#     "deferredRevenue": [100.00],
#     "department_id": [1],
#     "discountItem_id": [1],
#     "discountRate": ["10%"]
# }

# # 新しいセールデータをデータフレームに追加
# new_sale_df = pl.DataFrame(new_sale_data)
# # cash_sale_df = cash_sale_df.vstack(new_sale_df)

# # 更新されたデータフレームを表示
# print(new_sale_df)


# # In[15]:


from faker import Faker
import random

# Fakerインスタンスの初期化
fake = Faker()

# サンプルデータを生成する関数
def generate_sample_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'date_of_birth': fake.date_of_birth().isoformat(),
            'phone_number': fake.phone_number(),
            'int': fake.random_int()
        }
        data.append(record)
    return data

# サンプルデータの生成
num_records = 10  # 生成するレコードの数
sample_data = generate_sample_data(num_records)

# サンプルデータの表示（テスト用）
for record in sample_data:
    print(record)


# In[ ]:


dir(fake)


# In[17]:


# サンプルデータを生成する関数
def generate_sales_order_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'accountingBookDetailList_id': random.randint(1, 100),
            'actualShipDate': fake.date(),
            'altHandlingCost': random.uniform(10.0, 100.0),
            'altSalesTotal': random.uniform(100.0, 1000.0),
            'altShippingCost': random.uniform(5.0, 50.0),
            'authCode': fake.bothify(text='????-####-####-####'),
            'balance': random.uniform(100.0, 10000.0),
            'billAddressList_id': random.randint(1, 100),
            'billingAddress_id': random.randint(1, 100),
            'billingSchedule_id': random.randint(1, 100),
            'canHaveStackable': fake.boolean(),
            'ccApproved': fake.boolean(),
            'ccAvsStreetMatch': fake.random_element(elements=('Y', 'N', 'X')),
            'ccAvsZipMatch': fake.random_element(elements=('Y', 'N', 'X')),
            'ccExpireDate': fake.date(),
            'ccName': fake.name(),
            'ccNumber': fake.credit_card_number(card_type=None),
            'ccSecurityCode': fake.credit_card_security_code(card_type=None),
            'ccStreet': fake.street_address(),
            'ccZipCode': fake.zipcode(),
            'checkNumber': str(random.randint(1000, 9999)),
            'class_id': random.randint(1, 100),
            'contribPct': str(random.uniform(0, 100)) + '%',
            'createdDate': fake.date(),
            'createdFrom_id': random.randint(1, 100),
            'creditCard_id': random.randint(1, 100),
            'creditCardProcessor_id': random.randint(1, 100),
            'currency_id': random.randint(1, 100),
            'currencyName': fake.currency_name(),
            'customFieldList_id': random.randint(1, 100),
            'customForm_id': random.randint(1, 100),
            'debitCardIssueNo': str(random.randint(1, 999)),
            'deferredRevenue': random.uniform(100.0, 10000.0),
            'department_id': random.randint(1, 100),
            'discountItem_id': random.randint(1, 100),
            'discountRate': str(random.uniform(0, 100)) + '%',
            # その他のフィールド
        }
        data.append(record)
    return data

# サンプルデータの生成
num_records = 100  # 生成するレコードの数
sample_data = generate_sales_order_data(num_records)

# # サンプルデータの表示（テスト用）
# for record in sample_data:
#     print(record)

sample_dataframe = pl.DataFrame(sample_data)


# In[18]:


sample_dataframe.head()


# In[36]:


def generate_location_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
             'locationId': _
            ,'allowStorePickup' : True
            ,'autoAssignmentRegionSetting' : fake.emoji()
            ,'bufferStock' : random.uniform(10.0, 100.0)
            ,'dailyShippingCapacity' : random.uniform(10.0, 100.0)
            ,'excludeLocationRegionsList_id' : random.uniform(10.0, 100.0)
            ,'geolocationMethod' : "_useLatLongCoordinates"
            ,'includeChildren' : False
            ,'includeInControlTower' : False
            ,'includeLocationRegionsList' : []
            ,'isInactive' : False
            ,'latitude' : random.uniform(-90, 90)
            ,'locationType' : 'Store'
            ,'logo' : fake.image()
            ,'longitude' : random.uniform(-180, 180)
            ,'mainAddress_id' : fake.address()
            ,'makeInventoryAvailable' : True
            ,'makeInventoryAvailableStore' : True
            ,'name' : f"Location {_+1}"
            ,'nextPickupCutOffTime' : fake.date_time()
            ,'parent_id' : 0
            ,'returnAddress_id' : fake.address() 
            ,'soPredConfidence' : 0
            ,'soPredictedDays' : 0
            ,'storePickupBufferStock' : random.uniform(10.0, 100.0)
            ,'subsidiaryList' : []
            ,'timeZone' : fake.timezone()
            ,'totalShippingCapacity' : random.uniform(10.0, 100.0)
        } 
        data.append(record)
    return data


# In[37]:


location_records = generate_location_data(25)


# In[38]:


location_dataframe = pl.DataFrame(location_records)


# In[39]:


location_dataframe.head()


# In[5]:


conn = duckdb.connect(db_path)


# In[121]:


conn.execute("CREATE OR REPLACE TABLE LOCATION AS SELECT * FROM location_dataframe")


# In[122]:


conn.sql("SELECT * FROM LOCATION").pl()


# In[77]:


location_ids = [row[0] for row in location_dataframe.select('locationId').iter_rows()]


# In[ ]:


location_ids


# In[100]:


def generate_accounts(location_ids):

    """
    Base account numbers and names names taken from https://strategiccfo.com/articles/accounting/standard-chart-of-accounts/

    1010 CASH Operating Account
    1320 INV – Work-in-Progress
    1330 INV – Finished Goods
    2110 A/P Trade
    4010 Revenue
    5010 COGS

    Modeled account numbers and names for this example.
    Highly simplified to fit the cookie shop business model and to abide by time constraints. 

    1{location_id} - CASH Operating Account
    2{location_id} - Work-in-progress cookies
    3{location_id} - Finished cookies
    4{location_id} - Revenue
    5{location_id} - COGS
    6{location_id} - Trade Expenses

    """
    most_recent_account_id = 0
    total_number_of_accounts = 6
    end_account_id = 0
    data = []
    for location_id in location_ids:
        account_number_base = [1,2,3,4,5,6]
        account_name_base = ["Cash", "Work-in-progress cookies", "Finished cookies", "Revenue", "COGS", "Trade Expenses"]
        acctType_base = [0,2,2,21,23,24]
        for _ in range(total_number_of_accounts):
            if "cookies" in account_name_base:
                is_inventory = True
            else:
                is_inventory = False
            account_name = account_name_base[_] + f" for location_id {location_id}"
            externalId_string = ''.join([fake.emoji() for x in range(8)])
            internalId_string = ''.join([fake.emoji() for x in range(8)])
            record = {
                 "accountId": _ + end_account_id
                ,"acctName": account_name
                ,"acctNumber": str(account_number_base[_])+str(location_id)
                ,"acctType": acctType_base[_]
                # 0 - Bank 1 - Accts Receivable 2 - Inventory 4 - Other Curr Assets 5 - Fixed Assets 6 - Accum Deprec. 8 - Other Assets 10 - Accts Payable 12 - Oth Curr Liab. 14 - Long Term Liab. 16 - Equity-No Close 18 - Retained Earnings 19 - Equity-Closes 21 - Income 23 - COGS 24 - Expense 25 - Other Income 26 - Other Expense 
                ,"billableExpensesAcct": False
                ,"cashFlowRate": 1 #Will actually be set for foreign currency, but for the first draft example we will assume that everything is contracted in Bitcoin. 
                ,"category1099misc": False
                ,"class_id": random.uniform(100.0, 10000.0)
                ,"curDocNum": str(random.randint(1000, 9999))
                ,"currency_id": 0
                ,"customFieldList_id": random.uniform(100.0, 10000.0)
                ,"deferralAcct_id": random.uniform(100.0, 10000.0)
                ,"department_id": random.uniform(100.0, 10000.0)
                ,"description": fake.text()
                ,"eliminate": False
                ,"exchangeRate": 1
                ,"generalRate": "_current"
                ,"includeChildren": False
                ,"inventory": is_inventory
                ,"isInactive": False
                ,"legalName": f"Your mom's {account_name}"
                ,"localizationsList": []
                ,"location_id": location_id
                ,"openingBalance": 0.00
                ,"parent_id": 0
                ,"restrictToAccountingBookList_id": 0
                ,"revalue": False
                ,"subsidiaryList_id": 0
                ,"tranDate": fake.date()
                ,"unit_id": 0 
                ,"unitsType_id":  0
                ,"externalId": externalId_string
                ,"internalId": internalId_string
            }
            data.append(record)
        end_account_id = most_recent_account_id + total_number_of_accounts
        most_recent_account_id = _
    return data


# In[101]:


test_location_ids = [0]


# In[ ]:


generate_accounts(test_location_ids)


# In[103]:


location_account_records = generate_accounts(location_ids)


# In[104]:


location_accounts = pl.DataFrame(location_account_records)


# In[ ]:


location_accounts.columns


# In[ ]:


# for row in location_accounts.select("cashFlowRate").iter_rows():
#     print(row[0])
for column in location_accounts.columns:
    print(column)
    for row in location_accounts.select(column).iter_rows():
        print(row[0])


# In[ ]:


dir(fake)


# In[115]:


fake.aba()


# In[116]:


fake.prefix()


# In[142]:


fake.bothify("???").upper()+fake.numerify("######")


# In[131]:


location_accounts.head()


# In[123]:


conn.execute("CREATE OR REPLACE TABLE ACCOUNTS AS SELECT * FROM location_accounts")


# In[179]:


conn.execute("SELECT * FROM ACCOUNTS LIMIT 10").pl() 


# In[154]:


def generate_inventory_items(num_records):
    data = []
    for _ in range(num_records):
        record = {
             "inventoryItemId": _
            ,"itemId": fake.bothify("???").upper()+fake.numerify("######")
            ,"displayName": fake.text()
            ,"accountingBookDetailList_id": random.randrange(100, 10000)
            ,"alternateDemandSourceItem_id": random.randrange(100, 10000)
            ,"assetAccount_id": random.randrange(100, 10000)
            ,"autoLeadTime": random.randrange(1,10)
            ,"autoPreferredStockLevel": random.randrange(1,10)
            ,"autoReorderPoint": random.randrange(1,10)
            ,"billingSchedule_id": random.randrange(1,10)
            ,"billPriceVarianceAcct_id": random.randrange(1,10)
            ,"billQtyVarianceAcct_id": random.randrange(1,10)
            ,"binNumberList_id": random.randrange(1,10)
            ,"class_id":random.randrange(1,10)
            ,"cogsAccount_id":random.randrange(1,10)
            ,"consumptionUnit_id":random.randrange(1,10)
            ,"contingentRevenueHandling":random.randrange(1,10)
            ,"conversionRate":random.randrange(1,10)
            ,"copyDescription": fake.text()
            ,"cost": random.uniform(1.0, 100.0)
            ,"costCategory_id": random.randrange(100, 10000)
            ,"costEstimate": random.uniform(1.0, 100.0) 
            ,"costEstimateType": "_latPurchasePrice"
        }
        data.append(record)
    return data


# In[155]:


num_items = 20


# In[156]:


inventory_items = generate_inventory_items(num_items)


# In[157]:


inventory_items_df = pl.DataFrame(inventory_items)


# In[158]:


inventory_items_df.head()


# In[159]:


conn.execute("CREATE OR REPLACE TABLE INVENTORYITEMS AS SELECT * FROM inventory_items_df")


# In[161]:


conn.execute("SELECT * FROM INVENTORYITEMS LIMIT 2").pl()


# In[164]:


def generate_inventory_item_locations(location_ids):
    inventory_location_names =  ["Receiving","Raw Materials 1","Raw Materials 2","Raw Materials 3","Raw Materials 4","Raw Materials 5","Machine 1","Machine 2","Machine 3","Finished Goods 1","Finished Goods 2","Finished Goods 3","Finished Goods 4","Finished Goods 5"]
    most_recent_inventory_location_id = 0
    total_number_of_inventory_locations = 14
    end_inventory_location_id = 0
    data = []
    for location in location_ids:
        for _ in range(total_number_of_inventory_locations):
            if "Machine" in inventory_location_names[_]:
                isWip = True
            else:
                isWip = False
            record = {
                 "inventoryItemLocationsId": _ + end_inventory_location_id
                ,"inventoryLocationDisplayName": inventory_location_names[_]
                ,"alternateDemandSourceItem_id": random.randrange(1,1000)
                ,"averageCostMli": random.uniform(1.0,100.0)
                ,"backwardConsumptionDays":random.randrange(1,100)
                ,"buildTime":random.uniform(1.0,100.0)
                ,"buildTimeLotSize":random.uniform(1.0,100.0)
                ,"cost":random.uniform(1.0,100.0)
                ,"costingLotSize":random.uniform(1.0,100.0)
                ,"defaultReturnCost":random.uniform(1.0,100.0)
                ,"demandSource_id":random.uniform(1.0,100.0)
                ,"demandTimeFence":random.randrange(1,1000)
                ,"fixedBuildTime":random.randrange(1,1000)
                ,"fixedLotSize":random.randrange(1,1000)
                ,"forwardConsumptionDays":random.randrange(1,1000)
                ,"inventoryCostTemplate_id":random.randrange(1,1000)
                ,"invtClassification":random.randrange(1,1000)
                ,"invtCountInterval":random.randrange(1,1000)
                ,"isWip": isWip
                ,"lastInvtCountDate": fake.date_time()
                ,"lastPurchasePriceMli":random.uniform(1.0,100.0)
                ,"leadTime":random.uniform(1.0,100.0)
                ,"location":location
                ,"locationAllowStorePickup": True
                ,"locationQtyAvailForStorePickup": random.uniform(1.0,100.0)
                ,"locationStorePickupBufferStock":random.uniform(1.0,100.0)
                ,"nextInvtCountDate": fake.date_time()
                ,"onHandValueMli":random.uniform(1.0,100.0)
                ,"periodicLotSizeDays":random.randrange(1,1000)
                ,"periodicLotSizeType": "_monthly"
                ,"preferredStockLevel":random.uniform(1.0,100.0)
                ,"quantityAvailable":random.uniform(1.0,100.0)
                ,"quantityBackOrdered":random.uniform(1.0,100.0)
                ,"quantityCommitted":random.uniform(1.0,100.0)
                ,"quantityOnHand":random.uniform(1.0,100.0)
                ,"quantityOnOrder":random.uniform(1.0,100.0)
                ,"reorderPoint":random.uniform(1.0,100.0)
                ,"supplyReplenishmentMethod_id":random.uniform(1.0,100.0)
                ,"supplyTimeFence":random.uniform(1.0,100.0)
                ,"supplyType_id":random.uniform(1.0,100.0)
            }
            data.append(record)
        
        most_recent_inventory_location_id = _
        end_inventory_location_id = most_recent_inventory_location_id + total_number_of_inventory_locations
    return data


# In[165]:


inventory_item_locations = generate_inventory_item_locations(location_ids)


# In[166]:


inventory_item_locations_df = pl.DataFrame(inventory_item_locations)


# In[170]:


inventory_item_locations_df.tail(20).select("location")


# In[172]:


location_ids


# In[173]:


def load_polars_df_to_duck(connection, table_name, df_name):
    connection.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM {df_name}")
    return conn.execute(f"SELECT * FROM {table_name} LIMIT 5").pl()


# In[174]:


load_polars_df_to_duck(conn, "INVENTORYITEMLOCATIONS", "inventory_item_locations_df")


# In[176]:


# conn.execute("DESCRIBE TABLE ACCOUNT").pl()


# In[180]:


# conn.execute("SELECT acctName FROM ACCOUNTS").pl()


# In[185]:


def generate_purchase_order(location_ids, num_records, max_item_id):
    data = []
    for location in location_ids:
        for _ in range(num_records):
            record = {
                  "purchaseOrderId": _
                 ,"account_id": 0 
                 ,"approvalStatus": "_approved"
                 ,"availableVendorCredit": 0
                 ,"billAddressList_id": 0
                 ,"billingAddress": fake.address()
                 ,"class_id": 0
                 ,"createdDate": fake.date()
                 ,"createdFrom_id": fake.numerify("#########")
                 ,"currency_id": 0
                 ,"currencyName": "Dogecoin"
                 ,"customFieldList_id": 0
                 ,"customForm_id": 0
                 ,"department_id": 0
                 ,"dueDate": fake.date()
                 ,"email": fake.email()
                 ,"employee_id": int(fake.numerify("#########"))
                 ,"entity_id": int(fake.numerify("#########"))
                 ,"entityTaxRegNum_id": random.randrange(1,10000000)
                 ,"exchangeRate": 1
                 ,"expenseList_id": 0
                 ,"fax": fake.phone_number()
                 ,"fob": "The Store"
                 ,"incoterm_code": None
                 ,"intercoStatus": None
                 ,"intercoTransaction_id": None
                 ,"purchaseOrderitemListId": random.randrange(0,max_item_id)
                 ,"lastModifiedDate": fake.date()
                 ,"linkedTrackingNumbers": int(fake.numerify("#########"))
                 ,"location_id": location
                 ,"memo": fake.text()
                 ,"message": fake.text()
                 ,"nextApprover_id": int(fake.numerify("#########"))
                 ,"nexus_id": int(fake.numerify("#########"))
                 ,"orderStatus": "_pendingReceipt"
                 ,"otherRefNum": int(fake.numerify("#########")) 
                 ,"purchaseContract_id": int(fake.numerify("#########")) 
                 ,"shipAddress": fake.address()
                 ,"shipDate": fake.date()
                 ,"shipIsResidential": False
                 ,"shipMethod": "rail" 
            } 
            data.append(record)
    return data


# In[186]:


purchase_order_df = pl.DataFrame(generate_purchase_order(location_ids, 100000,4))


# In[187]:


load_polars_df_to_duck(conn, "PURCHASEORDER", "purchase_order_df")


# In[192]:


def generate_work_order(location_ids, num_records, item_range_start, item_range_end):
    data = []
    for location in location_ids:
        for _ in range(num_records):
            record = {
                "workOrderId": _
                ,"account_id": 1
                ,"actualProductionEndDate": fake.date()
                ,"actualProductionStartDate": fake.date()
                ,"assemblyItem_id": random.randrange(item_range_start, item_range_end)
                ,"autoCalculateLag": 0
                ,"billOfMaterials_id": 0
                ,"billOfMaterialsRevision_id": 0
                ,"buildable": random.randrange(0,1000)
                ,"built": random.randrange(0,1000)
                ,"class_id": random.uniform(1.0,100000.0)
                ,"createdDate": fake.date()
                ,"createdFrom_id": int(fake.numerify("#########")) 
                ,"currency_id": 0
                ,"currencyName": "Dogecoin"
                ,"customFieldList_id": 0
                ,"customForm_id": 0
                ,"department_id": 0
                ,"dueDate": fake.date()
                ,"email": fake.email()
                ,"employee_id": int(fake.numerify("#########")) 
                ,"entity_id":   int(fake.numerify("#########")) 
                ,"workOrderitemListId": random.randrange(item_range_start, item_range_end)
                ,"job_id": 0
                ,"lastModifiedDate": fake.date()
                ,"location_id": location
                ,"manufacturingRouting_id": random.randrange(0,4)
                ,"memo": fake.text()
                ,"options_id": 0
                ,"orderStatus":"_closed"
                ,"partnersList_id": 0
                ,"quantity": random.randrange(1,50)
                ,"requestedDate": fake.date()
                ,"revision_id": 0
                ,"salesTeamList_id": 0
                ,"schedulingMethod": "_forward"
                ,"sourceTransactionId": fake.bothify("??????????#####")
                ,"sourceTransactionLine": 0
                ,"specialOrder": False
                ,"startDate": fake.date()
                ,"status": "_completed"
                ,"subsidiary_id": 0 
            } 
            data.append(record)
    return data


# In[196]:


def generate_sales_order(location_ids, num_records, item_range_start, item_range_end):
    data = []
    for location in location_ids:
        for _ in range(num_records):
            record = {
                 'accountingBookDetailList_id': random.randint(1, 100)
                ,'actualShipDate': fake.date()
                ,'altHandlingCost': random.uniform(10.0, 100.0)
                ,'altSalesTotal': random.uniform(100.0, 1000.0)
                ,'altShippingCost': random.uniform(5.0, 50.0)
                ,'authCode': fake.bothify(text='????-####-####-####')
                ,'balance': random.uniform(100.0, 10000.0)
                ,'billAddressList_id': random.randint(1, 100)
                ,'billingAddress_id': random.randint(1, 100)
                ,'billingSchedule_id': random.randint(1, 100)
                ,'canHaveStackable': fake.boolean()
                ,'ccApproved': fake.boolean()
                ,'ccAvsStreetMatch': fake.random_element(elements=('Y', 'N', 'X'))
                ,'ccAvsZipMatch': fake.random_element(elements=('Y', 'N', 'X'))
                ,'ccExpireDate': fake.date()
                ,'ccName': fake.name()
                ,'ccNumber': fake.credit_card_number(card_type=None)
                ,'ccSecurityCode': fake.credit_card_security_code(card_type=None)
                ,'ccStreet': fake.street_address()
                ,'ccZipCode': fake.zipcode()
                ,'checkNumber': str(random.randint(1000, 9999))
                ,'class_id': random.randint(1, 100)
                ,'contribPct': str(random.uniform(0, 100)) + '%'
                ,'createdDate': fake.date()
                ,'createdFrom_id': random.randint(1, 100)
                ,'creditCard_id': random.randint(1, 100)
                ,'creditCardProcessor_id': random.randint(1, 100)
                ,'currency_id': random.randint(1, 100)
                ,'currencyName': fake.currency_name()
                ,'customFieldList_id': random.randint(1, 100)
                ,'customForm_id': random.randint(1, 100)
                ,'debitCardIssueNo': str(random.randint(1, 999))
                ,'deferredRevenue': random.uniform(100.0, 10000.0)
                ,'department_id': random.randint(1, 100)
                ,'discountItem_id': random.randint(1, 100)
                ,'discountRate': str(random.uniform(0, 100)) + '%'
                ,'location_id': location
                ,'item_id': random.randrange(item_range_start, item_range_end)
                # その他のフィールド
            }
            data.append(record)
    return data



# In[205]:


work_order_df = pl.DataFrame(generate_work_order(location_ids, 100000,4,8))


# In[206]:


sales_order_df = pl.DataFrame(generate_sales_order(location_ids, 100000,4,8))


# In[207]:


# len(work_order_df)


# In[208]:


# len(sales_order_df)


# In[209]:


# len(purchase_order_df)


# In[210]:


load_polars_df_to_duck(conn, "WORKORDER", "work_order_df")


# In[211]:


load_polars_df_to_duck(conn, "SALESORDER", "sales_order_df")




# dir(fake)


# In[213]:


# dir(random)


# In[222]:


# def generate_uk_station_api_response():
#     train_id = fake.bothify("#").upper()+fake.numerify("#####")
#     response =  {
#       "date": fake.date()
#       ,"time_of_day": fake.numerify("##:##")
#       ,"request_time": fake.date_time()
#       ,"station_name": fake.city() 
#       ,"station_code": fake.bothify("###").upper()+fake.bothify("###")
#       ,"departures": {
#         "all": [
#             
#           {
#              "mode": "train"
#             ,"service": fake.numerify("#######")
#             ,"train_uid": fake.bothify("#").upper()+fake.numerify("#####")
#             ,"platform": str(int(fake.numerify("##")))
#             ,"operator": fake.bothify("##").upper()
#             ,"operator_name": fake.city() + " Railway"
#             ,"aimed_departure_time": fake.numerify("##:##")
#             ,"aimed_arrival_time": fake.numerify("##:##")
#             ,"aimed_pass_time": None
#             ,"origin_name": fake.city() 
#             ,"destination_name": fake.city() 
#             ,"source": "Network Rail"
#             ,"category": fake.numerify("##")
#             ,"service_timetable": {
#               "id": f"http://transportapi.com/v3/uk/train/service_timetables/{train_id}:{fake.date()}?live=true"
#             }
#             ,"status": random.choice(["EARLY","ON-TIME","LATE", "YOUR MOM"])
#             ,"expected_arrival_time": fake.numerify("##:##")
#             ,"expected_departure_time": fake.numerify("##:##")
#             ,"best_arrival_estimate_mins": str(int(fake.numerify("###")))
#             ,"best_departure_estimate_mins": str(int(fake.numerify("###")))
#           } for train in range(0,random.randrange(1,25))
#         ]
#       }
#     }
#     return response


# # In[223]:


# generate_uk_station_api_response()


# # In[224]:


# fake.time()


# # In[225]:


# dir(fake)


# # In[232]:


# fake.time()[:5]


# # In[233]:


# fake.date()


# # In[240]:


# def generate_uk_train_api_response():
#     response = {
#           "request_time": fake.date_time()
#           ,"service": fake.numerify("########")
#           ,"train_uid": fake.bothify("#").upper()+fake.numerify("#####")
#           ,"headcode": fake.numerify("####")
#           ,"toc": {
#             "atoc_code": fake.bothify("##")
#           }
#           ,"train_status": "1"
#           ,"mode": "train"
#           ,"category": fake.numerify("##")
#           ,"operator": fake.bothify("??").upper()
#           ,"operator_name": fake.city() + " Railway"
#           ,"stop_of_interest": fake.bothify("???").upper()
#           ,"origin_name": fake.city() 
#           ,"destination_name": fake.city() 
#           ,"stops": [
#             {
#                "station_code": fake.bothify("???").upper()
#               ,"tiploc_code": fake.bothify("??????").upper()
#               ,"station_name": fake.city() 
#               ,"status": random.choice(["EARLY","ON-TIME","LATE", "YOUR MOM"])
#               ,"stop_type": random.choice(["LO", "LI", "LT", "YOUR MOM"])
#               ,"platform": str(random.randrange(1,30))
#               ,"aimed_arrival_date": fake.date()
#               ,"aimed_arrival_time": fake.time()[:5]
#               ,"aimed_pass_date": fake.date() 
#               ,"aimed_pass_time": fake.time()[:5]
#               ,"aimed_departure_date": fake.date() 
#               ,"aimed_departure_time": fake.time()[:5]
#               ,"expected_arrival_date": fake.date()
#               ,"expected_arrival_time":fake.time()[:5]
#               ,"expected_pass_date": fake.date()
#               ,"expected_pass_time":fake.time()[:5]
#               ,"expected_departure_date":fake.date()
#               ,"expected_departure_time":fake.time()[:5]
#             }
#                 for stop in range(1,random.randrange(2,30))
#           ]
#         }
#     return response


# # In[241]:


# generate_uk_train_api_response()


# # In[242]:


# fake.add_provider("ja_JP.Provider")


# # In[249]:


# fake.provider("ja_JP.Provider")


# # In[250]:


# fake_jp = Faker("ja_JP")


# # In[251]:


# fake_jp.address()


# # In[252]:


# from xpinyin import Pinyin
# p = Pinyin()


# # In[253]:


# fake = Faker("zh_CN")


# # In[255]:


# from xpinyin import Pinyin
# p = Pinyin()


# # In[267]:


# def get_station_name():
#     station_name_cn = fake.city()
#     station_name_pn = p.get_pinyin(station_name_cn,"")
#     return (station_name_cn, station_name_pn)


# # In[268]:


# get_station_name()


# # In[269]:


# dir(fake)


# # In[281]:


# fake.tld()


# # In[289]:


# fake.numerify("#h##m")


# # In[316]:


# def generate_china_station_api_response():
#     fake = Faker("zh_CN")
#     def get_station_name():
#         station_name_cn = fake.city()
#         station_name_pn = p.get_pinyin(station_name_cn,"")
#         return (station_name_cn, station_name_pn)
#     stations_for_station_response = get_station_name()
#     station_response = \
#         {
#           "StatusCode": random.choice(["200","500", "YOUR MOM"])
#           ,"StationNameEN": stations_for_station_response[0] 
#           ,"StationNameCN": stations_for_station_response[1]
#         }
#     train_response_max = random.randrange(1,50)
#     train_response_range = range(0,train_response_max)
#     train_response_stations = [(get_station_name(), get_station_name()) for station in train_response_range]
#     train_response = [
#             
#     {
#       "TrainNo": fake.bothify("?").upper() + fake.numerify("####")
#       ,"DepTime": fake.time()[:5] 
#       ,"ArrTime": fake.time()[:5]
#       ,"Duration":fake.numerify("#h##m")
#       ,"DepStationEN": train_response_stations[train][0][0]
#       ,"DepStationCN": train_response_stations[train][0][1]
#       ,"ArrStationEN": train_response_stations[train][1][0] 
#       ,"ArrStationCN": train_response_stations[train][1][1]       }
#         for train in  train_response_range
#     ]
#     station_response["Trains"] = train_response
#     return station_response


# # In[318]:


# generate_china_station_api_response()


# # In[324]:


# def generate_china_train_api_response():
#     fake = Faker("zh_CN")
#     def get_station_name():
#         station_name_cn = fake.city()
#         station_name_pn = p.get_pinyin(station_name_cn,"")
#         return (station_name_cn, station_name_pn)
#     
#     train_response = \
#         {
#           "StatusCode": random.choice(["200","500", "YOUR MOM"])
#         }
#     train_no = fake.bothify("?#").upper()
#     timetable_response_max = random.randrange(1,50)
#     timetable_response_range = range(0,timetable_response_max)
#     timetable_response_stations = [get_station_name() for station in timetable_response_range]
#     timetable_response = [
#             
#     {
#       "TrainNo": train_no
#       ,"StationNo": timetable+1
#       ,"StationNameEN": timetable_response_stations[timetable][0]
#       ,"StationNameCN": timetable_response_stations[timetable][1]
#       ,"ArriveTime": fake.time()[:5] 
#       ,"StartTime": fake.time()[:5] 
#       ,"StopTime": fake.numerify("##min")
#     }
#         for timetable in  timetable_response_range
#     ]
#     train_response["TimeTable"] = timetable_response
#     return train_response


# # In[339]:


# generate_china_train_api_response()


# # In[340]:


# dir(fake)


# # In[352]:


# fake = Faker("en_US")


# # In[350]:


# fake.city()


# # In[356]:


# fake.timezone()


# # In[358]:


# str(fake.latitude())


# # In[359]:


# fake.longitude()


# # In[363]:


# fake.address()


# # In[366]:


# fake.state()


# # In[367]:


# dir(fake)


# # In[370]:


# fake.state_abbr()


# # In[372]:


# fake.zipcode()


# # In[395]:


# def generate_us_station_api_response():
#     fake = Faker("en_US")
#     station_code = fake.bothify("???").upper()
#     station_city = fake.city()
#     response = {
#         station_code:{
#             "name": station_city + " Union Station"
#             ,"code": station_code
#             ,"tz": fake.timezone() 
#             ,"lat": str(fake.latitude())
#             ,"lon": str(fake.longitude())
#             ,"address1": fake.address()
#             ,"address2" : ""
#             ,"city": station_city
#             ,"state": fake.state_abbr()
#             ,"zip": fake.zipcode()
#             ,"trains": [
#                 {
#                      "TrainNo": fake.numerify("%-%")
#                     ,"DepartureTime": fake.time()[:5]
#                     ,"ArrivalTime": fake.time()[:5]
#                     ,"Stops": [
#                       {
#                          "StopStation": fake.city()
#                         ,"ArrivalTime": fake.time()[:5] 
#                         ,"DepartureTime": fake.time()[:5] 
#                       }
#                  for stop in range(0,10)     
#                     ]
#                 }
#             for train in range (0,10)
#             ]
#         }
#     }
#     return response


# # In[396]:


# generate_us_station_api_response()


# # In[412]:


# def generate_us_train_api_response():
#     fake = Faker("en_US")
#     train_no = str(random.randrange(1,15))
#     train_id =  train_no + "_" + str((int(train_no)+2))
#     response = {
#         train_no:{
#           "routeName": fake.city() + random.choice([" Zephyr", " Express", " Limited", " Builder"])
#           ,"trainNum": train_no 
#           ,"trainID": train_id
#           ,"lat": str(fake.latitude())
#           ,"lon": str(fake.longitude())
#           ,"trainTimely": random.choice(["Yes", "No", "Sir, this is Amtrak"])
#           ,"stations": [
#                 {
#                     
#                    "name": fake.city() + " Union Station" 
#                   ,"code": fake.lexify("???").upper()
#                   ,"tz": fake.timezone() 
#                   ,"bus": False
#                   ,"schArr": fake.date_time()
#                   ,"schDep": fake.date_time()
#                   ,"arr": fake.date_time()
#                   ,"dep": fake.date_time()
#                   ,"arrCmnt": f"{random.randrange(0,10)} Minutes Early"
#                   ,"depCmnt": f"{random.randrange(0,10)} Minutes Early"
#                   ,"status": random.choice(["Arriving", "Arrived", "Departed", "Making Cookies"])
#                 }
#                 for station in range(0, random.randrange(1,25))
#               ]
#         }
#     }
#     return response


# # In[416]:


# generate_us_train_api_response()


# # In[447]:


# def generate_japan_station_api_response():
#     fake = Faker("ja_JP")
#     response =  {
#   "ResultSet": {
#      "apiVersion": "1.27.0.0"
#     ,"engineVersion": "201802_03a"
#     ,"TimeTable": {
#        "trainCount": random.randrange(1,300)
#       ,"code": fake.numerify("####")
#       ,"dateGroup": random.choice(["weekday","weekend","holiday","your mom"])
#       ,"Station": {
#         "Name": fake.city()
#       }
#       ,"HourTable": [
#         {
#            "TimeReliability": "onTimeTable"
#           ,"MinuteTable": [
#             {
#                "Minute": random.randrange(0,59)
#               ,"Stop": {
#                  "kindCode":  fake.numerify("%")
#                 ,"platformNo": random.randrange(1,40)
#                 ,"lineCode": fake.numerify("#####")
#                 ,"nameCode": random.randrange(1,200)
#                 ,"destinationCode": random.randrange(1,200)
#               }
#             }
#             for minute in range(0,random.randrange(1,8))
#           ] 
#           ,"Hour": hour
#         }
#         for hour in range(0,random.randrange(1,24))
#       ]
#       ,"Line": {
#          "Name": fake.city()+"線"
#         ,"Direction": fake.city()
#         ,"Source": fake.city() 
#         ,"Color": fake.numerify("#########")
#       }
#       ,"LineName": {
#          "text": "無し"
#         ,"code": "1"
#       }
#       ,"LineDestination": [
#         {
#           "text": fake.city()
#           ,"code": random.randrange(1,10000)
#         } 
#         for destination in range(0,random.randrange(1,25))
#       ]
#       ,"LineKind": {
#          "text": random.choice(["各駅停車","快速","特急","新幹線", "Your mom"])
#         ,"code": random.randrange(1,10000)
#       }
#     }
#   }
# }
#     return response


# # In[459]:


# generate_japan_station_api_response()


# # In[473]:


# def generate_japan_train_api_response():
#     fake = Faker("ja_JP")
#     fare = random.randrange(100,100000)
#     def generate_station():
#         return {
#              "code": str(random.randint(10000, 99999))
#             ,"name": fake.street_name()
#             ,"type": "train"
#             ,"yomi": fake.word()
#         }

#     def generate_geo_point():
#         return {
#              "longi": f"{random.randint(100, 139)}.{random.randint(0, 59)}.{random.randint(0, 59)}"
#             ,"lati": f"{random.randint(30, 35)}.{random.randint(0, 59)}.{random.randint(0, 59)}"
#             ,"longi_d": str(fake.longitude())
#             ,"gcs": "tokyo"
#             ,"lati_d": str(fake.latitude())
#         }

#     def generate_line():
#         return {
#              "stopstationcount": str(random.randint(0, 10))
#             ,"timeonboard": str(random.randint(0, 60))
#             ,"exhaustco2": str(random.randint(0, 1000))
#             ,"exhaustco2atpassengercar": str(random.randint(0, 1000))
#             ,"distance": str(random.randint(0, 100))
#             ,"name": fake.company() + "鐵道"
#             ,"type": "train"
#             ,"arrivalstate": {
#                 "type": "normal"
#                 ,"datetime": fake.iso8601()
#             }
#             ,"departurestate": {
#                  "type": "normal"
#                 ,"datetime": fake.iso8601()
#             }
#             ,"color": fake.numerify("#########")
#         }

#     def generate_course():
#         return {
#              "searchtype": "departure"
#             ,"datatype": "ontimetable"
#             ,"serializedata": fake.sha256()
#             ,"price": [
#                 {
#                      "kind": "faresummary"
#                     ,"oneway": str(random.randint(100, 500))
#                     ,"round": str(random.randint(200,1000))
#                 }
#             ]
#             ,"route": {
#                  "timeother": str(random.randint(0, 10))
#                 ,"timeonboard": str(random.randint(0, 60))
#                 ,"exhaustco2": str(random.randint(0, 1000))
#                 ,"exhaustco2atpassengercar": str(random.randint(0, 1000))
#                 ,"distance": str(random.randint(0, 100))
#                 ,"timewalk": str(random.randint(0, 30))
#                 ,"transfercount": str(random.randint(0, 5))
#                 ,"line": [generate_line() for _ in range(3)]
#                 ,"point": [
#                     {
#                         "name": fake.city()
#                     }
#                     ,{
#                          "station": generate_station()
#                         ,"prefecture": {
#                              "code": str(random.randint(1, 47))
#                             ,"name": fake.city()
#                         }
#                         ,"geopoint": generate_geo_point()
#                     }
#                 ]
#             }
#         }

#     api_structure = {
#         "resultset": {
#              "apiversion": "1.27.0.0"
#             ,"engineversion": "201806_02a"
#             ,"course": [generate_course() for _ in range(3)]
#         }
#     }
#     return api_structure


# # In[474]:


# generate_japan_train_api_response()


# # In[476]:


# conn.execute("SHOW TABLES;").pl()


# # In[6]:


# conn.execute("DESCRIBE TABLE ACCOUNTS;").pl()


# # In[7]:


# from deltalake.writer import write_deltalake


# # In[8]:


# delta_lake_path = 'output_data_lake/'


# # In[9]:


# import os


# # In[10]:


# os.getcwd()


# # In[11]:


# delta_lake_path = os.path.join(os.getcwd(), delta_lake_path)


# # In[12]:


# delta_lake_path


# # In[13]:


# table_name = "test_table"


# # In[14]:


# test_frame = conn.execute("DESCRIBE TABLE ACCOUNTS;").pl()


# # In[15]:


# test_frame.write_delta(os.path.join(delta_lake_path, table_name))


# # In[16]:


# test_lazy_df = pl.scan_delta(os.path.join(delta_lake_path, table_name))


# # In[19]:


# conn.execute("SELECT * FROM test_lazy_df LIMIT 10").pl()


# # In[20]:


# duckdb.sql("SELECT column_name FROM test_lazy_df LIMIT 5").pl()


# # In[ ]:




