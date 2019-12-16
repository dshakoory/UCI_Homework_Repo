import datetime as dt 
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask , jsonify


#setting up the dataset

engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)

# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)


Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session
session = scoped_session(sessionmaker(bind=engine))

last_12months = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
last_12months= dt.datetime.strptime(last_12months,"%Y-%m-%d")
date_oneyearago = last_12months - dt.timedelta(days = 365)


#make an app instance

app = Flask(__name__)

@app.route("/")
def welcome():

    return (
        f"Your Available Routes:<br/>"
        f"Last year's temp observations:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"Station list:<br/>"
        f"/api/v1.0/stations<br/>"
        f"Last's year's temp observation:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"List of the minimum , average and the max temperature for start date:<br/>"
        f"/api/v1.0/<start><br/>"
        f"List of the minimum , average and the max temperature for end date:<br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#precipitation for the last 12 months
@app.route("/api/v1.0/precipitation")

def precipitation():

	whole_12months = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date > date_oneyearago ).order_by(Measurement.date).all()

	precipitation_data = dict(whole_12months)
	return jsonify({'Data':precipitation_data})

#list of stations
@app.route("/api/v1.0/stations")
def stations():
	stations = session.query(Station).all()
	stations_list = list()
	for station in stations:
		stations_dict = dict()
		stations_dict['Station'] = station.station
		stations_dict["Station Name"] = station.name
		stations_dict["Latitude"] = station.latitude
		stations_dict["Longitude"] = station.longitude
		stations_dict["Elevation"] = station.elevation
		stations_list.append(stations_dict)

	return jsonify ({'Data':stations_list})

@app.route("/api/v1.0/tobs")
def tobs():

	twelve_month_tobs = session.query(Measurement.tobs,Measurement.date,Measurement.station).filter(Measurement.date > first_date).all()

	temperature_list = list()
	for data in twelve_month_tobs:
		temperature_dict = dict()
		temperature_dict['Station'] = data.station
		temperature_dict['Date'] = data.date
		temperature_dict['Temp'] = data.tobs
		temperature_list.append(temperature_dict)

	return jsonify ({'Data':temperature_list})

@app.route("/api/v1.0/<start>")
def start_temp(start=None):
#when given the start only, calculate lowest_temp, avg_temp, highest_temp for all dates greater than and equal to the start date
	starting_temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

	start_list = list()
	for lowest_temp, avg_temp, highest_temp in starting_temps:
		starting_dict = {}
		starting_dict["Min Temp"] = lowest_temp
		starting_dict["Max Temp"] = avg_temp
		starting_dict["Avg Temp"] = highest_temp
		start_list.append(starting_dict)

	return jsonify ({'Data':start_list})

@app.route("/api/v1.0/<start>/<end>")
def calc_temps(start=None,end=None):
    temperatures = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >= start,Measurement.date <= end).all()

    temp_list = list()
    for lowest_temp, avg_temp, highest_temp in temperatures:
    	temp_dict = dict()
    	temp_dict["Min Temp"] = lowest_temp
    	temp_dict["Avg Temo"] = avg_temp
    	temp_dict["Max Temp"] = highest_temp
    	temp_list.append(temp_dict)
 #return json representation of the list
    return jsonify ({'Data':temp_list})
	
	#run the app
if __name__ == '__main__':
    app.run(debug=True)