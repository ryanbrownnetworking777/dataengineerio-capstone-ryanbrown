# DataEngineer.io | Dataexpert.io Bootcamp Capstone Project
## Ryan Brown

# LORE (Scenario)

Bakehouse Central is where your inner Cookie Monster hangs out. They operate stalls in various train stations and smaller outfits **on the trains themselves** in the US, UK, China, and Japan. 
A significantly popular chain, they enjoy a large loyalty program membership and high usage of their Bakehouse Central app.  

They operate a data lakehouse, affectionately called the "Data Bakehouse" to store and perform analytics and other business functions off of their enterprise data across these four countries. 

Their engineers have pioneered new ovens and other robotic machinery to propel on-site production to insane heights. Near real-time production of tasty treats is now possible both on and off train.  

Following the success of promotional campaigns tying an event with the arrival of a specific train in each of the markets, management has descended into madness. 

Management has now several demands for a new analytics and data-empowered business intiatives. 

- Real time alignment of trains to production of baked goods, ideally with suggested commemerative treats for their loyalty members. (Operational Data use case)
- Updates on sales and profitability of each stores. (Analytics Use Case) 
- Down to machine level operational visibility for supply and demand planners.  
- Hourly refreshing dashboards


# Use Cases

Each of management's demands can be broken down into several distinct use cases that map into different business areas.

## Supply Chain | Operations 

- Real time alignment of trains to production of baked goods, ideally with suggested commemerative treats for their loyalty members. (Operational Data use case)

    - Production Planning 
        - Create a forecast based upon train timetable and potential rolling stock capacity. 

- Down to machine level operational visibility for supply and demand planners.  

    - Current WOs
    - Current Capacity 

## Marketing | Sales 

- Promotional suggestions to loyalty members based upon external events or train happenings

## Finance



## IT

# Data

## Train

- 4 Trail APIs
    - UK Rail Timetable 
    - China Rail Train 
    - Japan Rail Train  
    - Amtrak Train 

- 1 ERP:
    Netsuite


## Data Details


### UK Rail Timetable

#### UK Station Timetable

