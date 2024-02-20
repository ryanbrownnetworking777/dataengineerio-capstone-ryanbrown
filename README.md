# Data-Engineer.io Capstone

## Intent

This project sprung from the DataEngineer.io bootcamp I attended in Q4 of 2023, and was due 1/26/2024.

That being said, my intention is not simply to leave this a static document. I bit off way more than I could chew in the first iteration, and I am excited to iterate more upon this far after the original purpose has been completed. 

Before we begin...

## Disclaimer

The following document and associated repository was produced by a grown man with a tendency to engage in attention seeking behaviors on the internet. 

Jokes, memes, sarcasm, melodrama, imaginative narrative, and SAFE FOR WORK juvenile humor may be encountered. 

Side effects of consumption may include but are not limited to laughter, eye rolls, and utterances of the phrases "Seriously?", "Really?", "That's mature..." or similar. 

Author bears no responsibility for facial expressions experienced on camera during video calls while consuming this document when you should have been paying attention. 

Consumption by the overly stiff, joyless, grinchy, and those unable to have any fun is hereby not advised. 

**Consume at your own risk.** 

**You have be clearly, explicitly, and EMPHATICALLY WARNED**


And with that...

Your journey into my capstone project...

Hereby begins. 


## The Lore

Bakehouse Central is where your inner Cookie Monster hangs out. They operate shops in various train stations and smaller outfits **on the trains themselves** in the US, UK, China, and Japan. 

A significantly popular chain, they enjoy a large loyalty program membership and high usage of their Bakehouse Central app.  

Like many large organizations, there exists a glorious contradition of streams of direction and orders. 

### Stream 1 - The Siren Song

Whoever spiked the punch at the conference the CEO attended last year accmplished something absolutely insane. 

Now in any meetings where the words "data", "analysis", or "strategy" come within even a hint of earshot...

Their eyes glaze over. 

Their mouth moves as if entranced. 

"We must become a DATA-DRIVEN company"

Over, over, and over again. 

In American English, British English, Mandarin, and Japanese.

Incessant. 

It gets worse. 

With the success of promotional campaigns tying an event with the arrival of a specific train in each of the markets

Management 

has descended 

into MADNESS. 

Status report requests, "Where's my dashboard?", check-ins, choirs of leadership chanting in agreement. 

The internal corporate emails... 

Complete with branding!

"Celebrating day 39 of our 100 day journey to..."

That email has come out for the past five days. 

Looking at your email you notice the first of it's kind sent...200 days ago. 

It's all just so..._extra_. 

What a vibe.


### Stream 2 - The Rocks

Amidst this fever, this infection, indeed this MIND VIRUS spreading across this enterprise...

A different direction, a different message, a different song reverberates. 

Somber. Brooding. Portending of difficulty to come and difficulty already here. 

A song of _Expectations_.

A song of _Restrictions_.

A song of _Denial_.

No one is exactly sure it's origin. 

The word in the Slack is that the CFO and CTO are leading this countercharge against the euphoria. 

The reasons?

Again, no one knows. 

Perhaps... 


![CloudBillIsTooDamnHighMeme](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/02dd2543-677b-480b-a0e3-a43ccc046e82)


Other rumors abound pertaining to the Cloud Security Team and the Cloud Engineering Team that were both brought in. 

With, allegedly, the Cloud Security chaps vibing like..


![YourNetworkTrafficShallNotPassMeme](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/2c13ce57-07db-46b0-820e-2158ad316dec)

And the Cloud Engineering Team needing to be present for 5 hour daily work sessions for a week to set up a resource. 

One engineering manager burst into tears, started rocking in the fetal position, and endlessly mumbled "oh the JIRA tickets!" when asked. 

Whatever the exact reason.

The *EDICT* is clear. 

Signed with ~~the Royal Seal of~~ the signatures of the CFO and CTO themselves. 

~~In Blood~~

A revelation so terrible, it's on par with revelations of villanous paternity itself.


![TheCloudIsOutMeme](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/9287a5ad-7240-400a-ae79-f126f44f9e1c)

### The Reality Curveball

Being a bakery and not an analytics shop, naturally Bakehouse Central is focused more on oven output and effeciency rather than data. 

And that focus has paid off. 

Their engineers have pioneered new ovens and other robotic machinery to propel on-site production to insane heights. Near real-time production of tasty treats is now possible both on and off train.  

This new production reality...coupled with leadership madness, throws the problems into sharp relief.


### The Problems 

While (most of) the Executive Team is in fact HIGH and the CTO/CFO faction is indeed NIGH, the problems they seek to resolve are real. 

- Cookies are sitting less fresh, overproduced, and not aligned to demand. 
- Supply and Demand planners are operating on yesterdays data, from someone's final_final_v10.xlsx file stored on the network drive, and getting the view down to the machine level and back is a trek of pain and suffering. 
- Profitability is only updated once Accounting finishes their closes, giving store managers right proper frights at the end of the month. 
- Data in general is very..._stale_ in the organization. 

## The Goals

Even with the _Terrible Decree_, the organization moves forward. 

They are shooting for:

- Real time alignment of trains to production of baked goods, ideally with suggested commemerative treats for their loyalty members. (Operational Data use case)
- Updates on sales and profitability of each stores. (Analytics Use Case) 
- Down to machine level operational visibility for supply and demand planners.(Operational & Analytics)
- Hourly refreshing dashboards (Analytics Use Case)

## The Use Cases

Managment _has_ in fact lost their marbles. And yet...

Each of management's demands can be broken down into several distinct use cases that map into different business areas.

These use cases can then have several different business activities and/or data points associated with them. 

### Supply Chain | Operations 

- Real time alignment of trains to production of baked goods, ideally with suggested commemerative treats for their loyalty members. (Operational Data use case)

    Busines activities: 

    - Production Planning 
        - Create a forecast based upon train timetable and potential rolling stock capacity. 

    Data requirements:

    - Current Train state
    - Current WOs
    - Current Capacity 
    - Current POs
    - Current Raw Materials Inventory
    - Current Finished Goods Inventory



- Down to machine level operational visibility for supply and demand planners.  

    - Current WOs
    - Current Capacity 
    - Current POs
    - Current Raw Materials Inventory
    - Current Finished Goods Inventory

### Marketing | Sales 


- Promotional suggestions to loyalty members based upon external events or train happenings.

    Business Activities: 

    - Creating the suggested promotion

    Data Requirements: 

    - Current Train state
    - Current off-train events
    - Loyalty members on those trains
    - Loyalty members going to those events
    - Current inventory
    - Current production capacity

### Finance

- Updates on sales and profitability of each stores. (Analytics Use Case) 

    Business Activities: 
    
   - Financial reporting, specifically the Cash Flow Statement

   Data Requirements:

   - Accounting data for the following types of accounts:
        - Sales
        - Expenses

### IT

- Hourly refreshing dashboards

    Business activities:

    - General support of the business

    Data Requirements:

    - Data Quality
    - Data Health
    - Data Freshness


## The Deliverables

 - A modern data lakehouse, affecionately termed the Data Bakehouse 🍪, that supports operational and analytics use cases with a high refresh rate. 

 - A consolidated internal API endpoint for trains and stations in their four markets.  

 - Reporting and Operational views combining these data sources.

## The Phases 

- Phase 0: Bare bones MVP
    - Objective:
        - Build out the "plumbing" for the ETL. 
        - Submit on the DataEngineer.io deadline. 
    - Data:
        - Absolute 🐄💩 (quite literal nonsense generated with Faker).
    - Front End: 
        - Jupyter Lab Notebook
    - Delivery: January 2024

- Phase 0.5: Slightly meated MVP
    - Objective:
        - Round out the loose ends from Phase 0
    - Data:
        - Slightly less absolute 🐄💩 (quite literal nonsense generated with Faker, BUT with a few more rules).
    - Front End: 
        - Jupyter Lab Notebook
        - Excel (Because yes everything ends up in Excel)
        - Rill
        - Apache Superset
    - Delivery: Q1 2024

- Phase 1: Fully Fleshed Out MVP 
    - Objective:
        - Data in Accross the API and ERP data sources that makes legitimate sense.
    - Data:
        - NOT absolute 🐄💩 (Still generated with Faker, but with significant thought into the actual rules and business model so that values are sensible to an outside observer while still being fictional).
    - Front End: 
        - Jupyter Lab Notebook
        - Excel (Because yes everything ends up in Excel)
        - Rill
        - Apache Superset
    - Delivery: Q2 2024


- Phase 2: Continued iteration
    - Objective:
        - Integration of more Data Engineering best practices. 
        - Plumbing even moar business, data, and strategy rabbit holes.
        - Flights of fancy.
    - Data:
        - Continued iteration and improvement.
    - Front End: 
        - Jupyter Lab Notebook
        - Excel (Because yes everything ends up in Excel)
        - Rill
        - Apache Superset
    - Delivery: Q4 2024

- Phase ♾: Endless tinkering
    - Objective:
        - That one pet project that will never go away.
    - Delivery: When I'm bored of this. 


## The Stack

Bakehouse Central is building their _on premises_ Data Bakehouse 🍪  on the following technology stack:

### Storage
    
- In World: Local network drives. 
- Reality : Local drives. 

### Compute

- 🦆DB
- Polars
- Python

### Storage Format

