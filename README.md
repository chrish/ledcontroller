# ledcontroller

This is a simple controller for a LED strip. It comes with a basic frontend allowing you to select from predefined colors, or use sliders to mix RGB and Alpha. 

The frontend is pure HTML/JS/CSS, and the backend is a Flask-based API allowing for two operations: 
##GET /api/colors
This returns a list of predefined colors, used to populate the colorlist in the frontend. If you select one of these the sliders are updated to reflect the current color. 
##POST /api/colors
This uses the supplied a/r/g/b parameters and sets the new color and alpha. 

#Running
The frontend can be served using any webserver, the same goes for the backend assuming that the webserver supports Python/Flask. 

Running it in dev can be done via `flask run` and a .flaskenv file containing the following:
    FLASK_APP=ledcontrollerapi.py
    FLASK_ENV=development
    FLASK_RUN_HOST=<host ip>
    FLASK_RUN_PORT=5000 <-- Can be set to anything, but there is a reference to this port in the JS that also needs to be updated if it changes. 
