import LedArray

'''
    So... 

    dotstar keeps track of initial configuration. This is the defaults which are loaded into the webapp. 
    The webapp keeps track of state, and requests changes to individually named arrays as needed. 

    When this happens the LedArray is initialized, and the changes are made as required if the lib supports initialization 
    without changing any existing shit. If things have to change during init, we do so. 

    
'''
from flask import Flask
app = Flask(__name__)



@app.route('/ctrl/<segmentidx>/<color>/<intensity>')
def ctrl_light():
    