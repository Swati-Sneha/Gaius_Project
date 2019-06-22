# GAIUS PROJECT

Gaius_Project is a prototype framework to handle multiple HTTP requests from users and return response as fast as possible. The processing of the incoming requests are handled in a seperate thread by the Python (3.6.7) Script.

## run.py
- handles the incoming HTTP request using Flask API
- recieves and enqueues the requests in multiprocessing queue
- At regular intervals (here, 15 sec), a thread is called to process the request without interrupting the HTTP request
- run command
```
$ python run.py
```

## tasks.py
- ImageHandler Class, that creates all the fidelity level of images (original, mid, low) as soon as object of it is created, during read/upload of photo. 

## gaius.config
  - the additional parameters to be passed are stored in config file
  
## requirements.txt
- required packages for the script to run 
#### Installation
```sh
$ pip install -r requirements.txt
```
## data
- Folder to contain input media

## output
- Folder to contain processed result of HTTP request

