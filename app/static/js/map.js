function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: new google.maps.LatLng(-23.9629293,-46.2945767),
        mapTypeControl: false,
        streetViewControl: false,
        styles: [
          {elementType: 'geometry', stylers: [{color: '#ebe3cd'}]},
          {elementType: 'labels.text.fill', stylers: [{color: '#523735'}]},
          {elementType: 'labels.text.stroke', stylers: [{color: '#f5f1e6'}]},
          {featureType: 'administrative', elementType: 'geometry.stroke', stylers: [{color: '#c9b2a6'}]},
          {featureType: 'administrative.land_parcel', elementType: 'geometry.stroke', stylers: [{color: '#dcd2be'}]},
          {featureType: 'administrative.land_parcel', elementType: 'labels.text.fill', stylers: [{color: '#ae9e90'}]},
          {featureType: 'landscape.natural', elementType: 'geometry', stylers: [{color: '#dfd2ae'}]},
          {featureType: 'poi', stylers: [{visibility: 'off'}]},
          {featureType: 'road', elementType: 'geometry', stylers: [{color: '#f5f1e6'}]},
          {featureType: 'road.arterial', elementType: 'geometry', stylers: [{color: '#fdfcf8'}]},
          {featureType: 'road.highway', elementType: 'geometry', stylers: [{color: '#f8c967'}]},
          {featureType: 'road.highway', elementType: 'geometry.stroke', stylers: [{color: '#e9bc62'}]},
          {featureType: 'road.highway.controlled_access', elementType: 'geometry', stylers: [{color: '#e98d58'}]},
          {featureType: 'road.highway.controlled_access', elementType: 'geometry.stroke', stylers: [{color: '#db8555'}]},
          {featureType: 'road.local', elementType: 'labels.text.fill', stylers: [{color: '#806b63'}]},
          {featureType: 'transit.line', elementType: 'geometry', stylers: [{color: '#dfd2ae'}]},
          {featureType: 'transit.line', elementType: 'labels.text.fill', stylers: [{color: '#8f7d77'}]},
          {featureType: 'transit.line', elementType: 'labels.text.stroke', stylers: [{color: '#ebe3cd'}]},
          {featureType: 'transit.station', elementType: 'geometry', stylers: [{color: '#dfd2ae'}]},
          {featureType: 'water', elementType: 'geometry.fill', stylers: [{color: '#95a5a6'}]},
          {featureType: 'water', elementType: 'labels.text.fill', stylers: [{color: '#ecf0f1'}]}
        ]
    });

    var geocode;

    var http = new XMLHttpRequest();
    http.open('GET', '/marker', true);
    http.onreadystatechange = function() {
        if (http.readyState == XMLHttpRequest.DONE) {
            if (http.readyState == 4) {
                geocode = JSON.parse(http.responseText);
                geocode = geocode['dicio'];
                for (var i = 0; i < Object.keys(geocode).length; i++) {
                    var LatLng = {lat: geocode[i][0], lng: geocode[i][1]};
                    var marker = new google.maps.Marker({
                        position: LatLng,
                        map: map
                    });
                    marker.addListener('click', function() {
                        infowindow.open(map, marker);
                    });
                }
            }
        }
    }
    http.send(null);
}
