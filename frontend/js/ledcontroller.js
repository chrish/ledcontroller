var host = "http://192.168.0.115:5000"

function printColorSet(colors){
    var ct = document.getElementById("colors");
    for(let prop in colors){
        //var hexcolor = "#" + colors[prop].toString(16);
        var hexcolor = "#" + colors[prop].toString(16).padStart(6, "0");
        var d = document.createElement("div");
        var dspan = document.createElement("span");
        var tn = document.createTextNode(hexcolor);
        var tncbr = document.createElement("br");
        var tnc = document.createTextNode(prop);
        dspan.appendChild(tn);
        dspan.appendChild(tncbr);
        dspan.appendChild(tnc);
        d.appendChild(dspan);   
        
        d.setAttribute("style", "background-color: " + hexcolor);
        d.setAttribute("class", "colorbox");
        d.setAttribute("onclick", "setColorSlider(this.style.backgroundColor)");

        ct.appendChild(d);
    }
}

function getDefaultColorsRequest(){
    var xhr = new XMLHttpRequest();

    xhr.onload = function() {
        if( xhr.status >= 200 && xhr.status <= 300){
            printColorSet(xhr.response)
        } else {
            console.log(xhr)
        }
    }

    return xhr;
}

function setColorSlider(col){
    rgb = col.replace(/[^\d,]/g, '').split(',');
    var r = parseInt(rgb[0]);
    var g = parseInt(rgb[1]);
    var b = parseInt(rgb[2]);


    document.getElementById("sr").value = r;
    document.getElementById("sg").value = g;
    document.getElementById("sb").value = b;

    postColor([r,g,b]);
}

function componentToHex(c) {
    var hex = parseInt(c).toString(16);
    var ret = hex.length == 1 ? "0" + hex : hex;
    console.log("Conv col: " + ret);
    
    return ret;
  }

function updateCurrentColor(col){
    var hex = "#" + componentToHex(col[0]) + componentToHex(col[1]) + componentToHex(col[2]);
    
    console.log("Hexcol: " + hex);

    var cc = document.getElementById("activecolor");
    cc.innerHTML = hex;
    cc.setAttribute("style", "background-color: " + hex);
}


function postColor(rgbColorCode){
    var intensity = document.getElementById("sa").value;

    console.log("intensity: " + intensity);
    updateCurrentColor(rgbColorCode);
    var xhr = new XMLHttpRequest(); 
    xhr.open('POST', host + "/api/colors");
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.send("a=" + intensity + "&r=" + rgbColorCode[0] + "&g=" + rgbColorCode[1] + "&b=" + rgbColorCode[2]);
}

function postColorAsHex(hexColorCode){
    var rgb = hexColorCode.replace(/[^\d,]/g, '').split(',');
    postColor(rgb);
}

function init(){
    var rq = getDefaultColorsRequest();
    rq.open("GET", host + "/api/colors");
    rq.responseType = "json";
    rq.send();
}

function sliderChange(){
    var r = document.getElementById("sr").value;
    var g = document.getElementById("sg").value;
    var b = document.getElementById("sb").value;

    console.log("Changing color to rgb(" + r + ", " + g + ", " + b + ")")

    postColor([r,g,b]);
}



