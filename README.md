# REST API Resource management

## Introduction

This is an example based on the video https://www.youtube.com/watch?v=4T5Gnrmzjak (Jake Wright). The best way to learn is to try yourself. I wanted to build a simple REST API and came across this tutorial. What caught my eye is that not only you get to build a simple REST API but you also get to play a bit with docker (and compose) and with flask.

### What the REST API is intended for

If you don't want to go through the whole video, basically Jake wants to develop some home automation and to do so he creates a solution through a web page (flask) and some microservices (using docker). The idea is storing a set of home automation devices so you can list them, add new ones and delete existing ones. The main interest is the idea behind the solution.

## How it works

There will be 2 endpoints, /devices and /device/<identifier>. The first one will be used for collection management and the second one for individual device management.

Responses will be in JSON and will be in the form:

```json
{
	"status": "What has happened",
	"data": "data content about the request"
}
```

Quick reminder of http response codes (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

### Collection management options

**Request GET /device**

GET the complete list of current devices at the collection

**Response GET /devices**

Response code: *200 OK*

Response data will be:
```json
[{
	"identifier": "device_id",
	"description": "device_description",
	"type": "device_type",
	"address": "ip_address"
},
{
	"identifier": "device_id",
	"description": "device_description",
	"type": "device_type",
	"address": "ip_address"
}]
```
**Request POST /devices**

POST a new device into the collection

*Arguments for POST command:*
- `"identifier": string` (a unique string identified for the device)
- `"description": string` (a friendly name to describe the device)
- `"type": string` (a device type)
- `"address": string` (the ip address to connect to the device x.x.x.x)

If by any means an identifier already exists it will be **overwritten** with this new request

**Response POST /devices**

Response code: *201 Created*

Response data will be:
```json
{
	"identifier": "device_id",
	"description": "device_description",
	"type": "device_type",
	"address": "ip_address"
}
```

### Device management

**Request GET /device/<identifier>**

GET the data from a specific device

**Response GET /device/<identifier>**

Response code: *200 OK* (if device is found in the collection)
Response code: *404 Not found* (if device is not found in the collection)

Response data will be:
```json
{
	"identifier": "device_id",
	"description": "device_description",
	"type": "device_type",
	"address": "ip_address"
}
```
**Request DELETE /device/<identifier>**

DELETE the specified device

**Response DELETE /device/<identifier>**

Response code: *204 No content* (when device successfully deleted)
Response code: *404 Not found* (if device is not found in the collection)

### References

[Original video](https://www.youtube.com/watch?v=4T5Gnrmzjak)
[Markdown python library](https://python-markdown.github.io/sitemap.html)
[Flask database access example](http://flask.pocoo.org/docs/0.12/appcontext/)
[Docker compose](https://docs.docker.com/compose/gettingstarted/)
[Docker Python container](https://hub.docker.com/_/python/)
[Flask](http://flask.pocoo.org/)
[Shelve](https://docs.python.org/3/library/shelve.html)
[Flask RESTFul extension](http://flask-restful.readthedocs.io/en/latest/)