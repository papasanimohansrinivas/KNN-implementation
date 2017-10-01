
for running the code

<img src="docs/cmd.PNG" />

sample output from out.csv

<img src="docs/cmd_1.PNG" />

you can open the outputfile in cmd and can check result like this

<img src="docs/cmd_3.PNG" />


--- END NOTES ---

# Geofencing Validator 

# Dependencies Installation Guide

If you have pip3 installed in linux 
then use "sudo pip3 install geocoder"

else if ypu don't have even pip 
then install pip3 with 
"sudo apt-get install python3-setuptools"
then  "sudo easy_install3 pip"
then again try "sudo pip3 install geocoder"

# Project Description

  Checks whether address is appropriate for given lat,long

## Prerequisites
1. Python 3
  1. geocoder module is must
2.Mapbox apikey for their geocoding services.
  2. api_key for map_box_api = 
  api_key_1 = "pk.eyJ1IjoibW9oYW4wMCIsImEiOiJjajg0bDdudDYwOHM1MndwZmNjenp1dTduIn0.LxknjhXAQ_1n98amoXAANw"

  api_key_2 = "pk.eyJ1IjoibW9oYW4wMCIsImEiOiJjajgzZDZ6bGo3ZHdzMzNycjdlcnZqeHY4In0.caVuIsMV5qClz4zHIKvFIg"
  
## General Explanation 

geocoder is a python2/python3 module that acts as a wrapper for several of existing api's for geocoding services.

Some of them are yahoo,bing,google,MAPBOX,map_quest,etc.

And all services are not  created equal.

Some of them even are free but they haven't provided reliable results while testing the app.

Eg  map_quest gave wrong location address for lat,long that are in india. etcc...

MAP_BOX provided easy to parse and understandable json format.

I stuck with it beacause it was simple to use.

In future if you find map_box services as inadequate i urge you to change the code in map_box.py to suit your needs.

Ex change service from map_box to ..... .

# Algorithm 

I converted lat,long to address with map_box api

then i compared country of both addresses first if they were a match then sates and then cities then finally streets.

In between if any of them were a mismatch then i returned appropriate output like "same city","same state" ,etc..


## Local Testing

To run tests from terminal in ubuntu 

use cmd:- python3 geocodingValidator_.py location-for-dev.csv output_filename.csv

## Running Tests
Tests are run with given location-for-dev.csv file 

outputfile is named as out.csv

## Some Notes

I ran tests on rented instance of ubuntu 16.04 on google cloud platform 

screen shots are taken while running the code from terminal.

JSON format returned by MAPBOX services contains usually country,county,state,city,lat,long information contained as key,values

U could acces them as variable.json['country'],variable.json['county'] etc..

map_box.py file may show  error statements  if map_box_api returns null values for given lat,long or addresses

