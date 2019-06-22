import os,sys, time
from PIL import Image
from multiprocessing import Process

# huey = RedisHuey('my-app', host='redis.myapp.com')

class ImageHandler:

	def __init__(self, image, output_dir):

		self.output_dir=output_dir
		self.image=image
		self.im = Image.open(self.image)
		self.width, self.height = self.im.size
		self.image_name=self.image.split("/")[-1]

		self.fns=[self.check_original_resolution(), self.convert_mid_resolution(), self.convert_low_resolution()]

		self.runInParallel()

	def runInParallel(self):
		'''Function responsible to run processes in parallel'''
		proc = []
		for fn in self.fns:
			p = Process(target=fn)
			p.start()
			proc.append(p)
		for p in proc:
			p.join()


	def check_original_resolution(self):
		'''saves the image in output_directory in original form'''
		new_image_name=str(self.image_name.split(".")[0])+"_orig_."+str(self.image_name.split(".")[-1])
		print(self.output_dir+new_image_name)
		self.im.save(self.output_dir+new_image_name)
		time.sleep(5)

	def convert_mid_resolution(self):
		'''saves the image in output_directory in medium resolution'''
		new_image = self.im.resize((int(self.width/2), int(self.height/2)))
		new_image_name=str(self.image_name.split(".")[0])+"_mid_"+str(self.width/2)+"."+str(self.image_name.split(".")[-1])  #Can further be modified for better nomenclature
		new_image.save(self.output_dir+new_image_name)
		time.sleep(10)

	def convert_low_resolution(self):
		'''saves the image in output_directory in low resolution'''
		new_image = self.im.resize((int(self.width/4), int(self.height/4)))
		new_image_name=str(self.image_name.split(".")[0])+"_low_"+str(self.width/4)+"."+str(self.image_name.split(".")[-1]) #Can further be modified for better nomenclature
		new_image.save(self.output_dir+new_image_name)
		time.sleep(10)

