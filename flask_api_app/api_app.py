from flask import Flask, jsonify, request
from faker import Faker
import random
from xpinyin import Pinyin
p = Pinyin()

# Fakerインスタンスの初期化
fake = Faker()

app = Flask(__name__)

def generate_uk_station_api_response():
    fake = Faker("en_GB")
    train_id = fake.bothify("#").upper()+fake.numerify("#####")
    response =  {
      "date": fake.date()
      ,"time_of_day": fake.numerify("##:##")
      ,"request_time": fake.date_time()
      ,"station_name": fake.city() 
      ,"station_code": fake.bothify("###").upper()+fake.bothify("###")
      ,"departures": {
        "all": [
            
          {
             "mode": "train"
            ,"service": fake.numerify("#######")
            ,"train_uid": fake.bothify("#").upper()+fake.numerify("#####")
            ,"platform": str(random.randrange(1,30))
            ,"operator": fake.bothify("##").upper()
            ,"operator_name": fake.city() + " Railway"
            ,"aimed_departure_time": fake.numerify("##:##")
            ,"aimed_arrival_time": fake.numerify("##:##")
            ,"aimed_pass_time": None
            ,"origin_name": fake.city() 
            ,"destination_name": fake.city() 
            ,"source": "Network Rail"
            ,"category": fake.numerify("##")
            ,"service_timetable": {
              "id": f"http://yourmomstrainservice.com/v3/uk/train/service_timetables/{train_id}:{fake.date()}?live=true"
            }
            ,"status": random.choice(["EARLY","ON-TIME","LATE", "YOUR MOM"])
            ,"expected_arrival_time": fake.numerify("##:##")
            ,"expected_departure_time": fake.numerify("##:##")
            ,"best_arrival_estimate_mins": str(int(fake.numerify("###")))
            ,"best_departure_estimate_mins": str(int(fake.numerify("###")))
          } for train in range(0,random.randrange(1,25))
        ]
      }
    }
    return response

def generate_uk_train_api_response():
    fake = Faker("en_GB")
    response = {
          "request_time": fake.date_time()
          ,"service": fake.numerify("########")
          ,"train_uid": fake.bothify("#").upper()+fake.numerify("#####")
          ,"headcode": fake.numerify("####")
          ,"toc": {
            "atoc_code": fake.bothify("##")
          }
          ,"train_status": "1"
          ,"mode": "train"
          ,"category": fake.numerify("##")
          ,"operator": fake.bothify("??").upper()
          ,"operator_name": fake.city() + " Railway"
          ,"stop_of_interest": fake.bothify("???").upper()
          ,"origin_name": fake.city() 
          ,"destination_name": fake.city() 
          ,"stops": [
            {
               "station_code": fake.bothify("???").upper()
              ,"tiploc_code": fake.bothify("??????").upper()
              ,"station_name": fake.city() 
              ,"status": random.choice(["EARLY","ON-TIME","LATE", "YOUR MOM"])
              ,"stop_type": random.choice(["LO", "LI", "LT", "YOUR MOM"])
              ,"platform": str(random.randrange(1,30))
              ,"aimed_arrival_date": fake.date()
              ,"aimed_arrival_time": fake.time()[:5]
              ,"aimed_pass_date": fake.date() 
              ,"aimed_pass_time": fake.time()[:5]
              ,"aimed_departure_date": fake.date() 
              ,"aimed_departure_time": fake.time()[:5]
              ,"expected_arrival_date": fake.date()
              ,"expected_arrival_time":fake.time()[:5]
              ,"expected_pass_date": fake.date()
              ,"expected_pass_time":fake.time()[:5]
              ,"expected_departure_date":fake.date()
              ,"expected_departure_time":fake.time()[:5]
            }
                for stop in range(1,random.randrange(2,30))
          ]
        }
    return response

def generate_china_station_api_response():
    fake = Faker("zh_CN")
    def get_station_name():
        station_name_cn = fake.city()
        station_name_pn = p.get_pinyin(station_name_cn,"")
        return (station_name_cn, station_name_pn)
    stations_for_station_response = get_station_name()
    station_response = \
        {
          "StatusCode": random.choice(["200","500", "YOUR MOM"])
          ,"StationNameEN": stations_for_station_response[0] 
          ,"StationNameCN": stations_for_station_response[1]
        }
    train_response_max = random.randrange(1,50)
    train_response_range = range(0,train_response_max)
    train_response_stations = [(get_station_name(), get_station_name()) for station in train_response_range]
    train_response = [
            
    {
      "TrainNo": fake.bothify("?").upper() + fake.numerify("####")
      ,"DepTime": fake.time()[:5] 
      ,"ArrTime": fake.time()[:5]
      ,"Duration":fake.numerify("#h##m")
      ,"DepStationEN": train_response_stations[train][0][0]
      ,"DepStationCN": train_response_stations[train][0][1]
      ,"ArrStationEN": train_response_stations[train][1][0] 
      ,"ArrStationCN": train_response_stations[train][1][1]       }
        for train in  train_response_range
    ]
    station_response["Trains"] = train_response
    return station_response

