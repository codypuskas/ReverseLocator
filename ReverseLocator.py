#Creator: Cody Puskas
import sys
import os
from geopy.geocoders import Nominatim

locator = Nominatim()

while True:
    try:
        #coordinates = str(raw_input("Enter the coordinates you would like to look up: "))
        coordinates = "39.7589478,-84.1916068" #Dayton Coordinates
        print coordinates
        break
    except ValueError:
        print "Invalid input"

location = locator.reverse(coordinates)

if location is None:
    print "Address does not exist"
    input()

else:
    print "Location Found"
    print location.address
    input()