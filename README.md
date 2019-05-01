Crop Planting By Date
=====================

## Provides the answer to the question gardeners have:  if I want a crop in a certain date range, what can I plant today  

Source API:  http://growstuff.org/  Growstuff has a nice database that provides time to first producton and final production in median days.  

Coded using:
 * Python
 * JavaScript
 * Flask/Jinja
 * JQuery

Released onto AWS EC2 May 1, 2019

The API is accessed using Growstuff's crops.jason files.  With a maximum of 30 crops per json file, the program iterates files inspecting lists in dictionaries (objects) for matching data.

Growstuff uses a powerful method to grow and maintain its database using a kind of crowdsourcing.

Enhancements could include:
  * Copying down the database once per week to reduce load times
  * Some references to a locations air temperature, soil temperature and daylight hours.  This information is readily available given lat/lon.  I have not found an API that connects a specific crop to those location/season based parameters




