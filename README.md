# Hyperloop API

## Overview

### Project Manifesto
We all have a right to freedom and the pursuit of happiness.
Included in these rights is the ability to travel, to explore, to learn, grow and contribute all around the world.
Yet today, we are shackled by the modern day likes of the horse-drawn carriage,
traveling at painfully slow speeds - often through soul-destroying traffic - preventing us from truly reaching the destinations we seek.

Imagine being able to travel hundreds of miles in minutes instead of hours.
Each home and office building could have an underground station (similar to how we have garages today)
where you could board a pod-like autonomous vehicle that would whisk you away directly to your destination.
This would shrink our world.

[Hyperloop technology](http://www.spacex.com/sites/spacex/files/hyperloop_alpha-20130812.pdf) gives us a better path forward via a fast, weather-immune, and sustainable new form of transportation.

### How It Works
This application uses the following components to provide a theoretical Hyperloop API and documentation portal:

 * **Python 3.5+**
 * **Flask 1.0.\*:** Flask is a popular Python microframework that's great for performant APIs.
 * **Flask Blueprints:** [Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/#blueprints) are used to modularize the `api` and `docs` components.
 * **Marshmallow:** [Marshmallow](https://github.com/marshmallow-code/marshmallow) is used to define a [schema](https://github.com/dsposito/hyperloop-api/blob/master/models/station.py#L30) for each model. This is really useful for API validation, serialization and to [auto generate](https://github.com/dsposito/hyperloop-api/blob/master/docs/openapi.py#L12) an associated [YAML file](https://github.com/dsposito/hyperloop-api/blob/master/docs/static/openapi/schemas/station.yaml) for documentation.
 * **OpenAPI:** The [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) is used to [document the API](https://github.com/dsposito/hyperloop-api/blob/master/docs/static/openapi/spec.yaml).
 * **ReDoc:** The API documentation [YAML spec](https://github.com/dsposito/hyperloop-api/blob/master/docs/static/openapi/spec.yaml) is converted to JSON and [rendered](https://github.com/dsposito/hyperloop-api/blob/master/docs/templates/index.html#L10) by [ReDoc](https://github.com/Rebilly/ReDoc) - a React-based documentation portal UI.

## Setup
After cloning the repo, install its dependencies:

```
pip install -r requirements.txt
```

## Usage
Use the following to run the application locally:

```
FLASK_APP=app.py FLASK_ENV=development flask run
```

The documentation is now accessible via http://127.0.0.1:5000/docs and the API endpoints via http://127.0.0.1:5000/api.
