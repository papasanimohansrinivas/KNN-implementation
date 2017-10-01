--- NOTES - REMOVE THIS SECTION  
This document should be provided with your submission instead of any .txt or .doc files.

Please rename this doc to "README.md" and provide it with your submission.

If you need to use imagery, create a `docs` folder, put your screenshots or images in there, and link them like this:

<img src="docs/img.jpg" />

--- END NOTES ---

# Geofencing Validator 
Deployment Guide

### Checks whether address is appropriate for given lat,long

## Prerequisites
1. Python 3
  1. geocoder module
2.Mapbox apikey for their geocoding services.
  2. api_key for map_box_key = 


## Local Deployment

Py -3 geocodingValidator_.py location-for-dev.csv output_filename.csv


## Production Build and Installation
How to build the application for upload to a server
```bash
Note: assume it is a dedicated server not AWS or Heroku.
```

### Manual Deployment Notes

apikeys for map_box :- 

assign one of those apikeys  to map_box_key variable in map_box.py file

"pk.eyJ1IjoibW9oYW4wMCIsImEiOiJjajg0bDdudDYwOHM1MndwZmNjenp1dTduIn0.LxknjhXAQ_1n98amoXAANw"

"pk.eyJ1IjoibW9oYW4wMCIsImEiOiJjajgzZDZ6bGo3ZHdzMzNycjdlcnZqeHY4In0.caVuIsMV5qClz4zHIKvFIg"


## Running Tests

## Notes
