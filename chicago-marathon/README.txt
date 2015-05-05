Upfront Apology if this is too much
===================================
So sorry if I overstepped by doing to much! I just got excited and wanted to help. I've tried to comment heavily so you can understand what I did and edit it. Or just don't use it if you want to figure it out on your own!

Contents of folder
==================
- test.html: Most important, html and javascript that emulates what you wanted to show group.
- route.xml: Route information extracted from Google map you sent me
- route.json: Essential route information parsed out from xml document and put in JSON form
- compose-json.py: Python script I wrote to parse route data from xml file

To view **********
=======
Because of cross-origin restrictions, you need to run a server to grab the JSON file. Therefore type the following command in terminal in this directory

python -m SimpleHTTPServer

Then navigate to http://localhost:8000/test.html


Details
=======
test.html is where all the magic happens. It should be similar to what you have, but I added some extra functionality, most notably that it draws out each individual segment of the race course so you can manipulate them separately (look for routeSegments array). I also added comments for how to style the map if so desired, as well as put a loop (interval) that updates the line widths in the map to emulate/test the idea that changing widths are a good vizualization for changing race conditions. I also included some legend code. The most notable thing left out is a click handler for clicking on the paths- I figure you can work on that if you want to (feel free to ask for help).

route.json is where the route information is stored. It contains the starting and ending latitude and longitude coordinates for each segment of the route.

route.xml is the full data taken from the map you got from your contact

compose-json.py is the script I wrote to pull out the necessary coordinates into the json file. This is also commented if you want to see how it works. To run it just type "python compose-json.py", but know that this will overwrite the current route.json.