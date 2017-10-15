$(document).ready(function(){
    gettingJSON();
});
function gettingJSON(){
    
    $.getJSON("http://api.openweathermap.org/data/2.5/weather?id=5327684&units=imperial&APPID=833ddcc1f636c3c7e11c3ce7b999b6eb",function(result){
        document.getElementById("weather").innerHTML = "Berkeley, CA Weather: <br>"+ "Temp: " + result["main"]["temp"] + " &#8457" + "<br>" + "Humidity: " + result["main"]["humidity"] + " %" + "<br>" + "Status: " + result.weather[0].main;
    });
};