def generate_china_train_api_response():
    fake = Faker("zh_CN")
    def get_station_name():
        station_name_cn = fake.city()
        station_name_pn = p.get_pinyin(station_name_cn,"")
        return (station_name_cn, station_name_pn)
    
    train_response = \
        {
          "StatusCode": random.choice(["200","500", "YOUR MOM"])
        }
    train_no = fake.bothify("?#")
    timetable_response_max = random.randrange(1,50)
    timetable_response_range = range(0,timetable_response_max)
    timetable_response_stations = [get_station_name() for station in timetable_response_range]
    timetable_response = [
            
    {
      "TrainNo": train_no
      ,"StationNo": timetable+1
      ,"StationNameCN": timetable_response_stations[timetable][0]
      ,"StationNameEN": timetable_response_stations[timetable][1]
      ,"ArriveTime": fake.time()[:5] 
      ,"StartTime": fake.time()[:5] 
      ,"StopTime": fake.numerify("##min")
    }
        for timetable in  timetable_response_range
    ]
    train_response["TimeTable"] = timetable_response
    return train_response


def generate_us_station_api_response():
    fake = Faker("en_US")
    station_code = fake.bothify("???").upper()
    station_city = fake.city()
    response = {
        station_code:{
            "name": station_city + " Union Station"
            ,"code": station_code
            ,"tz": fake.timezone() 
            ,"lat": str(fake.latitude())
            ,"lon": str(fake.longitude())
            ,"address1": fake.address()
            ,"address2" : ""
            ,"city": station_city
            ,"state": fake.state_abbr()
            ,"zip": fake.zipcode()
            ,"trains": [
                {
                     "TrainNo": fake.numerify("%-%")
                    ,"DepartureTime": fake.time()[:5]
                    ,"ArrivalTime": fake.time()[:5]
                    ,"Stops": [
                      {
                         "StopStation": fake.city()
                        ,"ArrivalTime": fake.time()[:5] 
                        ,"DepartureTime": fake.time()[:5] 
                      }
                 for stop in range(0,random.randrange(10))     
                    ]
                }
            for train in range(0,random.randrange(10)) 
            ]
        }
    }
    return response

def generate_us_train_api_response():
    fake = Faker("en_US")
    train_no = str(random.randrange(1,15))
    train_id =  train_no + "_" + str((int(train_no)+2))
    response = {
        train_no:{
          "routeName": fake.city() + random.choice([" Zephyr", " Express", " Limited", " Builder"])
          ,"trainNum": train_no 
          ,"trainID": train_id
          ,"lat": str(fake.latitude())
          ,"lon": str(fake.longitude())
          ,"trainTimely": random.choice(["Yes", "No", "Sir, this is Amtrak"])
          ,"stations": [
                {
                    
                   "name": fake.city() + " Union Station" 
                  ,"code": fake.lexify("???").upper()
                  ,"tz": fake.timezone() 
                  ,"bus": False
                  ,"schArr": fake.date_time()
                  ,"schDep": fake.date_time()
                  ,"arr": fake.date_time()
                  ,"dep": fake.date_time()
                  ,"arrCmnt": f"{random.randrange(0,10)} Minutes Early"
                  ,"depCmnt": f"{random.randrange(0,10)} Minutes Early"
                  ,"status": random.choice(["Arriving", "Arrived", "Departed", "Making Cookies"])
                }
                for station in range(0, random.randrange(1,25))
              ]
        }
    }
    return response


def generate_japan_station_api_response():
    fake = Faker("ja_JP")
    response =  {
  "ResultSet": {
     "apiVersion": "1.27.0.0"
    ,"engineVersion": "201802_03a"
    ,"TimeTable": {
       "trainCount": random.randrange(1,300)
      ,"code": fake.numerify("####")
      ,"dateGroup": random.choice(["weekday","weekend","holiday","your mom"])
      ,"Station": {
        "Name": fake.city()
      }
      ,"HourTable": [
        {
           "TimeReliability": "onTimeTable"
          ,"MinuteTable": [
            {
               "Minute": random.randrange(0,59)
              ,"Stop": {
                 "kindCode":  fake.numerify("%")
                ,"platformNo": random.randrange(1,40)
                ,"lineCode": fake.numerify("#####")
                ,"nameCode": random.randrange(1,200)
                ,"destinationCode": random.randrange(1,200)
              }
            }
            for minute in range(0,random.randrange(1,8))
          ] 
          ,"Hour": hour
        }
        for hour in range(0,random.randrange(1,24))
      ]
      ,"Line": {
         "Name": fake.city()+"線"
        ,"Direction": fake.city()
        ,"Source": fake.city() 
        ,"Color": fake.numerify("#########")
      }
      ,"LineName": {
         "text": "無し"
        ,"code": "1"
      }
      ,"LineDestination": [
        {
          "text": fake.city()
          ,"code": random.randrange(1,10000)
        } 
        for destination in range(0,random.randrange(1,25))
      ]
      ,"LineKind": {
         "text": random.choice(["各駅停車","快速","特急","新幹線", "Your mom"])
        ,"code": random.randrange(1,10000)
      }
    }
  }
}
    return response


