# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from flask import Flask, jsonify

# Setting up the database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement = Base.classes.measurement
session = Session(engine)

#`/api/v1.0/precipitation`

#`/api/v1.0/tobs`

#`/api/v1.0/stations`

#`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  



app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
    	f"Welcome to my 'Home' page!<br/>"
    	f"These are the availible paths:<br/>"
        f"/api/v1.0/precipitation - Precipitation Observations from the previous year<br/>"

        f"/api/v1.0/stations"
        f"- Observation stations<br/>"

        f"/api/v1.0/tobs"
        f"- Temperature Observations (tobs) for the previous year<br/>"

        f"/api/v1.0/temps/&ltstart&gt/&ltend&gt"
        f"- Minimum, average and maximum temps for start or start-end date range (format yyyy-mm-dd)<br/>"
)

# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
		most_recent_date_query=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
		most_recent_date=most_recent_date_query[0]
		most_recent_date_split=most_recent_date.split("-")
		year_before=str(int(most_recent_date_split[0])-1)
		one_year_earlier=year_before+'-'+most_recent_date_split[1]+'-'+most_recent_date_split[2]
		precip_query=session.query(Measurement.date, Measurement.prcp).\
    	filter(Measurement.date >= one_year_earlier).order_by(Measurement.date).all()
		precip_dict=dict(precip_query)

		return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
		stations=session.query(Station.station, Station.name).group_by(Station.name).all()
		return (
			stations[0][1], stations[1][1]
			)
"""
@app.route("/api/v1.0/tobs")
def tobs():
	#I know this isn't working but it all looks right!!!!!  I keep getting an error on my indentations :(
		most_recent_date_query=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
		most_recent_date=most_recent_date_query[0]
		most_recent_date_split=most_recent_date.split("-")
		year_before=str(int(most_recent_date_split[0])-1)
		one_year_earlier=year_before+'-'+most_recent_date_split[1]+'-'+most_recent_date_split[2]
		precip_query=session.query(Measurement.date, Measurement.tobs).\
    	filter(Measurement.date >= one_year_earlier).order_by(Measurement.date).all()
    	return(precip_query)
"""
@app.route("/api/v1.0/<start>")
def start():
	#start_date="2016-09-22"
	#end_date="2016-09-27"
	def calc_temps(desired_start_date, desired_end_date):
	    start_date=year_before(desired_start_date)
	    end_date=year_before(desired_end_date)
	    vacay_list = session.query(Measurement.tobs, Measurement.date).filter(Measurement.date>=start_date)\
	        .filter(Measurement.date<=end_date).all()
	    vacay_temps_list = []
	    for item in vacay_list:
	        vacay_temps_list.append(item[0])
	    minimumn_temp = min(vacay_temps_list)
	    maximum_temp = max(vacay_temps_list)
	    average_temp = mean(vacay_temps_list)
	    return minimumn_temp, maximum_temp, average_temp
	user_start_date=input("When would you like to start your vaction?  Format YYYY-MM-DD ")
	user_end_date=input("When would you like to end your vacation?  Format YYYY-MM-DD ")
	trip_min_temp, trip_max_temp, trip_avg_temp = calc_temps(user_start_date, user_end_date)
	print("The minimum temperature is: %s" % str(trip_min_temp))
	print("The maximum temperature is: %s" % str(trip_max_temp))
	print("The average temperature is: %s" % str(trip_avg_temp))









if __name__ == "__main__":
    app.run(debug=True)




