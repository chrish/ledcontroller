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
        d.setAttribute("onclick", "postColorAsHex(this.style.backgroundColor)");

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

function postColor(rgbColorCode){
    var xhr = new XMLHttpRequest(); 
    xhr.open('POST', host + "/api/colors");
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    console.log("col=" + rgbColorCode);

    xhr.send("r=" + rgbColorCode[0] + "&g=" + rgbColorCode[1] + "&b=" + rgbColorCode[2]);
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



