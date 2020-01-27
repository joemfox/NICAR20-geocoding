# NICAR20: Geocoding
Materials for a class on programmatic geocoding for NICAR 2020

Sometimes, you need more firepower than what you can get using online geocoding tools. This session will show you how to access the U.S. Census geocoding API to retrieve location data using the Python programming language.

This session is good for people whose geocoding needs have outgrown point-and-click tools and have basic experience writing Python.

# What is geocoding?
- input: address
- output: geographic data (latitude and longitude)

# What will we do in this session?
- Write a python script to get location data for a csv of 1,000 addresses using the U.S. Census Geocoder

# Examine your data
- How many addresses do you have?
- Are the addresses in one field or split into many (number, street, city, state, zip, etc.)?
- How clean is the data?

### Examining our data:
- We have 1,000 addresses (this is a subset of an 82,000-address file)
- The addresses are in one field
- Addresses appear properly formatted but many of them have PO Box or the name of a shopping center in front of them, which will cause trouble.

# Choose a geocoding service
- There are dozens of options!
- Services vary in:
  - Price
  - Rate limits
  - Setup
  - Web interface vs. programmatic API
  - Accuracy

### Our choice: Census Geocoder
- For this session, we'll use the [Census Geocoder](https://geocoding.geo.census.gov/geocoder/). It's a good place to start for a few reasons:
  - It's free!
  - No rate limits for single requests
  - Batch rate limits are pretty high (10,000 lines per request)
  - No API key required
  - It has a web interface that will help us do some preliminary testing
  - Good documentation

# Getting started
- We'll test a few lines using the web interface to make the right decisions about which API endpoints to use
- The [Address](https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?form) and [Address Batch](https://geocoding.geo.census.gov/geocoder/locations/addressbatch?form) functions require addresses to be split into different fields, and ours aren't.
- We will start with the [One-line Address](https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?form) function.
- Plug in a few of the addresses from the csv. Does the web interface return a result? Does it look correct? What about when we try one of the PO Boxes?

## Side note: Geographies vs. Locations
- Use the [Geographies](https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress?form) endpoints if you need to get geographic entities that contain your address, too. For example, you might want to know what census block or county your address is in.
- If you just need the location of the address, use the [Locations](https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?form) search.

# Writing some code
- Now that we know (most of) our addresses will work with the one-line address search, let's implement that in code.

- set up request URL and parameters
- csv.reader
- loop through rows, make request for each
- limit to first few rows for testing
- view url, click on a few
- when those are working, view json
- census returns json even if there are no matches, so we need to check whether there is a match in `addressMatches`
- if there is a match, let's print it and see what's in it
- we need the `coordinates` dict
- latitude and longitude are returned as `y` and `x`
- add a count for addresses that don't match
- enter blank values for lat/lon so we can still write a proper csv (and come back to those later)
- create a csvwriter and output file
- enter headers + new column names
- write each row as we get it


things to improve
- speed
- quit/resume
- enable batching
- parse addresses to remove junk (usaddress)


batching
- more complicated (can't just do url parameters)
- have to upload a file
- let's parse first
- one thing you would have to do is write original file with new id field to join new addresses to original data