Synthetic data based upon [TransportAPI](https://developer.transportapi.com/docs#get-/v3/uk/train/service_timetables/-service-.json). 

data will be a generated json blob with the following fields per the transportapi documentation:

```
{
  "date": "2022-08-04",
  "time_of_day": "15:23",
  "request_time": "2022-08-04T15:23:18+01:00",
  "station_name": "Richmond",
  "station_code": "crs:RMD",
  "departures": {
    "all": [
      {
        "mode": "train",
        "service": "24671105",
        "train_uid": "Y70941",
        "platform": "2",
        "operator": "SW",
        "operator_name": "South Western Railway",
        "aimed_departure_time": "15:28",
        "aimed_arrival_time": "15:28",
        "aimed_pass_time": null,
        "origin_name": "Windsor & Eton Riverside",
        "destination_name": "London Waterloo",
        "source": "Network Rail",
        "category": "OO",
        "service_timetable": {
          "id": "http://transportapi.com/v3/uk/train/service_timetables/Y70941:2022-08-04?live=true"
        },
        "status": "EARLY",
        "expected_arrival_time": "15:28",
        "expected_departure_time": "15:28",
        "best_arrival_estimate_mins": 4,
        "best_departure_estimate_mins": 4
      },
      {
        "mode": "train",
        "service": "22214000",
        "train_uid": "Y21211",
        "platform": "4",
        "operator": "LO",
        "operator_name": "London Overground",
        "aimed_departure_time": "15:32",
        "aimed_arrival_time": null,
        "aimed_pass_time": null,
        "origin_name": "Richmond",
        "destination_name": "Stratford",
        "source": "Network Rail",
        "category": "OO",
        "service_timetable": {
          "id": "http://transportapi.com/v3/uk/train/service_timetables/Y21211:2022-08-04?live=true"
        },
        "status": "STARTS HERE",
        "expected_arrival_time": null,
        "expected_departure_time": "15:32",
        "best_arrival_estimate_mins": null,
        "best_departure_estimate_mins": 8
      }
    ]
  }
}
```

These fields are defined in the following way, again per the TransportAPI documentation. 

```
station_code *
string
Specifies the station code of the station of interest as specified in the request.

station_name *
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

request_time *
date-time
The time of making the API request.

date *
string
The date of interest as specified in the request.

time_of_day *
string
The time of interest as specified in the request

- departures
object
A wrapper object containing all departures for this train station.

- all*
array of object
An array containing all departures for this train station.

mode *
string
The mode of transport for the service. The value would be train for regular services and bus for replacement bus services.

service *
string
When source_config=dws_staff, the value is the Darwin RID of the train service.

Otherwise, this is The Network Rail service code of the service.

train_uid *
string
The train uid of the service

platform *
string┃null
The platform at which the train servicing this departure is scheduled to call at or pass through the given station. When live=true and realtime data about the platform is available, the realtime value is used.

operator *
string┃null
The ATOC code of the train operating company operating the service.

operator_name *
string┃null
The public facing name of the train operating company operating the service.

aimed_departure_time *
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_arrival_time *
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time *
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
origin_name *
string┃null
The public facing name of the origin station for the train service: a short descriptive locally unique name text.

destination_name *
string┃null
The public facing name of the destination station for the train service: a short descriptive locally unique name text.

source *
string
A short description of the data sources used to populate the data for this train departure.

category *
string┃null
The category of the train service. View the full list of possible values.

- service_timetable*
object
An object containing details about the train service timetable for this departure.

id *
string
The ID of the train service timetable for this departure: a URL pointing to it.

status
enum┃null
A textual realtime status description of the service at the station based on the available RTI data.

Can be null if the train should have already progressed past the station.

This field is likely to be deprecated or altered in future.

Allowed: ARRIVED┃CANCELLED┃CHANGE OF IDENTITY┃CHANGE OF ORIGIN┃EARLY┃LATE┃NO REPORT┃OFF ROUTE┃ON TIME┃REINSTATEMENT┃STARTS HERE┃DELAYED┃BUS┃null
expected_departure_time
string┃null
The expected departure time for the service from this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
expected_arrival_time
string┃null
The expected arrival time for the service to this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
actual_departure_time
string┃null
The actual observed time that the service departed from the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_arrival_time
string┃null
The actual observed time that the service arrived at the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_pass_time
string┃null
The actual observed time that the service passed through the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
best_departure_estimate_mins
integer┃null
Estimated time offset in minutes until departure of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

best_arrival_estimate_mins
integer┃null
Estimated time offset in minutes until arrival of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

- station_detail
object or null
An object containing additional station detail about certain stations.

Present only when the station_detail parameter is used.

- origin
object or null
An object containing additional station detail for the origin station of this departure.

Present only when origin is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- destination
object or null
An object containing additional station detail for the destination station of this departure.

Present only when destination is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- called_at
array of object
A list of objects containing additional station detail about each previous time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used.
⮕ [ An object containing additional station detail about a particular time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- calling_at
array of object
A list of objects containing additional station detail about each upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used.
⮕ [ An object containing additional station detail about an upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- arrivals
object
A wrapper object containing all arrivals for this train station.

- all*
array of object
An array containing all departures for this train station.

mode *
string
The mode of transport for the service. The value would be train for regular services and bus for replacement bus services.

service *
string
When source_config=dws_staff, the value is the Darwin RID of the train service.

Otherwise, this is The Network Rail service code of the service.

train_uid *
string
The train uid of the service

platform *
string┃null
The platform at which the train servicing this departure is scheduled to call at or pass through the given station. When live=true and realtime data about the platform is available, the realtime value is used.

operator *
string┃null
The ATOC code of the train operating company operating the service.

operator_name *
string┃null
The public facing name of the train operating company operating the service.

aimed_departure_time *
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_arrival_time *
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time *
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
origin_name *
string┃null
The public facing name of the origin station for the train service: a short descriptive locally unique name text.

destination_name *
string┃null
The public facing name of the destination station for the train service: a short descriptive locally unique name text.

source *
string
A short description of the data sources used to populate the data for this train departure.

category *
string┃null
The category of the train service. View the full list of possible values.

- service_timetable*
object
An object containing details about the train service timetable for this departure.

id *
string
The ID of the train service timetable for this departure: a URL pointing to it.

status
enum┃null
A textual realtime status description of the service at the station based on the available RTI data.

Can be null if the train should have already progressed past the station.

This field is likely to be deprecated or altered in future.

Allowed: ARRIVED┃CANCELLED┃CHANGE OF IDENTITY┃CHANGE OF ORIGIN┃EARLY┃LATE┃NO REPORT┃OFF ROUTE┃ON TIME┃REINSTATEMENT┃STARTS HERE┃DELAYED┃BUS┃null
expected_departure_time
string┃null
The expected departure time for the service from this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
expected_arrival_time
string┃null
The expected arrival time for the service to this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
actual_departure_time
string┃null
The actual observed time that the service departed from the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_arrival_time
string┃null
The actual observed time that the service arrived at the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_pass_time
string┃null
The actual observed time that the service passed through the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
best_departure_estimate_mins
integer┃null
Estimated time offset in minutes until departure of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

best_arrival_estimate_mins
integer┃null
Estimated time offset in minutes until arrival of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

- station_detail
object or null
An object containing additional station detail about certain stations.

Present only when the station_detail parameter is used.

- origin
object or null
An object containing additional station detail for the origin station of this departure.

Present only when origin is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- destination
object or null
An object containing additional station detail for the destination station of this departure.

Present only when destination is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- called_at
array of object
A list of objects containing additional station detail about each previous time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used.
⮕ [ An object containing additional station detail about a particular time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- calling_at
array of object
A list of objects containing additional station detail about each upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used.
⮕ [ An object containing additional station detail about an upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- passes
object
A wrapper object containing all passes for this train station.

- all*
array of object
An array containing all departures for this train station.

mode *
string
The mode of transport for the service. The value would be train for regular services and bus for replacement bus services.

service *
string
When source_config=dws_staff, the value is the Darwin RID of the train service.

Otherwise, this is The Network Rail service code of the service.

train_uid *
string
The train uid of the service

platform *
string┃null
The platform at which the train servicing this departure is scheduled to call at or pass through the given station. When live=true and realtime data about the platform is available, the realtime value is used.

operator *
string┃null
The ATOC code of the train operating company operating the service.

operator_name *
string┃null
The public facing name of the train operating company operating the service.

aimed_departure_time *
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_arrival_time *
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time *
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
origin_name *
string┃null
The public facing name of the origin station for the train service: a short descriptive locally unique name text.

destination_name *
string┃null
The public facing name of the destination station for the train service: a short descriptive locally unique name text.

source *
string
A short description of the data sources used to populate the data for this train departure.

category *
string┃null
The category of the train service. View the full list of possible values.

- service_timetable*
object
An object containing details about the train service timetable for this departure.

id *
string
The ID of the train service timetable for this departure: a URL pointing to it.

status
enum┃null
A textual realtime status description of the service at the station based on the available RTI data.

Can be null if the train should have already progressed past the station.

This field is likely to be deprecated or altered in future.

Allowed: ARRIVED┃CANCELLED┃CHANGE OF IDENTITY┃CHANGE OF ORIGIN┃EARLY┃LATE┃NO REPORT┃OFF ROUTE┃ON TIME┃REINSTATEMENT┃STARTS HERE┃DELAYED┃BUS┃null
expected_departure_time
string┃null
The expected departure time for the service from this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
expected_arrival_time
string┃null
The expected arrival time for the service to this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
actual_departure_time
string┃null
The actual observed time that the service departed from the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_arrival_time
string┃null
The actual observed time that the service arrived at the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_pass_time
string┃null
The actual observed time that the service passed through the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
best_departure_estimate_mins
integer┃null
Estimated time offset in minutes until departure of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

best_arrival_estimate_mins
integer┃null
Estimated time offset in minutes until arrival of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

- station_detail
object or null
An object containing additional station detail about certain stations.

Present only when the station_detail parameter is used.

- origin
object or null
An object containing additional station detail for the origin station of this departure.

Present only when origin is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- destination
object or null
An object containing additional station detail for the destination station of this departure.

Present only when destination is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- called_at
array of object
A list of objects containing additional station detail about each previous time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used.
⮕ [ An object containing additional station detail about a particular time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- calling_at
array of object
A list of objects containing additional station detail about each upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used.
⮕ [ An object containing additional station detail about an upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- updates
object
A wrapper object containing all updates for this train station.

- all*
array of object
An array containing all departures for this train station.

mode *
string
The mode of transport for the service. The value would be train for regular services and bus for replacement bus services.

service *
string
When source_config=dws_staff, the value is the Darwin RID of the train service.

Otherwise, this is The Network Rail service code of the service.

train_uid *
string
The train uid of the service

platform *
string┃null
The platform at which the train servicing this departure is scheduled to call at or pass through the given station. When live=true and realtime data about the platform is available, the realtime value is used.

operator *
string┃null
The ATOC code of the train operating company operating the service.

operator_name *
string┃null
The public facing name of the train operating company operating the service.

aimed_departure_time *
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_arrival_time *
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time *
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
origin_name *
string┃null
The public facing name of the origin station for the train service: a short descriptive locally unique name text.

destination_name *
string┃null
The public facing name of the destination station for the train service: a short descriptive locally unique name text.

source *
string
A short description of the data sources used to populate the data for this train departure.

category *
string┃null
The category of the train service. View the full list of possible values.

- service_timetable*
object
An object containing details about the train service timetable for this departure.

id *
string
The ID of the train service timetable for this departure: a URL pointing to it.

status
enum┃null
A textual realtime status description of the service at the station based on the available RTI data.

Can be null if the train should have already progressed past the station.

This field is likely to be deprecated or altered in future.

Allowed: ARRIVED┃CANCELLED┃CHANGE OF IDENTITY┃CHANGE OF ORIGIN┃EARLY┃LATE┃NO REPORT┃OFF ROUTE┃ON TIME┃REINSTATEMENT┃STARTS HERE┃DELAYED┃BUS┃null
expected_departure_time
string┃null
The expected departure time for the service from this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
expected_arrival_time
string┃null
The expected arrival time for the service to this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
actual_departure_time
string┃null
The actual observed time that the service departed from the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_arrival_time
string┃null
The actual observed time that the service arrived at the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_pass_time
string┃null
The actual observed time that the service passed through the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
best_departure_estimate_mins
integer┃null
Estimated time offset in minutes until departure of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

best_arrival_estimate_mins
integer┃null
Estimated time offset in minutes until arrival of the service. Based on RTI data if available, or timetable data if not. Can be negative.

This field is likely to be deprecated in future.

- station_detail
object or null
An object containing additional station detail about certain stations.

Present only when the station_detail parameter is used.

- origin
object or null
An object containing additional station detail for the origin station of this departure.

Present only when origin is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- destination
object or null
An object containing additional station detail for the destination station of this departure.

Present only when destination is used in the station_detail parameter.

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- called_at
array of object
A list of objects containing additional station detail about each previous time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used.
⮕ [ An object containing additional station detail about a particular time the train service for this departure has called at the train station, specified via the called_at parameter.

Present only when called_at is used in the station_detail parameter and the called_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
- calling_at
array of object
A list of objects containing additional station detail about each upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used.
⮕ [ An object containing additional station detail about an upcoming time the train service for this departure will call at the train station, specified via the calling_at parameter.

Present only when calling_at is used in the station_detail parameter and the calling_at parameter is used. ]

station_code
string┃null
The CRS code of the station.

tiploc_code
string┃null
The TIPLOC code of the station.

station_name
string┃null
The public facing name of the train station: a short descriptive locally unique name text.

platform
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_time
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_departure_time
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_time
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
```

This station timetable API will inform the production schedules for cookies at the railway station locations of Bakehouse Central. 

#### UK Train Timetable


Synthetic data based upon [TransportApi](https://developer.transportapi.com/docs#get-/v3/uk/train/service_timetables/-service-.json). 

Data will be a generated JSON blob with the following fields per the TransportAPI documentation:

```
{
  "request_time": "2022-08-04T15:23:18+01:00",
  "service": "25505005",
  "train_uid": "L03365",
  "headcode": "1024",
  "toc": {
    "atoc_code": "SR"
  },
  "train_status": "1",
  "mode": "train",
  "category": "OO",
  "operator": "13",
  "operator_name": "Scotrail",
  "stop_of_interest": "PAD",
  "origin_name": "London Paddington",
  "destination_name": "Heathrow Airport Terminal 5",
  "stops": [
    {
      "station_code": "PAD",
      "tiploc_code": "PADTON",
      "station_name": "London Paddington",
      "status": "LATE",
      "stop_type": "LO",
      "platform": "3",
      "aimed_arrival_date": "2022-08-04",
      "aimed_arrival_time": "15:23",
      "aimed_pass_date": "2022-08-04",
      "aimed_pass_time": "15:23",
      "aimed_departure_date": "2022-08-04",
      "aimed_departure_time": "15:24",
      "expected_arrival_date": "2022-08-04",
      "expected_arrival_time": "15:24",
      "expected_pass_date": "2022-08-04",
      "expected_pass_time": "15:24",
      "expected_departure_date": "2022-08-04",
      "expected_departure_time": "15:25"
    },
    {
      "station_code": "EAL",
      "tiploc_code": "EALINGB",
      "station_name": "Ealing Broadway",
      "status": "LATE",
      "stop_type": "LI",
      "platform": "1",
      "aimed_arrival_date": "2022-08-04",
      "aimed_arrival_time": "15:33",
      "aimed_pass_date": "2022-08-04",
      "aimed_pass_time": "15:33",
      "aimed_departure_date": "2022-08-04",
      "aimed_departure_time": "15:34",
      "expected_arrival_date": "2022-08-04",
      "expected_arrival_time": "15:34",
      "expected_pass_date": "2022-08-04",
      "expected_pass_time": "15:34",
      "expected_departure_date": "2022-08-04",
      "expected_departure_time": "15:35"
    }
  ]
}
```

These fields are defined in the following way, again per the TransportAPI documentation. 

```
request_time *
date-time
The time of making the API request.

service *
string
When source_config=dws_staff, the value is the Darwin RID of the train service.

Otherwise, this is The Network Rail service code of the service.

train_uid *
string
The train uid of the service

headcode *
string
The headcode of the service

- toc*
object
Train operating company information

atoc_code *
string┃null
The ATOC code of the train operating company operating the service.

train_status *
string┃null
The transport service type using CIF Train Status value. View the full list of possible values

mode *
string
The mode of transport for the service. The value would be train for regular services and bus for replacement bus services.

category *
string┃null
The category of the train service. View the full list of possible values.

operator *
string┃null
The ATOC code of the train operating company operating the service.

operator_name *
string┃null
The public facing name of the train operating company operating the service.

stop_of_interest *
string┃null
Not used. Value will be null.

origin_name *
string┃null
The public facing name of the origin station for the train service: a short descriptive locally unique name text.

destination_name *
string┃null
The public facing name of the destination station for the train service: a short descriptive locally unique name text.

- stops*
array of object
An array containing all stations for this train service.

station_code *
string
The CRS code of the station.

tiploc_code *
string
The TIPLOC code of the station.

station_name *
string
The public facing name of the train station: a short descriptive locally unique name text.

status
enum┃null
A textual realtime status description of the service at the station based on the available RTI data.

Can be null if the train should have already progressed past the station.

This field is likely to be deprecated or altered in future.

Allowed: ARRIVED┃CANCELLED┃CHANGE OF IDENTITY┃CHANGE OF ORIGIN┃EARLY┃LATE┃NO REPORT┃OFF ROUTE┃ON TIME┃REINSTATEMENT┃STARTS HERE┃DELAYED┃BUS┃null
stop_type *
enum
The type of the train station: LO - origin LI - intermediate LT - terminating

Allowed: LO┃LI┃LT
platform *
string┃null
The platform at which the is scheduled to call at or pass through the given station.

aimed_arrival_date *
string┃null
Scheduled arrival date for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{4}-\d{2}-\d{2}$
aimed_arrival_time *
string┃null
Scheduled arrival time for the train service at this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
aimed_pass_date *
string┃null
Scheduled pass date for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{4}-\d{2}-\d{2}$
aimed_pass_time *
string┃null
Scheduled pass time for the train service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Pattern: ^\d{2}:\d{2}$
aimed_departure_date *
string┃null
Scheduled departure date for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{4}-\d{2}-\d{2}$
aimed_departure_time *
string┃null
Scheduled departure time for the train service at this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Pattern: ^\d{2}:\d{2}$
expected_arrival_date
string┃null
The expected arrival date for the service to this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{4}-\d{2}-\d{2}$
expected_arrival_time
string┃null
The expected arrival time for the service to this station.

Can be null if the train service doesn't arrive at the station e.g. when it's at the origin station and it only departs from it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
expected_pass_date
string┃null
The expected pass date for the service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Present only when live=true in the request.

Pattern: ^\d{4}-\d{2}-\d{2}$
expected_pass_time
string┃null
The expected pass time for the service through this station.

Can be null if the train service doesn't pass through the station, e.g. when it arrives and/or departs from it.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
expected_departure_date
string┃null
The expected departure date for the service from this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{4}-\d{2}-\d{2}$
expected_departure_time
string┃null
The expected departure time for the service from this station.

Can be null if the train service doesn't depart from the station e.g. when it's at the destination station and it only arrives to it or when it passes through a station.

Present only when live=true in the request.

Pattern: ^\d{2}:\d{2}$
actual_arrival_date
string┃null
The actual observed date that the service arrived at the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{4}-\d{2}-\d{2}$
actual_arrival_time
string┃null
The actual observed time that the service arrived at the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_pass_date
string┃null
The actual observed date that the service passed through the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{4}-\d{2}-\d{2}$
actual_pass_time
string┃null
The actual observed time that the service passed through the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
actual_departure_date
string┃null
The actual observed date that the service departed from the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{4}-\d{2}-\d{2}$
actual_departure_time
string┃null
The actual observed time that the service departed from the station, if that has already happened according to the realtime data, null otherwise.

Present only when source_config=dws_staff in the request.

Pattern: ^\d{2}:\d{2}$
```


### China Rail Timetable

#### China Station Timetable
 
Synthetic data based upon [China Train/Rail Rapid API](https://rapidapi.com/etcloud-etcloud-default/api/china-train-rail). 

Data will be a generated JSON blob with the following feilds. This response structure is synthetic as the China Train/Rail Rapid API endpoint for this type of data is broken. Inspiration taken from the "Search Train Tickets" endpoint. Generated with ChatGPT GPT-4.

```
{
  "StatusCode": "200",
  "StationNameEN": "Shanghai Hongqiao",
  "StationNameCN": "上海虹橋",
  "Trains": [
    {
      "TrainNo": "G1234",
      "DepTime": "07:30",
      "ArrTime": "10:45",
      "Duration": "3h15m",
      "DepStationEN": "Shanghai Hongqiao",
      "DepStationCN": "上海虹橋",
      "ArrStationEN": "Nanjing South",
      "ArrStationCN": "南京南",
      "StopStations": [
        {
          "StationNameEN": "Suzhou",
          "StationNameCN": "蘇州",
          "ArrivalTime": "08:00",
          "DepartureTime": "08:05"
        },
        {
          "StationNameEN": "Wuxi",
          "StationNameCN": "無錫",
          "ArrivalTime": "08:30",
          "DepartureTime": "08:35"
        },
        {
          "StationNameEN": "Changzhou",
          "StationNameCN": "常州",
          "ArrivalTime": "09:00",
          "DepartureTime": "09:05"
        }
      ]
    },
    {
      "TrainNo": "G5678",
      "DepTime": "08:00",
      "ArrTime": "11:20",
      "Duration": "3h20m",
      "DepStationEN": "Shanghai Hongqiao",
      "DepStationCN": "上海虹橋",
      "ArrStationEN": "Hangzhou East",
      "ArrStationCN": "杭州東",
      "StopStations": [
        {
          "StationNameEN": "Jiaxing South",
          "StationNameCN": "嘉興南",
          "ArrivalTime": "08:45",
          "DepartureTime": "08:50"
        },
        {
          "StationNameEN": "Huzhou",
          "StationNameCN": "湖州",
          "ArrivalTime": "09:15",
          "DepartureTime": "09:20"
        }
      ]
    }
    // その他の列車情報...
  ]
}

```


#### China Train Timetable

Synthetic data based upon [China Train/Rail Rapid API](https://rapidapi.com/etcloud-etcloud-default/api/china-train-rail). 

Data will be a generated JSON blob with the following fields per the Rapid API test response generator.


```
{
  "Status": "200",
  "TimeTable": [
    {
      "TrainNo": "G1",
      "StationNo": "1",
      "StationNameEN": "Beijing South",
      "StationNameCN": "北京南",
      "ArriveTime": "09:00",
      "StartTime": "09:00",
      "StopTime": "0min"
    },
    {
      "TrainNo": "G1",
      "StationNo": "2",
      "StationNameEN": "Jinan West",
      "StationNameCN": "济南西",
      "ArriveTime": "10:22",
      "StartTime": "10:24",
      "StopTime": "2min"
    },
    {
      "TrainNo": "G1",
      "StationNo": "3",
      "StationNameEN": "Nanjing South",
      "StationNameCN": "南京南",
      "ArriveTime": "12:24",
      "StartTime": "12:26",
      "StopTime": "2min"
    },
    {
      "TrainNo": "G1",
      "StationNo": "4",
      "StationNameEN": "Shanghai HongQiao",
      "StationNameCN": "上海虹桥",
      "ArriveTime": "13:28",
      "StartTime": "13:28",
      "StopTime": "0min"
    }
  ]
}
```


### US Rail Timetable

#### US Station Timetable

Synthetic data based upon [Amtrak.js](https://github.com/piemadd/amtrak/tree/master). 

Data will be a generated JSON blob with the following fields per the Amtrak.js documentation augmented and extended with ChatGPT GPT-4.

```
{
  "MSP": {
    "name": "St. Paul - Minneapolis Union",
    "code": "MSP",
    "tz": "America/Chicago",
    "lat": 44.947661,
    "lon": -93.085355,
    "address1": "240 Kellogg Boulevard East",
    "address2": " ",
    "city": "St. Paul",
    "state": "MN",
    "zip": "55101",
    "trains": [
      {
        "TrainNo": "7-9",
        "DepartureTime": "08:00",
        "ArrivalTime": "10:30",
        "Stops": [
          {
            "StopStation": "Minneapolis Central",
            "ArrivalTime": "08:45",
            "DepartureTime": "08:50"
          },
          {
            "StopStation": "Bloomington",
            "ArrivalTime": "09:15",
            "DepartureTime": "09:20"
          }
        ]
      },
      {
        "TrainNo": "7-8",
        "DepartureTime": "09:00",
        "ArrivalTime": "11:30",
        "Stops": [
          {
            "StopStation": "Minneapolis Central",
            "ArrivalTime": "09:45",
            "DepartureTime": "09:50"
          },
          {
            "StopStation": "Bloomington",
            "ArrivalTime": "10:15",
            "DepartureTime": "10:20"
          }
        ]
      },
      {
        "TrainNo": "8-9",
        "DepartureTime": "10:00",
        "ArrivalTime": "12:30",
        "Stops": [
          {
            "StopStation": "Minneapolis Central",
            "ArrivalTime": "10:45",
            "DepartureTime": "10:50"
          },
          {
            "StopStation": "Bloomington",
            "ArrivalTime": "11:15",
            "DepartureTime": "11:20"
          }
        ]
      }
    ]
  }
}
```


#### US Train Timetable

Synthetic data based upon [Amtrak.js](https://github.com/piemadd/amtrak/tree/master). 

Data will be a generated JSON blob with the following fields per the Amtrak.js documentation. 

```
{
  "7": [
    {
      "routeName": "Empire Builder",
      "trainNum": 7,
      "trainID": "7-9",
      "lat": 47.99575847096814,
      "lon": -97.89425087260365,
      "trainTimely": "NaN Minutes Early",
      "stations": [
        {
          "name": "Chicago Union",
          "code": "CHI",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T15:05:00-06:00",
          "schDep": "2024-01-09T15:05:00-06:00",
          "arr": "2024-01-09T15:05:00-06:00",
          "dep": "2024-01-09T15:05:00-06:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Glenview",
          "code": "GLN",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T15:29:00-06:00",
          "schDep": "2024-01-09T15:29:00-06:00",
          "arr": "2024-01-09T15:27:00-06:00",
          "dep": "2024-01-09T15:29:00-06:00",
          "arrCmnt": "2 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Milwaukee",
          "code": "MKE",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T16:35:00-06:00",
          "schDep": "2024-01-09T16:45:00-06:00",
          "arr": "2024-01-09T16:31:00-06:00",
          "dep": "2024-01-09T16:45:00-06:00",
          "arrCmnt": "4 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Columbus",
          "code": "CBS",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T17:55:00-06:00",
          "schDep": "2024-01-09T17:55:00-06:00",
          "arr": "2024-01-09T17:47:00-06:00",
          "dep": "2024-01-09T17:55:00-06:00",
          "arrCmnt": "8 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Portage",
          "code": "POG",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T18:24:00-06:00",
          "schDep": "2024-01-09T18:24:00-06:00",
          "arr": "2024-01-09T18:20:00-06:00",
          "dep": "2024-01-09T18:24:00-06:00",
          "arrCmnt": "4 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Wisconsin Dells",
          "code": "WDL",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T18:42:00-06:00",
          "schDep": "2024-01-09T18:42:00-06:00",
          "arr": "2024-01-09T18:39:00-06:00",
          "dep": "2024-01-09T18:42:00-06:00",
          "arrCmnt": "3 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Tomah",
          "code": "TOH",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T19:20:00-06:00",
          "schDep": "2024-01-09T19:20:00-06:00",
          "arr": "2024-01-09T19:18:00-06:00",
          "dep": "2024-01-09T19:20:00-06:00",
          "arrCmnt": "2 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "La Crosse",
          "code": "LSE",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T20:04:00-06:00",
          "schDep": "2024-01-09T20:04:00-06:00",
          "arr": "2024-01-09T20:05:00-06:00",
          "dep": "2024-01-09T20:09:00-06:00",
          "arrCmnt": "On Time",
          "depCmnt": "5 Minutes Late",
          "status": "Departed"
        },
        {
          "name": "Winona",
          "code": "WIN",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T20:34:00-06:00",
          "schDep": "2024-01-09T20:40:00-06:00",
          "arr": "2024-01-09T20:40:00-06:00",
          "dep": "2024-01-09T20:48:00-06:00",
          "arrCmnt": "6 Minutes Late",
          "depCmnt": "8 Minutes Late",
          "status": "Departed"
        },
        {
          "name": "Red Wing",
          "code": "RDW",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T21:42:00-06:00",
          "schDep": "2024-01-09T21:42:00-06:00",
          "arr": "2024-01-09T21:50:00-06:00",
          "dep": "2024-01-09T21:51:00-06:00",
          "arrCmnt": "8 Minutes Late",
          "depCmnt": "9 Minutes Late",
          "status": "Departed"
        },
        {
          "name": "St. Paul - Minneapolis Union",
          "code": "MSP",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-09T22:56:00-06:00",
          "schDep": "2024-01-09T23:13:00-06:00",
          "arr": "2024-01-09T22:46:00-06:00",
          "dep": "2024-01-09T23:13:00-06:00",
          "arrCmnt": "10 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "St. Cloud",
          "code": "SCD",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T01:09:00-06:00",
          "schDep": "2024-01-10T01:09:00-06:00",
          "arr": "2024-01-10T00:42:00-06:00",
          "dep": "2024-01-10T01:09:00-06:00",
          "arrCmnt": "27 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Staples",
          "code": "SPL",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T02:10:00-06:00",
          "schDep": "2024-01-10T02:10:00-06:00",
          "arr": "2024-01-10T02:09:00-06:00",
          "dep": "2024-01-10T02:10:00-06:00",
          "arrCmnt": "1 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Detroit Lakes",
          "code": "DLK",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T03:06:00-06:00",
          "schDep": "2024-01-10T03:06:00-06:00",
          "arr": "2024-01-10T03:05:00-06:00",
          "dep": "2024-01-10T03:07:00-06:00",
          "arrCmnt": "1 Minutes Early",
          "depCmnt": "On Time",
          "status": "Departed"
        },
        {
          "name": "Fargo",
          "code": "FAR",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T04:13:00-06:00",
          "schDep": "2024-01-10T04:13:00-06:00",
          "arr": "2024-01-10T03:58:00-06:00",
          "dep": "2024-01-10T04:13:00-06:00",
          "arrCmnt": "15 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Departed"
        },
        {
          "name": "Grand Forks",
          "code": "GFK",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T05:34:00-06:00",
          "schDep": "2024-01-10T05:34:00-06:00",
          "arr": "2024-01-10T05:20:00-06:00",
          "dep": "2024-01-10T05:39:00-06:00",
          "arrCmnt": "14 Minutes Early",
          "depCmnt": "5 Minutes Late",
          "status": "Departed"
        },
        {
          "name": "Devils Lake",
          "code": "DVL",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T06:59:00-06:00",
          "schDep": "2024-01-10T06:59:00-06:00",
          "arr": "2024-01-10T06:59:00-06:00",
          "dep": "2024-01-10T06:59:00-06:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Rugby",
          "code": "RUG",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T07:53:00-06:00",
          "schDep": "2024-01-10T07:53:00-06:00",
          "arr": "2024-01-10T07:53:00-06:00",
          "dep": "2024-01-10T07:53:00-06:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Minot",
          "code": "MOT",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T09:06:00-06:00",
          "schDep": "2024-01-10T09:51:00-06:00",
          "arr": "2024-01-10T09:06:00-06:00",
          "dep": "2024-01-10T09:06:00-06:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Stanley",
          "code": "STN",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T10:46:00-06:00",
          "schDep": "2024-01-10T10:46:00-06:00",
          "arr": "2024-01-10T10:46:00-06:00",
          "dep": "2024-01-10T10:46:00-06:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Williston",
          "code": "WTN",
          "tz": "America/Chicago",
          "bus": false,
          "schArr": "2024-01-10T11:59:00-06:00",
          "schDep": "2024-01-10T11:59:00-06:00",
          "arr": "2024-01-10T11:59:00-06:00",
          "dep": "2024-01-10T11:59:00-06:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Wolf Point",
          "code": "WPT",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T12:34:00-07:00",
          "schDep": "2024-01-10T12:34:00-07:00",
          "arr": "2024-01-10T12:34:00-07:00",
          "dep": "2024-01-10T12:34:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Glasgow",
          "code": "GGW",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T13:20:00-07:00",
          "schDep": "2024-01-10T13:20:00-07:00",
          "arr": "2024-01-10T13:20:00-07:00",
          "dep": "2024-01-10T13:20:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Malta",
          "code": "MAL",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T14:20:00-07:00",
          "schDep": "2024-01-10T14:20:00-07:00",
          "arr": "2024-01-10T14:20:00-07:00",
          "dep": "2024-01-10T14:20:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Havre",
          "code": "HAV",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T15:54:00-07:00",
          "schDep": "2024-01-10T16:15:00-07:00",
          "arr": "2024-01-10T15:54:00-07:00",
          "dep": "2024-01-10T15:54:00-07:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Shelby",
          "code": "SBY",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T18:13:00-07:00",
          "schDep": "2024-01-10T18:21:00-07:00",
          "arr": "2024-01-10T18:13:00-07:00",
          "dep": "2024-01-10T18:13:00-07:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Cut Bank",
          "code": "CUT",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T18:51:00-07:00",
          "schDep": "2024-01-10T18:51:00-07:00",
          "arr": "2024-01-10T18:51:00-07:00",
          "dep": "2024-01-10T18:51:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Browning",
          "code": "BRO",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T19:28:00-07:00",
          "schDep": "2024-01-10T19:28:00-07:00",
          "arr": "2024-01-10T19:28:00-07:00",
          "dep": "2024-01-10T19:28:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Essex",
          "code": "ESM",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T20:44:00-07:00",
          "schDep": "2024-01-10T20:44:00-07:00",
          "arr": "2024-01-10T20:44:00-07:00",
          "dep": "2024-01-10T20:44:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "West Glacier",
          "code": "WGL",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T21:27:00-07:00",
          "schDep": "2024-01-10T21:27:00-07:00",
          "arr": "2024-01-10T21:27:00-07:00",
          "dep": "2024-01-10T21:27:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Whitefish",
          "code": "WFH",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-10T22:06:00-07:00",
          "schDep": "2024-01-10T22:21:00-07:00",
          "arr": "2024-01-10T22:06:00-07:00",
          "dep": "2024-01-10T22:06:00-07:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Libby",
          "code": "LIB",
          "tz": "America/Denver",
          "bus": false,
          "schArr": "2024-01-11T00:05:00-07:00",
          "schDep": "2024-01-11T00:05:00-07:00",
          "arr": "2024-01-11T00:05:00-07:00",
          "dep": "2024-01-11T00:05:00-07:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Sandpoint",
          "code": "SPT",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T00:55:00-08:00",
          "schDep": "2024-01-11T00:55:00-08:00",
          "arr": "2024-01-11T00:55:00-08:00",
          "dep": "2024-01-11T00:55:00-08:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Spokane",
          "code": "SPK",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T02:44:00-08:00",
          "schDep": "2024-01-11T03:19:00-08:00",
          "arr": "2024-01-11T02:44:00-08:00",
          "dep": "2024-01-11T02:44:00-08:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Ephrata",
          "code": "EPH",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T05:28:00-08:00",
          "schDep": "2024-01-11T05:28:00-08:00",
          "arr": "2024-01-11T05:28:00-08:00",
          "dep": "2024-01-11T05:28:00-08:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Wenatchee",
          "code": "WEN",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T06:35:00-08:00",
          "schDep": "2024-01-11T06:45:00-08:00",
          "arr": "2024-01-11T06:35:00-08:00",
          "dep": "2024-01-11T06:35:00-08:00",
          "arrCmnt": "0 Minutes Early",
          "depCmnt": "0 Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Leavenworth",
          "code": "LWA",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T07:18:00-08:00",
          "schDep": "2024-01-11T07:18:00-08:00",
          "arr": "2024-01-11T07:18:00-08:00",
          "dep": "2024-01-11T07:18:00-08:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Everett",
          "code": "EVR",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T10:03:00-08:00",
          "schDep": "2024-01-11T10:03:00-08:00",
          "arr": "2024-01-11T09:44:00-08:00",
          "dep": "2024-01-11T09:44:00-08:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Edmonds",
          "code": "EDM",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T10:35:00-08:00",
          "schDep": "2024-01-11T10:35:00-08:00",
          "arr": "2024-01-11T10:12:00-08:00",
          "dep": "2024-01-11T10:12:00-08:00",
          "arrCmnt": "NaN Minutes Early",
          "depCmnt": "NaN Minutes Early",
          "status": "Enroute"
        },
        {
          "name": "Seattle King Street",
          "code": "SEA",
          "tz": "America/Los_Angeles",
          "bus": false,
          "schArr": "2024-01-11T11:29:00-08:00",
          "schDep": "2024-01-11T11:29:00-08:00",
          "arr": "2024-01-11T10:46:00-08:00",
          "dep": "2024-01-11T10:46:00-08:00",
          "arrCmnt": "43 Minutes Early",
          "depCmnt": "43 Minutes Early",
          "status": "Enroute"
        }
      ],
      "heading": "W",
      "eventCode": "DVL",
      "eventTZ": "America/Chicago",
      "eventName": "Devils Lake",
      "origCode": "CHI",
      "originTZ": "America/Chicago",
      "origName": "Chicago Union",
      "destCode": "SEA",
      "destTZ": "America/Los_Angeles",
      "destName": "Seattle King Street",
      "trainState": "Active",
      "velocity": 70.4634704589844,
      "statusMsg": " ",
      "createdAt": "2024-01-10T07:19:54-05:00",
      "updatedAt": "2024-01-10T07:19:54-05:00",
      "lastValTS": "2024-01-10T06:15:56-06:00",
      "objectID": 52
    }
  ]
}

```

### US Station Timetable


```
{
  "MSP": {
    "name": "St. Paul - Minneapolis Union",
    "code": "MSP",
    "tz": "America/Chicago",
    "lat": 44.947661,
    "lon": -93.085355,
    "address1": "240 Kellogg Boulevard East",
    "address2": " ",
    "city": "St. Paul",
    "state": "MN",
    "zip": "55101",
    "trains": [
      {
        "TrainNo": "7-9",
        "DepartureTime": "08:00",
        "ArrivalTime": "10:30",
        "Stops": [
          {
            "StopStation": "Minneapolis Central",
            "ArrivalTime": "08:45",
            "DepartureTime": "08:50"
          },
          {
            "StopStation": "Bloomington",
            "ArrivalTime": "09:15",
            "DepartureTime": "09:20"
          }
        ]
      },
      {
        "TrainNo": "7-8",
        "DepartureTime": "09:00",
        "ArrivalTime": "11:30",
        "Stops": [
          {
            "StopStation": "Minneapolis Central",
            "ArrivalTime": "09:45",
            "DepartureTime": "09:50"
          },
          {
            "StopStation": "Bloomington",
            "ArrivalTime": "10:15",
            "DepartureTime": "10:20"
          }
        ]
      },
      {
        "TrainNo": "8-9",
        "DepartureTime": "10:00",
        "ArrivalTime": "12:30",
        "Stops": [
          {
            "StopStation": "Minneapolis Central",
            "ArrivalTime": "10:45",
            "DepartureTime": "10:50"
          },
          {
            "StopStation": "Bloomington",
            "ArrivalTime": "11:15",
            "DepartureTime": "11:20"
          }
        ]
      }
    ]
  }
}

```


### Japan Rail Timetable

#### Japan Station Timetable

Synthetic data based upon [TransportAPI](https://developer.transportapi.com/docs#get-/v3/uk/train/service_timetables/-service-.json). 

Data will be a generated json blob with the following fields per the transportapi documentation:
