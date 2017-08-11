# Car Repair Shop Manager/Web
[![version](https://img.shields.io/badge/version-v_0.0.3-blue.svg)](https://h01000110.github.io/20161120/gerenciador-oficina-web)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/h01000110/gerenciador-oficina-web/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/h01000110/gerenciador-oficina-web.svg?branch=master)](https://travis-ci.org/h01000110/gerenciador-oficina-web)

## Framework
[Flask](http://flask.pocoo.org/)

## Installation
```bash
$ git clone https://github.com/h01000110/gerenciador-oficina-web.git  
$ pip3 install -r requirements.txt  
```

## Run
```bash
$ python3 run.py runserver
```

## Features
* Multi-View  
* Monthly Statistics  
* DB SQLite3  
* Customer Backup/pdf  
* Multi-Language - pt-BR/en-US  
* Client Map(internet required)  

## Client Map
Follow these steps to getting your Key: [GoogleMaps API](https://developers.google.com/maps/documentation/javascript/adding-a-google-map#step_3_get_an_api_key) and [Geocoding](https://developers.google.com/maps/documentation/javascript/geocoding#GetStarted);  
Paste your key in **app/templates/mapa.html**  
```html
<script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"></script>
```

## Changelog
en US [Car Repair Shop Manager/Web](https://h01000110.github.io/20170811/car-repair-shop-manager-web)  
pt BR [Gerenciador de Oficina/Web](https://h01000110.github.io/20161120/gerenciador-oficina-web)

## Resources
[Font Awesome by Dave Gandy](http://fontawesome.io)  
[Circle Icons by Nick Roach](https://www.elegantthemes.com/blog/freebie-of-the-week/beautiful-flat-icons-for-free)
