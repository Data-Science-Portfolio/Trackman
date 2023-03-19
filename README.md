# Trackman


Code written in Python 3.6.10

Separate requirments file not included as only built-in libraries were used like os, glob, json

Should probably run without any problem on any python version above 3.0

To run the script make sure to download/clone the repo and change the 'path' variable

-------------------------------------------------------------------------------------------------

Description of the solution approach taken:

A hierarchical relationship between the different tables needed to be discovered and illustrated.

Most parts of the files could be safely ignored, if I understood the assignment well only two
things were important in each file: the name of the file (=the name of a table) and a querry inside 
it that showed wether other tables were required to create it.

A straightforward solution could be to just scrape those querries split them by each 'join' string
and pick up the first word in each segment which is doable thanks to the SQL syntax.

After we have all tables and all the other tables that are needed for their creation (Note: some 
tables are not present in the files, especially the ones that ended up being parent nodes) it is 
a good idea to depending on the next step to load them all into a list or dictionary.

I went for a simple solution without too much hassle so the logic has not been organized into 
functions or classes, however it would be recommended to do that especially if the code is going 
to be reused or is going to be used with other pieces of logic.

The next step was to figure the logic to arrange the tables in a hierarchical order.
For the sake of simplicity I went with an o(n) time complexity solution that should be more
than appopriate for our current case. 

The visualization has been done in a simple way due to the lack of time but should satisfy
the basic requirments of the task. It's easily readable (json format) and should be easily
ingested by other applications as well. See example below:


      "base.games": {
            "crosscheck.games": {
                  "crosscheck.calibration_maintenance": {},
                  "games.autorecalibration": {}
            },
            "crosscheck.tags": {
                  "crosscheck.games": {
                        "crosscheck.calibration_maintenance": {},
                        "games.autorecalibration": {}
                  },
                  "games.latency": {},
                  "games.live_final": {},
                  "games.nulls": null,
                  "games.oem": {},
                  "games.vision": {},
                  "games.vision_oem": {},
                  "locations.latency": {},
                  "locations.vision_oem": {}
