var lon = document.getElementById("map").getAttribute("data-lon");
var lat = document.getElementById("map").getAttribute("data-lat");

window.onload = function () {
    var map = L.map('map').setView([lat, lon], 13);
    L.marker([lat, lon]).addTo(map);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);
    console.log("Map loaded");
}