- Delta Lake
    - Accomplished via [delta-rs](https://github.com/delta-io/delta-rs)

### The Architecture

Delta Lakehouse Medallion architecture with the following layers, all stored on disk:

- Bronze (Raw)
- Silver (Transformed)
- Audit (for Write-Audit-Publish pattern)
- Gold (Serving)

### But Why Tho?

I give all of these justifications as a 5+ year professional delivering data solutions on (almost exclusively) Azure. I enjoy what I do and am proud to deliver for my clients. 

However...

For the purposes of this exercise, my spiky points of view fall into these main areas:

#### Cloud Complexity and Cost

There is a threshold for cloud services that they potentially become more expensive. 

Managing cloud services requires a complex web of set up, network management, permissions, etc, to be successfull.  

Azure Data Lake Storage (Gen 2), as an an example, requires at a minimum the following to be set up for enterprise use based upon my experience:
- Storage Container Permissions
- Network Endpoints (Public or Private)
- Access Control Lists to the *files themselves*
- Hierarchical Namespace Enabled

"Cloud Exit" is somewhat a trending topic in technical social media for the aforementioned reasons (along with probably others not mentioned); with as of this writing one of the most prominent voices being David Heinemeier Hansson of 37Signals. 

In many areas of life, buying is cheaper than renting, why would compute and storage be different?

#### Data Volumes

"Big" Data perhaps is the realm of truly "Big" organizations. 

Bakehouse Central with it's four country footprint *may* be big, and I've also seen entire company data fit into less than 300 GB. 

Therefore why go to all the trouble with distrubuted compute?

#### Bro It's All _Files_

A Data Lakehouse, more tastily known as a Data Bakehouse 🍪, is _quite literally_ a special directory structure _written to disk_. Why are we bringing in other folk's network and disks in storing and managing this?


![AlwaysHasBeenFilesToDisk](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/df28f095-a96c-44c7-ad1b-c856fab04b7d)

Go get yourself a cookie.

#### But Can I Do It?

Data Lakehouses typically have been tied with a distributed processing engine such as Spark. 

Technically validating being able to do the same thing WITHOUT Spark is cool. 

I also had wanted to give Polars a try. 


#### Zig When They Zag

"Moving to the Cloud" is the dominant way of thinking about data processing as of this writing. 

Therefore a counterpoint _deserves_ to be fleshed out and made known. Every approach has pros and cons, and the discussion **must** be broad. I do not believe us as technical practitioners should become married to one specific approach.

#### I Have Done This Before

In my very first role in data ever I built out a very crude data mart for the supply chain department in an envelope company.

The stack was MSSQL Server, JupyterHub run on Ubuntu, and SQL scripts loaded with Windows Task Scheduler.  

Not very fancy, but it didn't cost any money, required no approvals (although my local IT guy hid my network traffic so corporate IT wouldn't know. GOAT), and served the needs of the department. My department even had me showcase my solution to the company president. It remains one of my proudest technical achievements. 

My best automation/enablment story out of that experience was yeeting a report that took (at most) 2 days to complete completely out of our department with a refreshable Excel workbook for the end user. 

Let's do that, but make it modern, built off of open source standards and libraries.  

