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

10. Dockerizing our flask app:
https://docs.docker.com/desktop/install/mac-install/

HOMEBREW_NO_AUTO_UPDATE=1 brew install --cask docker 


```subl Dockerfile``` and enter its contents..

```export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"```

Note: Need the desktop docker running for the next step 

```docker build --tag python-docker .```

```docker images``` #see the docker image we just created

```docker run -p 3334:3334 -d python-docker ``` #the port here should be the same as in main.py

Goto localhost:3334 and verify!

### Extra useful docker commands:
docker ps -a #lists all running containers

docker stop <container_id>

docker rm <container_id>



### Sources:
- https://www.topcoder.com/thrive/articles/build-microservice-architecture-msa-rest-api-using-the-using-flask 
- https://blog.logrocket.com/build-deploy-flask-app-using-docker/ 
- https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ 
- 
