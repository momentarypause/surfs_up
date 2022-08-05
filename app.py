# Import dependencies
from flask import Flask, jsonify

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# Set up database
engine = create_engine("sqlite:///surfs_up_Data/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# Create New Flask app Instance
app = Flask(__name__)

# Define root (starting point)
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br></br>
    <br> Available Routes:</br>
    <br> /api/v1.0/precipitation </br>
    <br> /api/v1.0/stations </br>
    <br> /api/v1.0/tobs </br>
    <br> /api/v1.0/temp/start/end </br>
    ''')

# Precipitation Route: write a query to get the date and precipitation for previous year and create a (jsonify) dict with date as key and precip as value
# Create route
@app.route("/api/v1.0/precipitation")
# Create function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# Stations Route: get all stations and unravel results into a 1-D array, convert to a list
# Create Route
@app.route("/api/v1.0/stations")
# Create function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# Monthly temp route: get temps for the last year from the primary station.  Unravel into a 1-D array and convert to list and jsonify
# Create route
@app.route("/api/v1.0/tobs")
# Create function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Stats Route: find min, max, and avg temps
# Create Route with starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Create function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
