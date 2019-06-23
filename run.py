import os, sys
import multiprocessing
from time import sleep
import uuid
import multiprocessing as mp
from tasks import ImageHandler
from flask import Flask, request 
import threading
from configparser import ConfigParser
import glob, random

queue = mp.Queue()
app = Flask(__name__) 
# pool = mp.Pool(mp.cpu_count())

config = ConfigParser()
config.readfp(open('gaius.config'))
time_sleep = config.getint('settings', 'time_sleep')  #in seconds

##Input Output Folder for images
output_dir=config.get('images', 'output_dir')
input_dir=config.get('images', 'input_dir')

image_1=config.get('images', 'image_1')
image_2=config.get('images', 'image_2')

OUTPUT_DIRECTORY=os.path.join(os.path.dirname(__file__), output_dir)
DATA_DIRECTORY=os.path.join(os.path.dirname(__file__), input_dir)


images=glob.glob(DATA_DIRECTORY+'*.png')
len_images=len(images)
# images_int=range(len_images)

print(images)

@app.route('/read_photo/<var>', methods=['GET'])
def read_photo(var):
	image=DATA_DIRECTORY+random.choice(images)
	add_task(image, 'image') 
	return 'Image of random choice read successfully '+str(image.split('/')[-1])


@app.route('/read_photo') 
def read_photo1():         
	'''read photo from a path, this can be changed to upload phot in further course'''
	image=DATA_DIRECTORY+image_1
	add_task(image, 'image')             
	return 'Image 1 Read Successfully..'

@app.route('/read_photo1')
def read_photo2():
	'''read another photo from path, to check multiple requests, further can be changed to upload video/audio'''
	image=DATA_DIRECTORY+image_2
	add_task(image, 'image')
	return 'Image 2 Read Successfully..'

def add_task(loc, _type):
	'''the requests are added in queue'''
	queue.put({'location':loc, 'type':_type})

def perform_tasks():
	'''The tasks are performed at the interval of every time_sleep seconds'''
	threading.Timer(time_sleep, perform_tasks).start()
	if not queue.empty():
		'''Performs the task in FIFO manner'''
		item=queue.get()
		if item['type']=='image': # checks the type of file. Further audio/video can be added.
			print(item['location'])
			img = ImageHandler(item['location'], OUTPUT_DIRECTORY)

def main():
	perform_tasks()
	'''Flask api call'''
	app.run(debug=True, port=5000) 


if __name__ == '__main__':
	 main()
    # get_word_counts(sys.argv[1])