[The Real Reason](https://www.youtube.com/watch?v=mQJ6q1ZCzsg)

## The Data

### The Sources

#### In-World

##### ERP

Bakehouse Central runs on a variant of [Netsuite](https://www.netsuite.com/portal/products/erp.shtml). 

The Data Bakehouse 🍪 includes the following ERP tables:

- Locations
- InventoryItemLocations
- InventoryItems
- Accounts
- WorkOrders
- PurchaseOrders
- SalesOrders

Data is snapshotted from Production into a separate RDBMS area and read by the ETL pipeline infrastructure.

##### API 

Bakehouse Central's engineering team has/will create a unified ERP endpoint for 8 different external APIs that reflect the train markets in which the company operates.

The endpoints fall into two categories:
- Station
    - Data about a particular station and what services (trains) are departing or arriving at that train station. 
- Train
    - Data about a particular service (train), what stations it is calling at, status, etc. 

The API exposes the following endpoints:
- UK Station
- UK Train
- China Station
- China Train
- US Station
- US Train
- Japan Station
- Japan Train

#### Reality

##### ERP Mockup

🦆DB File containing data organized into the aforementioned tables.

Data generated using [Faker](https://faker.readthedocs.io/en/master/).

Inspired by the [Netsuite Table Documentation](https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_2/schema/record/salesorder.html).

##### Flask API

Flask API with the aforementioned endpoints.

Data generated using [Faker](https://faker.readthedocs.io/en/master/).

Inspired by the following real APIs:

- UK
    
    - Station: [TransportAPI](https://developer.transportapi.com/docs#get-/v3/uk/train/station_timetables/-id-.json).
    - Train: [TransportApi](https://developer.transportapi.com/docs#get-/v3/uk/train/service_timetables/-service-.json).

- China

    - Station: [China Train/Rail Rapid API](https://rapidapi.com/etcloud-etcloud-default/api/china-train-rail).
         - This is the "Search Train Tickets" endpoint as the station endpoint for this API is broken. Response generated with ChatGPT GPT-4. 
    - Train: [China Train/Rail Rapid API](https://rapidapi.com/etcloud-etcloud-default/api/china-train-rail).

- US

    - Station: [Amtrak.js](https://github.com/piemadd/amtrak/tree/master).
        - Based upon documentation and extended with ChatGPT GPT-4.
    - Train: [Amtrak.js](https://github.com/piemadd/amtrak/tree/master).

- Japan 

**Drawn from Japanese versions of the docs**

- Station: [Ekispert Web Service](https://docs.ekispert.com/v1/api/operationLine/timetable.html).
- Train: [Ekispert Web Service](https://docs.ekispert.com/v1/api/search/course/extreme.html).

### The Dictionary

#### Mockup 🦆DB File
```
┌────────────────────────┐
│          Tables        │
│                        │
├────────────────────────┤
│ ACCOUNTS               │
│ INVENTORYITEMLOCATIONS │
│ INVENTORYITEMS         │
│ LOCATION               │
│ PURCHASEORDER          │
│ SALESORDER             │
│ WORKORDER              │
├────────────────────────┤
│        11 rows         │
└────────────────────────┘
```
#### 🦆DB Tables 

```
ACCOUNTS
┌───────┬─────────────────────────────────┬───────────┬─────────┬────────────┬─────────┐
│  cid  │              name               │   type    │ notnull │ dflt_value │   pk    │
│ int32 │             varchar             │  varchar  │ boolean │  varchar   │ boolean │
├───────┼─────────────────────────────────┼───────────┼─────────┼────────────┼─────────┤
│     0 │ accountId                       │ BIGINT    │ false   │            │ false   │
│     1 │ acctName                        │ VARCHAR   │ false   │            │ false   │
│     2 │ acctNumber                      │ VARCHAR   │ false   │            │ false   │
│     3 │ acctType                        │ BIGINT    │ false   │            │ false   │
│     4 │ billableExpensesAcct            │ BOOLEAN   │ false   │            │ false   │
│     5 │ cashFlowRate                    │ BIGINT    │ false   │            │ false   │
│     6 │ category1099misc                │ BOOLEAN   │ false   │            │ false   │
│     7 │ class_id                        │ DOUBLE    │ false   │            │ false   │
│     8 │ curDocNum                       │ VARCHAR   │ false   │            │ false   │
│     9 │ currency_id                     │ BIGINT    │ false   │            │ false   │
│    10 │ customFieldList_id              │ DOUBLE    │ false   │            │ false   │
│    11 │ deferralAcct_id                 │ DOUBLE    │ false   │            │ false   │
│    12 │ department_id                   │ DOUBLE    │ false   │            │ false   │
│    13 │ description                     │ VARCHAR   │ false   │            │ false   │
│    14 │ eliminate                       │ BOOLEAN   │ false   │            │ false   │
│    15 │ exchangeRate                    │ BIGINT    │ false   │            │ false   │
│    16 │ generalRate                     │ VARCHAR   │ false   │            │ false   │
│    17 │ includeChildren                 │ BOOLEAN   │ false   │            │ false   │
│    18 │ inventory                       │ BOOLEAN   │ false   │            │ false   │
│    19 │ isInactive                      │ BOOLEAN   │ false   │            │ false   │
│    20 │ legalName                       │ VARCHAR   │ false   │            │ false   │
│    21 │ localizationsList               │ INTEGER[] │ false   │            │ false   │
│    22 │ location_id                     │ BIGINT    │ false   │            │ false   │
│    23 │ openingBalance                  │ DOUBLE    │ false   │            │ false   │
│    24 │ parent_id                       │ BIGINT    │ false   │            │ false   │
│    25 │ restrictToAccountingBookList_id │ BIGINT    │ false   │            │ false   │
│    26 │ revalue                         │ BOOLEAN   │ false   │            │ false   │
│    27 │ subsidiaryList_id               │ BIGINT    │ false   │            │ false   │
│    28 │ tranDate                        │ VARCHAR   │ false   │            │ false   │
│    29 │ unit_id                         │ BIGINT    │ false   │            │ false   │
│    30 │ unitsType_id                    │ BIGINT    │ false   │            │ false   │
│    31 │ externalId                      │ VARCHAR   │ false   │            │ false   │
│    32 │ internalId                      │ VARCHAR   │ false   │            │ false   │
├───────┴─────────────────────────────────┴───────────┴─────────┴────────────┴─────────┤
│ 33 rows                                                                    6 columns │
└──────────────────────────────────────────────────────────────────────────────────────┘

```



INVENTORYITEMLOCATIONS


```
┌───────┬────────────────────────────────┬───────────┬─────────┬────────────┬─────────┐
│  cid  │              name              │   type    │ notnull │ dflt_value │   pk    │
│ int32 │            varchar             │  varchar  │ boolean │  varchar   │ boolean │
├───────┼────────────────────────────────┼───────────┼─────────┼────────────┼─────────┤
│     0 │ inventoryItemLocationsId       │ BIGINT    │ false   │            │ false   │
│     1 │ inventoryLocationDisplayName   │ VARCHAR   │ false   │            │ false   │
│     2 │ alternateDemandSourceItem_id   │ BIGINT    │ false   │            │ false   │
│     3 │ averageCostMli                 │ DOUBLE    │ false   │            │ false   │
│     4 │ backwardConsumptionDays        │ BIGINT    │ false   │            │ false   │
│     5 │ buildTime                      │ DOUBLE    │ false   │            │ false   │
│     6 │ buildTimeLotSize               │ DOUBLE    │ false   │            │ false   │
│     7 │ cost                           │ DOUBLE    │ false   │            │ false   │
│     8 │ costingLotSize                 │ DOUBLE    │ false   │            │ false   │
│     9 │ defaultReturnCost              │ DOUBLE    │ false   │            │ false   │
│    10 │ demandSource_id                │ DOUBLE    │ false   │            │ false   │
│    11 │ demandTimeFence                │ BIGINT    │ false   │            │ false   │
│    12 │ fixedBuildTime                 │ BIGINT    │ false   │            │ false   │
│    13 │ fixedLotSize                   │ BIGINT    │ false   │            │ false   │
│    14 │ forwardConsumptionDays         │ BIGINT    │ false   │            │ false   │
│    15 │ inventoryCostTemplate_id       │ BIGINT    │ false   │            │ false   │
│    16 │ invtClassification             │ BIGINT    │ false   │            │ false   │
│    17 │ invtCountInterval              │ BIGINT    │ false   │            │ false   │
│    18 │ isWip                          │ BOOLEAN   │ false   │            │ false   │
│    19 │ lastInvtCountDate              │ TIMESTAMP │ false   │            │ false   │
│    20 │ lastPurchasePriceMli           │ DOUBLE    │ false   │            │ false   │
│    21 │ leadTime                       │ DOUBLE    │ false   │            │ false   │
│    22 │ location                       │ BIGINT    │ false   │            │ false   │
│    23 │ locationAllowStorePickup       │ BOOLEAN   │ false   │            │ false   │
│    24 │ locationQtyAvailForStorePickup │ DOUBLE    │ false   │            │ false   │
│    25 │ locationStorePickupBufferStock │ DOUBLE    │ false   │            │ false   │
│    26 │ nextInvtCountDate              │ TIMESTAMP │ false   │            │ false   │
│    27 │ onHandValueMli                 │ DOUBLE    │ false   │            │ false   │
│    28 │ periodicLotSizeDays            │ BIGINT    │ false   │            │ false   │
│    29 │ periodicLotSizeType            │ VARCHAR   │ false   │            │ false   │
│    30 │ preferredStockLevel            │ DOUBLE    │ false   │            │ false   │
│    31 │ quantityAvailable              │ DOUBLE    │ false   │            │ false   │
│    32 │ quantityBackOrdered            │ DOUBLE    │ false   │            │ false   │
│    33 │ quantityCommitted              │ DOUBLE    │ false   │            │ false   │
│    34 │ quantityOnHand                 │ DOUBLE    │ false   │            │ false   │
│    35 │ quantityOnOrder                │ DOUBLE    │ false   │            │ false   │
│    36 │ reorderPoint                   │ DOUBLE    │ false   │            │ false   │
│    37 │ supplyReplenishmentMethod_id   │ DOUBLE    │ false   │            │ false   │
│    38 │ supplyTimeFence                │ DOUBLE    │ false   │            │ false   │
│    39 │ supplyType_id                  │ DOUBLE    │ false   │            │ false   │
├───────┴────────────────────────────────┴───────────┴─────────┴────────────┴─────────┤
│ 40 rows                                                                   6 columns │
└─────────────────────────────────────────────────────────────────────────────────────┘

```

INVENTORYITEMS


```

┌───────┬──────────────────────────────┬─────────┬─────────┬────────────┬─────────┐
│  cid  │             name             │  type   │ notnull │ dflt_value │   pk    │
│ int32 │           varchar            │ varchar │ boolean │  varchar   │ boolean │
├───────┼──────────────────────────────┼─────────┼─────────┼────────────┼─────────┤
│     0 │ inventoryItemId              │ BIGINT  │ false   │            │ false   │
│     1 │ itemId                       │ VARCHAR │ false   │            │ false   │
│     2 │ displayName                  │ VARCHAR │ false   │            │ false   │
│     3 │ accountingBookDetailList_id  │ BIGINT  │ false   │            │ false   │
│     4 │ alternateDemandSourceItem_id │ BIGINT  │ false   │            │ false   │
│     5 │ assetAccount_id              │ BIGINT  │ false   │            │ false   │
│     6 │ autoLeadTime                 │ BIGINT  │ false   │            │ false   │
│     7 │ autoPreferredStockLevel      │ BIGINT  │ false   │            │ false   │
│     8 │ autoReorderPoint             │ BIGINT  │ false   │            │ false   │
│     9 │ billingSchedule_id           │ BIGINT  │ false   │            │ false   │
│    10 │ billPriceVarianceAcct_id     │ BIGINT  │ false   │            │ false   │
│    11 │ billQtyVarianceAcct_id       │ BIGINT  │ false   │            │ false   │
│    12 │ binNumberList_id             │ BIGINT  │ false   │            │ false   │
│    13 │ class_id                     │ BIGINT  │ false   │            │ false   │
│    14 │ cogsAccount_id               │ BIGINT  │ false   │            │ false   │
│    15 │ consumptionUnit_id           │ BIGINT  │ false   │            │ false   │
│    16 │ contingentRevenueHandling    │ BIGINT  │ false   │            │ false   │
│    17 │ conversionRate               │ BIGINT  │ false   │            │ false   │
│    18 │ copyDescription              │ VARCHAR │ false   │            │ false   │
│    19 │ cost                         │ DOUBLE  │ false   │            │ false   │
│    20 │ costCategory_id              │ BIGINT  │ false   │            │ false   │
│    21 │ costEstimate                 │ DOUBLE  │ false   │            │ false   │
│    22 │ costEstimateType             │ VARCHAR │ false   │            │ false   │
├───────┴──────────────────────────────┴─────────┴─────────┴────────────┴─────────┤
│ 23 rows                                                               6 columns │
└─────────────────────────────────────────────────────────────────────────────────┘


```

LOCATION


```
┌───────┬───────────────────────────────┬───────────┬─────────┬────────────┬─────────┐
│  cid  │             name              │   type    │ notnull │ dflt_value │   pk    │
│ int32 │            varchar            │  varchar  │ boolean │  varchar   │ boolean │
├───────┼───────────────────────────────┼───────────┼─────────┼────────────┼─────────┤
│     0 │ locationId                    │ BIGINT    │ false   │            │ false   │
│     1 │ allowStorePickup              │ BOOLEAN   │ false   │            │ false   │
│     2 │ autoAssignmentRegionSetting   │ VARCHAR   │ false   │            │ false   │
│     3 │ bufferStock                   │ DOUBLE    │ false   │            │ false   │
│     4 │ dailyShippingCapacity         │ DOUBLE    │ false   │            │ false   │
│     5 │ excludeLocationRegionsList_id │ DOUBLE    │ false   │            │ false   │
│     6 │ geolocationMethod             │ VARCHAR   │ false   │            │ false   │
│     7 │ includeChildren               │ BOOLEAN   │ false   │            │ false   │
│     8 │ includeInControlTower         │ BOOLEAN   │ false   │            │ false   │
│     9 │ includeLocationRegionsList    │ INTEGER[] │ false   │            │ false   │
│    10 │ isInactive                    │ BOOLEAN   │ false   │            │ false   │
│    11 │ latitude                      │ DOUBLE    │ false   │            │ false   │
│    12 │ locationType                  │ VARCHAR   │ false   │            │ false   │
│    13 │ logo                          │ BLOB      │ false   │            │ false   │
│    14 │ longitude                     │ DOUBLE    │ false   │            │ false   │
│    15 │ mainAddress_id                │ VARCHAR   │ false   │            │ false   │
│    16 │ makeInventoryAvailable        │ BOOLEAN   │ false   │            │ false   │
│    17 │ makeInventoryAvailableStore   │ BOOLEAN   │ false   │            │ false   │
│    18 │ name                          │ VARCHAR   │ false   │            │ false   │
│    19 │ nextPickupCutOffTime          │ TIMESTAMP │ false   │            │ false   │
│    20 │ parent_id                     │ BIGINT    │ false   │            │ false   │
│    21 │ returnAddress_id              │ VARCHAR   │ false   │            │ false   │
│    22 │ soPredConfidence              │ BIGINT    │ false   │            │ false   │
│    23 │ soPredictedDays               │ BIGINT    │ false   │            │ false   │
│    24 │ storePickupBufferStock        │ DOUBLE    │ false   │            │ false   │
│    25 │ subsidiaryList                │ INTEGER[] │ false   │            │ false   │
│    26 │ timeZone                      │ VARCHAR   │ false   │            │ false   │
│    27 │ totalShippingCapacity         │ DOUBLE    │ false   │            │ false   │
├───────┴───────────────────────────────┴───────────┴─────────┴────────────┴─────────┤
│ 28 rows                                                                  6 columns │
└────────────────────────────────────────────────────────────────────────────────────┘


```

PURCHASEORDER


```
┌───────┬─────────────────────────┬─────────┬─────────┬────────────┬─────────┐
│  cid  │          name           │  type   │ notnull │ dflt_value │   pk    │
│ int32 │         varchar         │ varchar │ boolean │  varchar   │ boolean │
├───────┼─────────────────────────┼─────────┼─────────┼────────────┼─────────┤
│     0 │ purchaseOrderId         │ BIGINT  │ false   │            │ false   │
│     1 │ account_id              │ BIGINT  │ false   │            │ false   │
│     2 │ approvalStatus          │ VARCHAR │ false   │            │ false   │
│     3 │ availableVendorCredit   │ BIGINT  │ false   │            │ false   │
│     4 │ billAddressList_id      │ BIGINT  │ false   │            │ false   │
│     5 │ billingAddress          │ VARCHAR │ false   │            │ false   │
│     6 │ class_id                │ BIGINT  │ false   │            │ false   │
│     7 │ createdDate             │ VARCHAR │ false   │            │ false   │
│     8 │ createdFrom_id          │ VARCHAR │ false   │            │ false   │
│     9 │ currency_id             │ BIGINT  │ false   │            │ false   │
│    10 │ currencyName            │ VARCHAR │ false   │            │ false   │
│    11 │ customFieldList_id      │ BIGINT  │ false   │            │ false   │
│    12 │ customForm_id           │ BIGINT  │ false   │            │ false   │
│    13 │ department_id           │ BIGINT  │ false   │            │ false   │
│    14 │ dueDate                 │ VARCHAR │ false   │            │ false   │
│    15 │ email                   │ VARCHAR │ false   │            │ false   │
│    16 │ employee_id             │ BIGINT  │ false   │            │ false   │
│    17 │ entity_id               │ BIGINT  │ false   │            │ false   │
│    18 │ entityTaxRegNum_id      │ BIGINT  │ false   │            │ false   │
│    19 │ exchangeRate            │ BIGINT  │ false   │            │ false   │
│    20 │ expenseList_id          │ BIGINT  │ false   │            │ false   │
│    21 │ fax                     │ VARCHAR │ false   │            │ false   │
│    22 │ fob                     │ VARCHAR │ false   │            │ false   │
│    23 │ incoterm_code           │ INTEGER │ false   │            │ false   │
│    24 │ intercoStatus           │ INTEGER │ false   │            │ false   │
│    25 │ intercoTransaction_id   │ INTEGER │ false   │            │ false   │
│    26 │ purchaseOrderitemListId │ BIGINT  │ false   │            │ false   │
│    27 │ lastModifiedDate        │ VARCHAR │ false   │            │ false   │
│    28 │ linkedTrackingNumbers   │ BIGINT  │ false   │            │ false   │
│    29 │ location_id             │ BIGINT  │ false   │            │ false   │
│    30 │ memo                    │ VARCHAR │ false   │            │ false   │
│    31 │ message                 │ VARCHAR │ false   │            │ false   │
│    32 │ nextApprover_id         │ BIGINT  │ false   │            │ false   │
│    33 │ nexus_id                │ BIGINT  │ false   │            │ false   │
│    34 │ orderStatus             │ VARCHAR │ false   │            │ false   │
│    35 │ otherRefNum             │ BIGINT  │ false   │            │ false   │
│    36 │ purchaseContract_id     │ BIGINT  │ false   │            │ false   │
│    37 │ shipAddress             │ VARCHAR │ false   │            │ false   │
│    38 │ shipDate                │ VARCHAR │ false   │            │ false   │
│    39 │ shipIsResidential       │ BOOLEAN │ false   │            │ false   │
│    40 │ shipMethod              │ VARCHAR │ false   │            │ false   │
├───────┴─────────────────────────┴─────────┴─────────┴────────────┴─────────┤
│ 41 rows                                                          6 columns │
└────────────────────────────────────────────────────────────────────────────┘


```

SALESORDER


```
┌───────┬─────────────────────────────┬─────────┬─────────┬────────────┬─────────┐
│  cid  │            name             │  type   │ notnull │ dflt_value │   pk    │
│ int32 │           varchar           │ varchar │ boolean │  varchar   │ boolean │
├───────┼─────────────────────────────┼─────────┼─────────┼────────────┼─────────┤
│     0 │ accountingBookDetailList_id │ BIGINT  │ false   │            │ false   │
│     1 │ actualShipDate              │ VARCHAR │ false   │            │ false   │
│     2 │ altHandlingCost             │ DOUBLE  │ false   │            │ false   │
│     3 │ altSalesTotal               │ DOUBLE  │ false   │            │ false   │
│     4 │ altShippingCost             │ DOUBLE  │ false   │            │ false   │
│     5 │ authCode                    │ VARCHAR │ false   │            │ false   │
│     6 │ balance                     │ DOUBLE  │ false   │            │ false   │
│     7 │ billAddressList_id          │ BIGINT  │ false   │            │ false   │
│     8 │ billingAddress_id           │ BIGINT  │ false   │            │ false   │
│     9 │ billingSchedule_id          │ BIGINT  │ false   │            │ false   │
│    10 │ canHaveStackable            │ BOOLEAN │ false   │            │ false   │
│    11 │ ccApproved                  │ BOOLEAN │ false   │            │ false   │
│    12 │ ccAvsStreetMatch            │ VARCHAR │ false   │            │ false   │
│    13 │ ccAvsZipMatch               │ VARCHAR │ false   │            │ false   │
│    14 │ ccExpireDate                │ VARCHAR │ false   │            │ false   │
│    15 │ ccName                      │ VARCHAR │ false   │            │ false   │
│    16 │ ccNumber                    │ VARCHAR │ false   │            │ false   │
│    17 │ ccSecurityCode              │ VARCHAR │ false   │            │ false   │
│    18 │ ccStreet                    │ VARCHAR │ false   │            │ false   │
│    19 │ ccZipCode                   │ VARCHAR │ false   │            │ false   │
│    20 │ checkNumber                 │ VARCHAR │ false   │            │ false   │
│    21 │ class_id                    │ BIGINT  │ false   │            │ false   │
│    22 │ contribPct                  │ VARCHAR │ false   │            │ false   │
│    23 │ createdDate                 │ VARCHAR │ false   │            │ false   │
│    24 │ createdFrom_id              │ BIGINT  │ false   │            │ false   │
│    25 │ creditCard_id               │ BIGINT  │ false   │            │ false   │
│    26 │ creditCardProcessor_id      │ BIGINT  │ false   │            │ false   │
│    27 │ currency_id                 │ BIGINT  │ false   │            │ false   │
│    28 │ currencyName                │ VARCHAR │ false   │            │ false   │
│    29 │ customFieldList_id          │ BIGINT  │ false   │            │ false   │
│    30 │ customForm_id               │ BIGINT  │ false   │            │ false   │
│    31 │ debitCardIssueNo            │ VARCHAR │ false   │            │ false   │
│    32 │ deferredRevenue             │ DOUBLE  │ false   │            │ false   │
│    33 │ department_id               │ BIGINT  │ false   │            │ false   │
│    34 │ discountItem_id             │ BIGINT  │ false   │            │ false   │
│    35 │ discountRate                │ VARCHAR │ false   │            │ false   │
│    36 │ location_id                 │ BIGINT  │ false   │            │ false   │
│    37 │ item_id                     │ BIGINT  │ false   │            │ false   │
├───────┴─────────────────────────────┴─────────┴─────────┴────────────┴─────────┤
│ 38 rows                                                              6 columns │
└────────────────────────────────────────────────────────────────────────────────┘


```

WORKORDER


```
┌───────┬────────────────────────────┬─────────┬─────────┬────────────┬─────────┐
│  cid  │            name            │  type   │ notnull │ dflt_value │   pk    │
│ int32 │          varchar           │ varchar │ boolean │  varchar   │ boolean │
├───────┼────────────────────────────┼─────────┼─────────┼────────────┼─────────┤
│     0 │ workOrderId                │ BIGINT  │ false   │            │ false   │
│     1 │ account_id                 │ BIGINT  │ false   │            │ false   │
│     2 │ actualProductionEndDate    │ VARCHAR │ false   │            │ false   │
│     3 │ actualProductionStartDate  │ VARCHAR │ false   │            │ false   │
│     4 │ assemblyItem_id            │ BIGINT  │ false   │            │ false   │
│     5 │ autoCalculateLag           │ BIGINT  │ false   │            │ false   │
│     6 │ billOfMaterials_id         │ BIGINT  │ false   │            │ false   │
│     7 │ billOfMaterialsRevision_id │ BIGINT  │ false   │            │ false   │
│     8 │ buildable                  │ BIGINT  │ false   │            │ false   │
│     9 │ built                      │ BIGINT  │ false   │            │ false   │
│    10 │ class_id                   │ DOUBLE  │ false   │            │ false   │
│    11 │ createdDate                │ VARCHAR │ false   │            │ false   │
│    12 │ createdFrom_id             │ BIGINT  │ false   │            │ false   │
│    13 │ currency_id                │ BIGINT  │ false   │            │ false   │
│    14 │ currencyName               │ VARCHAR │ false   │            │ false   │
│    15 │ customFieldList_id         │ BIGINT  │ false   │            │ false   │
│    16 │ customForm_id              │ BIGINT  │ false   │            │ false   │
│    17 │ department_id              │ BIGINT  │ false   │            │ false   │
│    18 │ dueDate                    │ VARCHAR │ false   │            │ false   │
│    19 │ email                      │ VARCHAR │ false   │            │ false   │
│    20 │ employee_id                │ BIGINT  │ false   │            │ false   │
│    21 │ entity_id                  │ BIGINT  │ false   │            │ false   │
│    22 │ workOrderitemListId        │ BIGINT  │ false   │            │ false   │
│    23 │ job_id                     │ BIGINT  │ false   │            │ false   │
│    24 │ lastModifiedDate           │ VARCHAR │ false   │            │ false   │
│    25 │ location_id                │ BIGINT  │ false   │            │ false   │
│    26 │ manufacturingRouting_id    │ BIGINT  │ false   │            │ false   │
│    27 │ memo                       │ VARCHAR │ false   │            │ false   │
│    28 │ options_id                 │ BIGINT  │ false   │            │ false   │
│    29 │ orderStatus                │ VARCHAR │ false   │            │ false   │
│    30 │ partnersList_id            │ BIGINT  │ false   │            │ false   │
│    31 │ quantity                   │ BIGINT  │ false   │            │ false   │
│    32 │ requestedDate              │ VARCHAR │ false   │            │ false   │
│    33 │ revision_id                │ BIGINT  │ false   │            │ false   │
│    34 │ salesTeamList_id           │ BIGINT  │ false   │            │ false   │
│    35 │ schedulingMethod           │ VARCHAR │ false   │            │ false   │
│    36 │ sourceTransactionId        │ VARCHAR │ false   │            │ false   │
│    37 │ sourceTransactionLine      │ BIGINT  │ false   │            │ false   │
│    38 │ specialOrder               │ BOOLEAN │ false   │            │ false   │
│    39 │ startDate                  │ VARCHAR │ false   │            │ false   │
│    40 │ status                     │ VARCHAR │ false   │            │ false   │
│    41 │ subsidiary_id              │ BIGINT  │ false   │            │ false   │
├───────┴────────────────────────────┴─────────┴─────────┴────────────┴─────────┤
│ 42 rows                                                             6 columns │
└───────────────────────────────────────────────────────────────────────────────┘

```

#### Bronze

Direct raw from 🦆DB

#### Silver


StagedAccounts


```
┌─────┬────────────────┬─────────┬─────────┬────────────┬───────┐
│ cid ┆ name           ┆ type    ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---            ┆ ---     ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str            ┆ str     ┆ bool    ┆ str        ┆ bool  │
╞═════╪════════════════╪═════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Account ID     ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 1   ┆ Account Name   ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 2   ┆ Account Number ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 3   ┆ Account Type   ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 4   ┆ Currency ID    ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 5   ┆ Department ID  ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
│ 6   ┆ Description    ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 7   ┆ Eliminate?     ┆ BOOLEAN ┆ false   ┆ null       ┆ false │
│ 8   ┆ Exchange Rate  ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 9   ┆ Inventory?     ┆ BOOLEAN ┆ false   ┆ null       ┆ false │
│ 10  ┆ Inactive?      ┆ BOOLEAN ┆ false   ┆ null       ┆ false │
│ 11  ┆ Legal Name     ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 12  ┆ Location ID    ┆ BIGINT  ┆ false   ┆ null       ┆ false │
└─────┴────────────────┴─────────┴─────────┴────────────┴───────┘

```

StagedInventoryItemLocations


```
┌─────┬────────────────────────────┬─────────┬─────────┬────────────┬───────┐
│ cid ┆ name                       ┆ type    ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                        ┆ ---     ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                        ┆ str     ┆ bool    ┆ str        ┆ bool  │
╞═════╪════════════════════════════╪═════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Inventory Item Location ID ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 1   ┆ Display Name               ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 2   ┆ Location                   ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 3   ┆ Quality Available          ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
│ 4   ┆ Quantity Backordered       ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
│ 5   ┆ Quantity Committed         ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
│ 6   ┆ Quantity On Hand           ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
│ 7   ┆ Quantity On Order          ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
└─────┴────────────────────────────┴─────────┴─────────┴────────────┴───────┘

```


StagedInventoryItems


```

┌─────┬─────────────────────────────┬─────────┬─────────┬────────────┬───────┐
│ cid ┆ name                        ┆ type    ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                         ┆ ---     ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                         ┆ str     ┆ bool    ┆ str        ┆ bool  │
╞═════╪═════════════════════════════╪═════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Inventory Item ID           ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 1   ┆ Item ID                     ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 2   ┆ Display Name                ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 3   ┆ Account Book Detail List ID ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 4   ┆ Asset Account ID            ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 5   ┆ bin Number List ID          ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 6   ┆ Description                 ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 7   ┆ Cost                        ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
└─────┴─────────────────────────────┴─────────┴─────────┴────────────┴───────┘


```

StagedLocation


```
┌─────┬───────────────────────────────────┬───────────┬─────────┬────────────┬───────┐
│ cid ┆ name                              ┆ type      ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                               ┆ ---       ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                               ┆ str       ┆ bool    ┆ str        ┆ bool  │
╞═════╪═══════════════════════════════════╪═══════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Location ID                       ┆ BIGINT    ┆ false   ┆ null       ┆ false │
│ 1   ┆ Store Pickup Allowed?             ┆ BOOLEAN   ┆ false   ┆ null       ┆ false │
│ 2   ┆ Buffer Stock Setting              ┆ DOUBLE    ┆ false   ┆ null       ┆ false │
│ 3   ┆ Inactive?                         ┆ BOOLEAN   ┆ false   ┆ null       ┆ false │
│ 4   ┆ Latitude                          ┆ DOUBLE    ┆ false   ┆ null       ┆ false │
│ 5   ┆ Longitude                         ┆ DOUBLE    ┆ false   ┆ null       ┆ false │
│ 6   ┆ Main Address ID                   ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 7   ┆ Inventory Available for Purchase? ┆ BOOLEAN   ┆ false   ┆ null       ┆ false │
│ 8   ┆ Location Name                     ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 9   ┆ Next Pickup Cut Off Time          ┆ TIMESTAMP ┆ false   ┆ null       ┆ false │
│ 10  ┆ Time Zone                         ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 11  ┆ Total Shipping Capacity           ┆ DOUBLE    ┆ false   ┆ null       ┆ false │
└─────┴───────────────────────────────────┴───────────┴─────────┴────────────┴───────┘


```

StagedPurchaseOrder


```
┌─────┬─────────────────────────┬─────────┬─────────┬────────────┬───────┐
│ cid ┆ name                    ┆ type    ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                     ┆ ---     ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                     ┆ str     ┆ bool    ┆ str        ┆ bool  │
╞═════╪═════════════════════════╪═════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Purchase Order ID       ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 1   ┆ Account ID              ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 2   ┆ Approval Status         ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 3   ┆ Billing Address List ID ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 4   ┆ Billing Address         ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 5   ┆ Created Date            ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 6   ┆ Created From ID         ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 7   ┆ Currency ID             ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 8   ┆ Currency Name           ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 9   ┆ Department ID           ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 10  ┆ Due Date                ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 11  ┆ email                   ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 12  ┆ Employee ID             ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 13  ┆ Exchange Rate           ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 14  ┆ Location ID             ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 15  ┆ Memo                    ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 16  ┆ Message                 ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 17  ┆ Order Status            ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 18  ┆ Order Reference Number  ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 19  ┆ Purchase Contract ID    ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 20  ┆ Shipping Address        ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 21  ┆ Ship Date               ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 22  ┆ Ship Method             ┆ VARCHAR ┆ false   ┆ null       ┆ false │
└─────┴─────────────────────────┴─────────┴─────────┴────────────┴───────┘

```

StagedSalesOrder


```
┌─────┬──────────────────────────────────────────────────┬─────────┬─────────┬────────────┬───────┐
│ cid ┆ name                                             ┆ type    ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                                              ┆ ---     ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                                              ┆ str     ┆ bool    ┆ str        ┆ bool  │
╞═════╪══════════════════════════════════════════════════╪═════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Actual Ship Date                                 ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 1   ┆ Balance Owed                                     ┆ DOUBLE  ┆ false   ┆ null       ┆ false │
│ 2   ┆ Billing Address ID                               ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 3   ┆ Are Promotions Stackable?                        ┆ BOOLEAN ┆ false   ┆ null       ┆ false │
│ 4   ┆ Credit Card Approved?                            ┆ BOOLEAN ┆ false   ┆ null       ┆ false │
│ 5   ┆ Match In Address Verification System for Street? ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 6   ┆ Match In Address Verification System for Zip?    ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 7   ┆ Credit Card Expire Date                          ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 8   ┆ Name On Credit Card                              ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 9   ┆ Credit Card Number                               ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 10  ┆ Credit Card Security Code                        ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 11  ┆ Credit Card Street                               ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 12  ┆ Credit Card Zip Code                             ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 13  ┆ Check Number                                     ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 14  ┆ Created Date                                     ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 15  ┆ Created From ID                                  ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 16  ┆ Currency ID                                      ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 17  ┆ Currency Names                                   ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 18  ┆ Department ID                                    ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 19  ┆ Discount Rate                                    ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 20  ┆ Location ID                                      ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 21  ┆ Item ID                                          ┆ BIGINT  ┆ false   ┆ null       ┆ false │
└─────┴──────────────────────────────────────────────────┴─────────┴─────────┴────────────┴───────┘


```

StagedWorkOrder


```
┌─────┬───────────────────────────────┬─────────┬─────────┬────────────┬───────┐
│ cid ┆ name                          ┆ type    ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                           ┆ ---     ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                           ┆ str     ┆ bool    ┆ str        ┆ bool  │
╞═════╪═══════════════════════════════╪═════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Work Order ID                 ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 1   ┆ Account ID                    ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 2   ┆ Actual Production End Date    ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 3   ┆ Actual Production Start Date  ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 4   ┆ Assembly Item ID              ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 5   ┆ Bill of Materials ID          ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 6   ┆ Bill of Materials Revision ID ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 7   ┆ Number of Units Buildable     ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 8   ┆ Number of Units Built         ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 9   ┆ Created Date                  ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 10  ┆ Created From                  ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 11  ┆ Currency ID                   ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 12  ┆ Currency Name                 ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 13  ┆ Department ID                 ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 14  ┆ Due Date                      ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 15  ┆ Email                         ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 16  ┆ Employee ID                   ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 17  ┆ Entity ID                     ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 18  ┆ Work Order Item List          ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 19  ┆ Job ID                        ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 20  ┆ Last Modified Date            ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 21  ┆ Location ID                   ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 22  ┆ Manufacturing Routing ID      ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 23  ┆ Memo                          ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 24  ┆ Order Status                  ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 25  ┆ Quantity                      ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 26  ┆ Requested Date                ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 27  ┆ Revision ID                   ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 28  ┆ Sales Team List ID            ┆ BIGINT  ┆ false   ┆ null       ┆ false │
│ 29  ┆ Scheduling Method             ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 30  ┆ Start Date                    ┆ VARCHAR ┆ false   ┆ null       ┆ false │
│ 31  ┆ Status                        ┆ VARCHAR ┆ false   ┆ null       ┆ false │
└─────┴───────────────────────────────┴─────────┴─────────┴────────────┴───────┘

```

### Audit

Same as Silver but with tables renamed as follows:

- StagedAccounts -> DimAccounts
- StagedInventoryItemLocations -> DimInventoryItemLocations
- StagedInventoryItems -> DimInventoryItems
- StagedLocation -> DimLocation
- StagedPurchaseOrder -> FactPurchaseOrder
- StagedSalesOrder -> FactSalesOrder
- StagedWorkOrder -> FactWorkOrder

Two additional tables for quality checks:


InvalidDataAuditLog


```
┌─────┬──────────────────────────┬───────────┬─────────┬────────────┬───────┐
│ cid ┆ name                     ┆ type      ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---                      ┆ ---       ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str                      ┆ str       ┆ bool    ┆ str        ┆ bool  │
╞═════╪══════════════════════════╪═══════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Table Name               ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 1   ┆ Audit Column             ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 2   ┆ SQL Constraint Predicate ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 3   ┆ Invalid Record Count     ┆ BIGINT    ┆ false   ┆ null       ┆ false │
│ 4   ┆ As Of Datetime           ┆ TIMESTAMP ┆ false   ┆ null       ┆ false │
└─────┴──────────────────────────┴───────────┴─────────┴────────────┴───────┘


```
NullCountAuditLog


```
┌─────┬────────────────┬───────────┬─────────┬────────────┬───────┐
│ cid ┆ name           ┆ type      ┆ notnull ┆ dflt_value ┆ pk    │
│ --- ┆ ---            ┆ ---       ┆ ---     ┆ ---        ┆ ---   │
│ i32 ┆ str            ┆ str       ┆ bool    ┆ str        ┆ bool  │
╞═════╪════════════════╪═══════════╪═════════╪════════════╪═══════╡
│ 0   ┆ Table Name     ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 1   ┆ Table Column   ┆ VARCHAR   ┆ false   ┆ null       ┆ false │
│ 2   ┆ Null Count     ┆ BIGINT    ┆ false   ┆ null       ┆ false │
│ 3   ┆ As Of Datetime ┆ TIMESTAMP ┆ false   ┆ null       ┆ false │
└─────┴────────────────┴───────────┴─────────┴────────────┴───────┘

```
### Gold

Same as Audit without the data quality check tables. 

### API  

```
endpoint:  uk_station


dictionary:
  key: date, type: <class 'str'>
    ,type: <class 'str'>
  key: departures, type: <class 'dict'>
    dictionary:
      key: all, type: <class 'list'>
        list:
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: aimed_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: aimed_pass_time, type: <class 'NoneType'>
                ,type: <class 'NoneType'>
              key: best_arrival_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: best_departure_estimate_mins, type: <class 'str'>
                ,type: <class 'str'>
              key: category, type: <class 'str'>
                ,type: <class 'str'>
              key: destination_name, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_arrival_time, type: <class 'str'>
                ,type: <class 'str'>
              key: expected_departure_time, type: <class 'str'>
                ,type: <class 'str'>
              key: mode, type: <class 'str'>
                ,type: <class 'str'>
              key: operator, type: <class 'str'>
                ,type: <class 'str'>
              key: operator_name, type: <class 'str'>
                ,type: <class 'str'>
              key: origin_name, type: <class 'str'>
                ,type: <class 'str'>
              key: platform, type: <class 'str'>
                ,type: <class 'str'>
              key: service, type: <class 'str'>
                ,type: <class 'str'>
              key: service_timetable, type: <class 'dict'>
                dictionary:
                  key: id, type: <class 'str'>
                    ,type: <class 'str'>
              key: source, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: train_uid, type: <class 'str'>
                ,type: <class 'str'>
  key: request_time, type: <class 'str'>
    ,type: <class 'str'>
  key: station_code, type: <class 'str'>
    ,type: <class 'str'>
  key: station_name, type: <class 'str'>
    ,type: <class 'str'>
  key: time_of_day, type: <class 'str'>
    ,type: <class 'str'>

endpoint:  uk_train


dictionary:
  key: category, type: <class 'str'>
    ,type: <class 'str'>
  key: destination_name, type: <class 'str'>
    ,type: <class 'str'>
  key: headcode, type: <class 'str'>
    ,type: <class 'str'>
  key: mode, type: <class 'str'>
    ,type: <class 'str'>
  key: operator, type: <class 'str'>
    ,type: <class 'str'>
  key: operator_name, type: <class 'str'>
    ,type: <class 'str'>
  key: origin_name, type: <class 'str'>
    ,type: <class 'str'>
  key: request_time, type: <class 'str'>
    ,type: <class 'str'>
  key: service, type: <class 'str'>
    ,type: <class 'str'>
  key: stop_of_interest, type: <class 'str'>
    ,type: <class 'str'>
  key: stops, type: <class 'list'>
    list:
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: aimed_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: aimed_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_arrival_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_departure_time, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_date, type: <class 'str'>
            ,type: <class 'str'>
          key: expected_pass_time, type: <class 'str'>
            ,type: <class 'str'>
          key: platform, type: <class 'str'>
            ,type: <class 'str'>
          key: station_code, type: <class 'str'>
            ,type: <class 'str'>
          key: station_name, type: <class 'str'>
            ,type: <class 'str'>
          key: status, type: <class 'str'>
            ,type: <class 'str'>
          key: stop_type, type: <class 'str'>
            ,type: <class 'str'>
          key: tiploc_code, type: <class 'str'>
            ,type: <class 'str'>
  key: toc, type: <class 'dict'>
    dictionary:
      key: atoc_code, type: <class 'str'>
        ,type: <class 'str'>
  key: train_status, type: <class 'str'>
    ,type: <class 'str'>
  key: train_uid, type: <class 'str'>
    ,type: <class 'str'>

endpoint:  china_station


dictionary:
  key: StationNameCN, type: <class 'str'>
    ,type: <class 'str'>
  key: StationNameEN, type: <class 'str'>
    ,type: <class 'str'>
  key: StatusCode, type: <class 'str'>
    ,type: <class 'str'>
  key: Trains, type: <class 'list'>
    list:
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArrStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: ArrTime, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationCN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepStationEN, type: <class 'str'>
            ,type: <class 'str'>
          key: DepTime, type: <class 'str'>
            ,type: <class 'str'>
          key: Duration, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>

endpoint:  china_train


dictionary:
  key: StatusCode, type: <class 'str'>
    ,type: <class 'str'>
  key: TimeTable, type: <class 'list'>
    list:
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>
      item type: <class 'dict'>
        dictionary:
          key: ArriveTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StartTime, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameCN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNameEN, type: <class 'str'>
            ,type: <class 'str'>
          key: StationNo, type: <class 'int'>
            ,type: <class 'int'>
          key: StopTime, type: <class 'str'>
            ,type: <class 'str'>
          key: TrainNo, type: <class 'str'>
            ,type: <class 'str'>

endpoint:  us_station


dictionary:
  key: QSF, type: <class 'dict'>
    dictionary:
      key: address1, type: <class 'str'>
        ,type: <class 'str'>
      key: address2, type: <class 'str'>
        ,type: <class 'str'>
      key: city, type: <class 'str'>
        ,type: <class 'str'>
      key: code, type: <class 'str'>
        ,type: <class 'str'>
      key: lat, type: <class 'str'>
        ,type: <class 'str'>
      key: lon, type: <class 'str'>
        ,type: <class 'str'>
      key: name, type: <class 'str'>
        ,type: <class 'str'>
      key: state, type: <class 'str'>
        ,type: <class 'str'>
      key: trains, type: <class 'list'>
        list:
          item type: <class 'dict'>
            dictionary:
              key: ArrivalTime, type: <class 'str'>
                ,type: <class 'str'>
              key: DepartureTime, type: <class 'str'>
                ,type: <class 'str'>
              key: Stops, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
              key: TrainNo, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: ArrivalTime, type: <class 'str'>
                ,type: <class 'str'>
              key: DepartureTime, type: <class 'str'>
                ,type: <class 'str'>
              key: Stops, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
              key: TrainNo, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: ArrivalTime, type: <class 'str'>
                ,type: <class 'str'>
              key: DepartureTime, type: <class 'str'>
                ,type: <class 'str'>
              key: Stops, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
              key: TrainNo, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: ArrivalTime, type: <class 'str'>
                ,type: <class 'str'>
              key: DepartureTime, type: <class 'str'>
                ,type: <class 'str'>
              key: Stops, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
                  item type: <class 'dict'>
                    dictionary:
                      key: ArrivalTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: DepartureTime, type: <class 'str'>
                        ,type: <class 'str'>
                      key: StopStation, type: <class 'str'>
                        ,type: <class 'str'>
              key: TrainNo, type: <class 'str'>
                ,type: <class 'str'>
      key: tz, type: <class 'str'>
        ,type: <class 'str'>
      key: zip, type: <class 'str'>
        ,type: <class 'str'>

endpoint:  us_train


dictionary:
  key: 1, type: <class 'dict'>
    dictionary:
      key: lat, type: <class 'str'>
        ,type: <class 'str'>
      key: lon, type: <class 'str'>
        ,type: <class 'str'>
      key: routeName, type: <class 'str'>
        ,type: <class 'str'>
      key: stations, type: <class 'list'>
        list:
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: arr, type: <class 'str'>
                ,type: <class 'str'>
              key: arrCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: bus, type: <class 'bool'>
                ,type: <class 'bool'>
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: dep, type: <class 'str'>
                ,type: <class 'str'>
              key: depCmnt, type: <class 'str'>
                ,type: <class 'str'>
              key: name, type: <class 'str'>
                ,type: <class 'str'>
              key: schArr, type: <class 'str'>
                ,type: <class 'str'>
              key: schDep, type: <class 'str'>
                ,type: <class 'str'>
              key: status, type: <class 'str'>
                ,type: <class 'str'>
              key: tz, type: <class 'str'>
                ,type: <class 'str'>
      key: trainID, type: <class 'str'>
        ,type: <class 'str'>
      key: trainNum, type: <class 'str'>
        ,type: <class 'str'>
      key: trainTimely, type: <class 'str'>
        ,type: <class 'str'>

endpoint:  japan_station


dictionary:
  key: ResultSet, type: <class 'dict'>
    dictionary:
      key: TimeTable, type: <class 'dict'>
        dictionary:
          key: HourTable, type: <class 'list'>
            list:
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: Hour, type: <class 'int'>
                    ,type: <class 'int'>
                  key: MinuteTable, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                      item type: <class 'dict'>
                        dictionary:
                          key: Minute, type: <class 'int'>
                            ,type: <class 'int'>
                          key: Stop, type: <class 'dict'>
                            dictionary:
                              key: destinationCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: kindCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lineCode, type: <class 'str'>
                                ,type: <class 'str'>
                              key: nameCode, type: <class 'int'>
                                ,type: <class 'int'>
                              key: platformNo, type: <class 'int'>
                                ,type: <class 'int'>
                  key: TimeReliability, type: <class 'str'>
                    ,type: <class 'str'>
          key: Line, type: <class 'dict'>
            dictionary:
              key: Color, type: <class 'str'>
                ,type: <class 'str'>
              key: Direction, type: <class 'str'>
                ,type: <class 'str'>
              key: Name, type: <class 'str'>
                ,type: <class 'str'>
              key: Source, type: <class 'str'>
                ,type: <class 'str'>
          key: LineDestination, type: <class 'list'>
            list:
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
              item type: <class 'dict'>
                dictionary:
                  key: code, type: <class 'int'>
                    ,type: <class 'int'>
                  key: text, type: <class 'str'>
                    ,type: <class 'str'>
          key: LineKind, type: <class 'dict'>
            dictionary:
              key: code, type: <class 'int'>
                ,type: <class 'int'>
              key: text, type: <class 'str'>
                ,type: <class 'str'>
          key: LineName, type: <class 'dict'>
            dictionary:
              key: code, type: <class 'str'>
                ,type: <class 'str'>
              key: text, type: <class 'str'>
                ,type: <class 'str'>
          key: Station, type: <class 'dict'>
            dictionary:
              key: Name, type: <class 'str'>
                ,type: <class 'str'>
          key: code, type: <class 'str'>
            ,type: <class 'str'>
          key: dateGroup, type: <class 'str'>
            ,type: <class 'str'>
          key: trainCount, type: <class 'int'>
            ,type: <class 'int'>
      key: apiVersion, type: <class 'str'>
        ,type: <class 'str'>
      key: engineVersion, type: <class 'str'>
        ,type: <class 'str'>

endpoint:  japan_train


dictionary:
  key: resultset, type: <class 'dict'>
    dictionary:
      key: apiversion, type: <class 'str'>
        ,type: <class 'str'>
      key: course, type: <class 'list'>
        list:
          item type: <class 'dict'>
            dictionary:
              key: datatype, type: <class 'str'>
                ,type: <class 'str'>
              key: price, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: kind, type: <class 'str'>
                        ,type: <class 'str'>
                      key: oneway, type: <class 'str'>
                        ,type: <class 'str'>
                      key: round, type: <class 'str'>
                        ,type: <class 'str'>
              key: route, type: <class 'dict'>
                dictionary:
                  key: distance, type: <class 'str'>
                    ,type: <class 'str'>
                  key: exhaustco2, type: <class 'str'>
                    ,type: <class 'str'>
                  key: exhaustco2atpassengercar, type: <class 'str'>
                    ,type: <class 'str'>
                  key: line, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                  key: point, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: geopoint, type: <class 'dict'>
                            dictionary:
                              key: gcs, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lati, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lati_d, type: <class 'str'>
                                ,type: <class 'str'>
                              key: longi, type: <class 'str'>
                                ,type: <class 'str'>
                              key: longi_d, type: <class 'str'>
                                ,type: <class 'str'>
                          key: prefecture, type: <class 'dict'>
                            dictionary:
                              key: code, type: <class 'str'>
                                ,type: <class 'str'>
                              key: name, type: <class 'str'>
                                ,type: <class 'str'>
                          key: station, type: <class 'dict'>
                            dictionary:
                              key: code, type: <class 'str'>
                                ,type: <class 'str'>
                              key: name, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                              key: yomi, type: <class 'str'>
                                ,type: <class 'str'>
                  key: timeonboard, type: <class 'str'>
                    ,type: <class 'str'>
                  key: timeother, type: <class 'str'>
                    ,type: <class 'str'>
                  key: timewalk, type: <class 'str'>
                    ,type: <class 'str'>
                  key: transfercount, type: <class 'str'>
                    ,type: <class 'str'>
              key: searchtype, type: <class 'str'>
                ,type: <class 'str'>
              key: serializedata, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: datatype, type: <class 'str'>
                ,type: <class 'str'>
              key: price, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: kind, type: <class 'str'>
                        ,type: <class 'str'>
                      key: oneway, type: <class 'str'>
                        ,type: <class 'str'>
                      key: round, type: <class 'str'>
                        ,type: <class 'str'>
              key: route, type: <class 'dict'>
                dictionary:
                  key: distance, type: <class 'str'>
                    ,type: <class 'str'>
                  key: exhaustco2, type: <class 'str'>
                    ,type: <class 'str'>
                  key: exhaustco2atpassengercar, type: <class 'str'>
                    ,type: <class 'str'>
                  key: line, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                  key: point, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: geopoint, type: <class 'dict'>
                            dictionary:
                              key: gcs, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lati, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lati_d, type: <class 'str'>
                                ,type: <class 'str'>
                              key: longi, type: <class 'str'>
                                ,type: <class 'str'>
                              key: longi_d, type: <class 'str'>
                                ,type: <class 'str'>
                          key: prefecture, type: <class 'dict'>
                            dictionary:
                              key: code, type: <class 'str'>
                                ,type: <class 'str'>
                              key: name, type: <class 'str'>
                                ,type: <class 'str'>
                          key: station, type: <class 'dict'>
                            dictionary:
                              key: code, type: <class 'str'>
                                ,type: <class 'str'>
                              key: name, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                              key: yomi, type: <class 'str'>
                                ,type: <class 'str'>
                  key: timeonboard, type: <class 'str'>
                    ,type: <class 'str'>
                  key: timeother, type: <class 'str'>
                    ,type: <class 'str'>
                  key: timewalk, type: <class 'str'>
                    ,type: <class 'str'>
                  key: transfercount, type: <class 'str'>
                    ,type: <class 'str'>
              key: searchtype, type: <class 'str'>
                ,type: <class 'str'>
              key: serializedata, type: <class 'str'>
                ,type: <class 'str'>
          item type: <class 'dict'>
            dictionary:
              key: datatype, type: <class 'str'>
                ,type: <class 'str'>
              key: price, type: <class 'list'>
                list:
                  item type: <class 'dict'>
                    dictionary:
                      key: kind, type: <class 'str'>
                        ,type: <class 'str'>
                      key: oneway, type: <class 'str'>
                        ,type: <class 'str'>
                      key: round, type: <class 'str'>
                        ,type: <class 'str'>
              key: route, type: <class 'dict'>
                dictionary:
                  key: distance, type: <class 'str'>
                    ,type: <class 'str'>
                  key: exhaustco2, type: <class 'str'>
                    ,type: <class 'str'>
                  key: exhaustco2atpassengercar, type: <class 'str'>
                    ,type: <class 'str'>
                  key: line, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: arrivalstate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: color, type: <class 'str'>
                            ,type: <class 'str'>
                          key: departurestate, type: <class 'dict'>
                            dictionary:
                              key: datetime, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                          key: distance, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2, type: <class 'str'>
                            ,type: <class 'str'>
                          key: exhaustco2atpassengercar, type: <class 'str'>
                            ,type: <class 'str'>
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                          key: stopstationcount, type: <class 'str'>
                            ,type: <class 'str'>
                          key: timeonboard, type: <class 'str'>
                            ,type: <class 'str'>
                          key: type, type: <class 'str'>
                            ,type: <class 'str'>
                  key: point, type: <class 'list'>
                    list:
                      item type: <class 'dict'>
                        dictionary:
                          key: name, type: <class 'str'>
                            ,type: <class 'str'>
                      item type: <class 'dict'>
                        dictionary:
                          key: geopoint, type: <class 'dict'>
                            dictionary:
                              key: gcs, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lati, type: <class 'str'>
                                ,type: <class 'str'>
                              key: lati_d, type: <class 'str'>
                                ,type: <class 'str'>
                              key: longi, type: <class 'str'>
                                ,type: <class 'str'>
                              key: longi_d, type: <class 'str'>
                                ,type: <class 'str'>
                          key: prefecture, type: <class 'dict'>
                            dictionary:
                              key: code, type: <class 'str'>
                                ,type: <class 'str'>
                              key: name, type: <class 'str'>
                                ,type: <class 'str'>
                          key: station, type: <class 'dict'>
                            dictionary:
                              key: code, type: <class 'str'>
                                ,type: <class 'str'>
                              key: name, type: <class 'str'>
                                ,type: <class 'str'>
                              key: type, type: <class 'str'>
                                ,type: <class 'str'>
                              key: yomi, type: <class 'str'>
                                ,type: <class 'str'>
                  key: timeonboard, type: <class 'str'>
                    ,type: <class 'str'>
                  key: timeother, type: <class 'str'>
                    ,type: <class 'str'>
                  key: timewalk, type: <class 'str'>
                    ,type: <class 'str'>
                  key: transfercount, type: <class 'str'>
                    ,type: <class 'str'>
              key: searchtype, type: <class 'str'>
                ,type: <class 'str'>
              key: serializedata, type: <class 'str'>
                ,type: <class 'str'>
      key: engineversion, type: <class 'str'>
        ,type: <class 'str'>

```

### The Size

For phase 0 no rows are filtered out so all tables have equivalent row counts across the layers. 

The following is from Silver. 


```
StagedAccounts


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 150      │
└──────────┘



StagedInventoryItemLocations


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 350      │
└──────────┘



StagedInventoryItems


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 20       │
└──────────┘



StagedLocation


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 25       │
└──────────┘



StagedPurchaseOrder


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 2500000  │
└──────────┘



StagedSalesOrder


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 2500000  │
└──────────┘



StagedWorkOrder


┌──────────┐
│ count(1) │
│ ---      │
│ i64      │
╞══════════╡
│ 2500000  │
└──────────┘

```

Estimated size of those tables in Polars in megabytes:

```


StagedAccounts


0.043



StagedInventoryItemLocations


0.026



StagedInventoryItems


0.007



StagedLocation


0.003



StagedPurchaseOrder


1576.849



StagedSalesOrder


689.056



StagedWorkOrder


1257.464


```



### The Model

Straight tables with dim and fact names prepended. No relationships defined for phase 0. 

Model wise, absolute 💩. 

## The Code

"Pipelines" are python scripts which execute a series of arbitarary functions defined in a YAML config. 

Code stored in `src` and further divided to into layer specific directories as well as `common`, where all the common functions run are stored. 

See `src/common/common_data_loading.py`

In `common` also are example configs and example `_etl.py` scripts.

See `src/common/common_data_loading_config.yaml`

See `src/common/common_etl.py`

Execution control happens in the common functions .py file. 

Functions are divided into several categories:

- ETL

- ETL Execution

- Data Quality

- Misc

Example Function:

```
def read_from_local_duck_db(db_path, query):
    db_path = os.path.join(os.getcwd(), db_path)
    conn = duckdb.connect(db_path)
    return conn.execute(query).pl()
```

Example Config:

```
delta_lake_path: &delta_lake_path "output_data_lake" 
db_path: &db_path ERPSourceMockup.db
# Multiline anchor of executable python code run before a called out function executes. Can be overridden in the actual definition. 
pre_execution_python_code: &pre_execution_python_code | 
  print(results.head(1))
  function_to_execute_arguments["df"] = results
  print(function_to_execute_arguments.keys())
# Array of etl jobs that will be run, each job has an arbitrary number of steps. Valid and invalid examples included. 
etl_jobs: 
  - 
    - step_description: Reading MYTABLE duckdb table
      function_to_execute: read_from_local_duck_db
      function_to_execute_arguments:
        db_path: *db_path 
        query: "SELECT * FROM MYTABLE"
    - step_description: Writing MYTABLE to local delta
      function_to_execute: write_to_local_delta
      function_to_execute_arguments:
        delta_lake_path: *delta_lake_path 
        table_name: MYTABLE
        layer: bronze
      pre_execution_python_code: *pre_execution_python_code
  -
    - step_description: Your mom is an invalid job example, but does deserve cookies 😜.
      function_to_execute: your mom
      function_to_execute_arguments:
        is_awesome: True
        deserves_cookies: True

```



### The ETL

Bronze

Output of [eza](https://github.com/eza-community/eza) in `src/bronze`

__init__.py
bronze_data_loading_config.yaml
bronze_etl.py

Silver

Output of [eza](https://github.com/eza-community/eza) in `src/silver`

__init__.py
silver_data_loading_config.yaml
silver_etl.py
sql_files

Audit

Output of [eza](https://github.com/eza-community/eza) in `src/audit`

__init__.py
audit_data_loading_config.yaml
audit_etl.py

Gold

Output of [eza](https://github.com/eza-community/eza) in `src/gold`

__init__.py
gold_data_loading_config.yaml
gold_etl.py

#### The DAGs

🦆DB -> Bronze

Bronze -> Silver

Silver -> Audit

Audit -> Gold

-> = _etl.py file for that specific layer

### The Queries

SQL Queries are stored in the sql_files dir of the corresponding layer. 

For Phase 0 this is only silver. 

For Phase 0 the queries are simply selecting a subset of the columns and renaming them. 

See `src/silver/sql_files` for the actual queries

### The Runs

Bronze Load

![BronzeLoad](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/d837bcf8-db66-4ce7-911b-391a36f07748)

Silver Load

![Silver Load](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/fd5b884e-b77f-49a4-9013-83170bd29a11)

Audit Load

Tables unique to Audit shown only

![Audit Load](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/0a497282-c269-44aa-bd33-655e0b421b6f)

Gold Load

![Gold Load](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/62ec6a6b-ad7b-4e57-9cb3-3ecc1c45eab5)

![Gold Load 2](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/88351cee-58c9-4934-a740-f76ef598883c)

API Saved on Disk

```

api_responses
└── Japan_Train
   ├── 2024_01_23_18_11_1706055071.json
   ├── 2024_01_23_18_22_1706055768.json
   ├── 2024_01_23_18_23_1706055781.json
   ├── 2024_01_23_18_23_1706055793.json
   └── 2024_01_23_18_30_1706056241.json
```


## The Tests

All functions covered by pytest. Further refinements will happen after Phase 0.

See `tests/`

<img width="1310" alt="image" src="https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/e4be5aa3-cfdd-4c3c-bb25-269c505d9881">


## The Quality Checks

Invalid Data based upon SQL Predicates

![Invalid Data](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/b4c6990c-b9e9-4f22-a5e3-27924ff6467c)

Null counts

![Null counts](https://github.com/ryanbrownnetworking777/ryanbrowncapstone/assets/39069157/8c85071d-e503-44c7-93e5-c7fdf87860ce)


Both performed with functions defined as such leveraging SQL run by 🦆DB.

See common function definition .py file for details.

## The "Front End"

See Quality checks. Jupyter Lab Notebooks all the way for Phase 0. 

💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀

## The Expansion

Assuming the constraint of "No Cloud" and "Low/No Budget", the solution could be deployed/expanded as follows:

- Repurpose older | procure dedicated machine (This is how I stood up the data mart at the envelope firm)
- Load framework
- Connect to network drive
- Schedule CRON jobs for the layers
- Connect to Front Ends
    - Excel: Microsoft and those associated with them spin a web of lies, claiming [here](https://blog.fabric.microsoft.com/en-us/blog/read-data-from-delta-lake-tables-with-the-deltalake-table-m-function/) and [here](https://blog.gbrueckl.at/2021/01/reading-delta-lake-tables-natively-in-powerbi/) that Delta is readable by Excel (assuming Power Query compatibility). I have yet to get that to work. 
    - Your BI tool here
    - Python | Whatever to consume Delta
- 🤑 or 😭 or both 

### Local Deployment Contours

- Batch size increased 100x
    -  Unplanned increase: 🦆DB would either take longer to process, or crash in the case of sudden increase (100x sudden increase in data volume would be *quite* discussion worthy) 
    - Planned increase: Split up the steps to process different sections of the raw data on different times according to a partition plan agreed upon.  
- If source.isStreaming() == True
    - The API is assumed to be "streaming" in the sense of lower latency pulls. 
    - Create a separate job running at lower latency for microbatch pulls
    - Create a separate listener to the Kafka topic/whatever, write with Flink to local Delta. 

- Scheduled Dashboard | Report | Email

    - CRON job for the specific report at a certain point, several hours before, including sending the email if necessary.  
    - CRON job running a script that checks the freshness of the data after loading, and/or the logs to check if the email was sent, if not schedule a temporary job to re-run. 
    - Review the temporary job if run, and send loud failure to the poor unfortunate soul defined as the owner for this job. 

- Exposing to other Data folks

    - Internal: if the data lake is on a network drive, and they already have access to the network drive, then they already have access. Just give them the path. 
    - External: Give VPN access to the internal network, then expose the files. A much bigger use case lol.  



## The Alternatives

This easily could be a standard Spark/Databricks/Fabric/{Insert managed spark here} deployment. 

Technically speaking, any other compute engine is theoretically plug-and-payable in the framework, provided Python bindings are available. Install/Import the libraries. Write the functions. Modify/Write the configs. Enjoy. 
The same goes for storage, plug in your s3/ADLS/whatever URL/Is into functions and go. 

My original stack idea:

- Apache Beam
- Apache Hudi
- Local LLMS for data generation

Why not? Newer frameworks to me that would have required more time to learn and implement than I had for phase 0. Simple as that. Would be excited to come back to that stack however.  

Local LLMs also require significant restraining to generate within a set of parameters, so it was simpler to use Faker. 

Ultimately the local solution was the quickest and easiest in terms of complexity to build out for the project. 

I have a sneaking suspicion that done properly, local compute and in-network storage could have less complexity on build out for the right organization as well. 


## The Deployment

- Pull repo

- Install duckdb

- Behold the dumpster fire that is `DataGeneration.py`

- Somehow create a venv with the required packages and Jupyter

- Run `DataGeneration.py`

- Run the jobs with `python -m src/{layer}/{layer}_etl` in order of bronze -> silver -> audit -> gold. 

- 🤑 or 😭 or both (works on my machine 😝).

- Run Flask API App when ready

- Load files and make calls to API in Jupyter notebook (or whatever other REPL front end you please)


# One Last Thing

Call your mom. Moms are the best. 
