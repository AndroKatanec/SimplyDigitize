#!/usr/bin/env python3

from email.mime import base
from std_msgs.msg import Bool
import rospy
import Meshroom_CLI
import sys


class Finish_Listener:

	###Callback funckija u kojoj pratimo /finished
	def finish_callback(self,data):
		print("The node has finished its job? {}".format(data.data))
		if(data.data==True):
				binPath = rospy.get_param('~binPath', "/home")
				baseDir = rospy.get_param('~baseDir', "/home")
				imgDir = rospy.get_param('~imgDir', "/home")
				print("Launch meshroom with the images in bin/images")
				Meshroom_CLI.__run__(binPath, baseDir, imgDir)
				rospy.signal_shutdown("Success")
			


	###Inicijalizacija Subscribera
	def __init__(self):
		self.listener=rospy.Subscriber("finished",Bool,self.finish_callback)
		self.finished_listen=Bool()

	###Running 
	def run(self):
		print('finish_listener has started!')
		while not rospy.is_shutdown():
			rospy.spin()

	###Main function
if __name__=='__main__':
	rospy.init_node('finish_listener')
	try:
		finish=Finish_Listener()
		finish.run()
	except rospy.ROSInterruptException: pass
