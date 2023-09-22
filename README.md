# Movie Recommendations

*Recommends top 10 movies based on user reviews*


## Installation

clone:
```
$ git clone https://github.com/cmu-seai/group-project-s23-strangers.git
$ cd movies
$ git checkout tanya_flask
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```

## Run
```
$ flask run 
* Running on http://17645-team14.isri.cmu.edu:8082 OR http://128.2.205.115:8082
```
Checking movie recommendations:
http://17645-team14.isri.cmu.edu:8082/recommend/userid - This will generate movie recommendations for this user

Example: http://17645-team14.isri.cmu.edu:8082/recommend/679775


#Kafka to csv Pipeline

Call getData function to pull data into the Data folder.  
It creates/updates three csvs and one file  
 - Recommendations to users  
 - mpg by users  
 - ratings by users  
 - File with current start kafka stream  

It checks if the stream is in bad by checking if format of csv follows   
 - mpgStr = "GET /data/m/"  
 - rateStr = "GET /rate/"  
 - recStr = "recommendation request 17645-team14.isri.cmu.edu:8082, status 200, result:"  

It also checks if the user id is [1,1000000] inclusive.  

This function needs the port to be available  
To connect to Kafka Broker Server with port forwarding by replacing   
    - [IP] with the ipaddress (Ex: 0.0.0.0)  
    - [port] with port number (Ex: 9092)  
$ssh -o ServerAliveInterval=60 -L <port>:localhost:<port> tunnel@<IP> -NTf  

To kill connection at port after :  
$lsof -ti:[port] | xargs kill -9  

It needs Keys.py to have the correct information (substitute [topic] and [port] with the correct number):  
TOPIC = "[topic]"  
LOCAlPORT = "localhost:[port]"  

Setup: it needs kafka-python, pytest, pytest-cov  
$python -m pip install kafka-python  
$python -m pip install pytest  
$python -m pip install pytest-cov  