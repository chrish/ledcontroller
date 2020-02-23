import sys
from app import app
from flask import request

sys.path.append('../src/ledcontroller/')
import ledcontroller.LedArray

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

@app.route('/api/colors', methods = ['GET', 'POST'])
def colors():
    if request.method == "GET":
        la = ledcontroller.LedArray.LedArray()
        return la.GetColors()
    elif request.method =="POST":
        a = request.values.get("a")
        r = request.values.get("r")
        g = request.values.get("g")
        b = request.values.get("b")
        rgb = (r, g, b)
        
        col = "0x" + rgb_to_hex((int(r),int(g),int(b)))
 
        la = ledcontroller.LedArray.LedArray()
        la.SetIntensity(int(a)/100)
        la.SetSolidColor(col)
        return col
        

    