def generate_japan_train_api_response():
    fake = Faker("ja_JP")
    fare = random.randrange(100,100000)
    def generate_station():
        return {
             "code": str(random.randint(10000, 99999))
            ,"name": fake.street_name()
            ,"type": "train"
            ,"yomi": fake.word()
        }

    def generate_geo_point():
        return {
             "longi": f"{random.randint(100, 139)}.{random.randint(0, 59)}.{random.randint(0, 59)}"
            ,"lati": f"{random.randint(30, 35)}.{random.randint(0, 59)}.{random.randint(0, 59)}"
            ,"longi_d": str(fake.longitude())
            ,"gcs": "tokyo"
            ,"lati_d": str(fake.latitude())
        }

    def generate_line():
        return {
             "stopstationcount": str(random.randint(0, 10))
            ,"timeonboard": str(random.randint(0, 60))
            ,"exhaustco2": str(random.randint(0, 1000))
            ,"exhaustco2atpassengercar": str(random.randint(0, 1000))
            ,"distance": str(random.randint(0, 100))
            ,"name": fake.company() + "鐵道"
            ,"type": "train"
            ,"arrivalstate": {
                "type": "normal"
                ,"datetime": fake.iso8601()
            }
            ,"departurestate": {
                 "type": "normal"
                ,"datetime": fake.iso8601()
            }
            ,"color": fake.numerify("#########")
        }

    def generate_course():
        return {
             "searchtype": "departure"
            ,"datatype": "ontimetable"
            ,"serializedata": fake.sha256()
            ,"price": [
                {
                     "kind": "faresummary"
                    ,"oneway": str(random.randint(100, 500))
                    ,"round": str(random.randint(200,1000))
                }
            ]
            ,"route": {
                 "timeother": str(random.randint(0, 10))
                ,"timeonboard": str(random.randint(0, 60))
                ,"exhaustco2": str(random.randint(0, 1000))
                ,"exhaustco2atpassengercar": str(random.randint(0, 1000))
                ,"distance": str(random.randint(0, 100))
                ,"timewalk": str(random.randint(0, 30))
                ,"transfercount": str(random.randint(0, 5))
                ,"line": [generate_line() for _ in range(3)]
                ,"point": [
                    {
                        "name": fake.city()
                    }
                    ,{
                         "station": generate_station()
                        ,"prefecture": {
                             "code": str(random.randint(1, 47))
                            ,"name": fake.city()
                        }
                        ,"geopoint": generate_geo_point()
                    }
                ]
            }
        }

    api_structure = {
        "resultset": {
             "apiversion": "1.27.0.0"
            ,"engineversion": "201806_02a"
            ,"course": [generate_course() for _ in range(3)]
        }
    }
    return api_structure


# エンドポイントの例

@app.route('/api/uk_station', methods=['GET'])
def get_uk_station():
    response = generate_uk_station_api_response()
    return jsonify(response)

@app.route('/api/uk_train', methods=['GET'])
def get_uk_train():
    response = generate_uk_train_api_response()
    return jsonify(response)

@app.route('/api/china_station', methods=['GET'])
def get_china_station():
    response = generate_china_station_api_response()
    return jsonify(response)

@app.route('/api/china_train', methods=['GET'])
def get_china_train():
    response = generate_china_train_api_response()
    return jsonify(response)

@app.route('/api/us_station', methods=['GET'])
def get_us_station():
    response = generate_us_station_api_response()
    return jsonify(response)

@app.route('/api/us_train', methods=['GET'])
def get_us_train():
    response = generate_us_train_api_response()
    return jsonify(response)


@app.route('/api/japan_station', methods=['GET'])
def get_japan_station():
    response = generate_japan_station_api_response()
    return jsonify(response)


@app.route('/api/japan_train', methods=['GET'])
def get_japan_train():
    response = generate_japan_train_api_response()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)
