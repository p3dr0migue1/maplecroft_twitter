// Initialise the map and set default values
var map = L.map('map').setView([39.123919, 35.448239], 3);

L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v9/tiles/{id}/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMa33p</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 14,
    id: '256',
    accessToken: 'pk.eyJ1IjoibWF4ZzIwMyIsImEiOiJjaXRhMnM1dncwMDU5MnhwaGxzenV1M3ExIn0.dHwySLGJmJairTuzOSn49Q'
}).addTo(map);

$.getJSON("/static/js/geo_data.json", function(data) {
    L.geoJson(data).addTo(map);
})
