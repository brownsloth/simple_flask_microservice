### Steps:

We are creating an API as a flask application accepting data from a JSON file. 

1. ```python3 -m venv venv```
2. ```source venv/bin/activate```
3. ```pip3 install flask```
4. Install python package to develop flask-based api quickly ```pip3 install flask-restx```
5. Need a database .json file for our API to interact with ```subl movies.json```
6. ```subl main.py``` and copy the following imports
```python
from flask
import Flask, Response, request, abort
// import json dependencies
from flask
import JSON, jsonify
from flask_restx
import Api, Resource, fields
```
7. Set the API entry point, load data, create data model 
8. Run the application ```python main.py```
9. Freeze requirements ```pip3 freeze > requirements.txt```



### Sources:
- https://www.topcoder.com/thrive/articles/build-microservice-architecture-msa-rest-api-using-the-using-flask 
