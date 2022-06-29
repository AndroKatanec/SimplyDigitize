#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
# Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError
from goprocam import GoProCamera, constants

bridge=CvBridge()
counter = 0


gopro = GoProCamera.GoPro(constants.gpcontrol)

def ready_callback(msg):
    ready_msg = msg.data
    if ready_msg == True:
        rospy.loginfo('Spremam sliku...')
        try:
            gopro.downloadLastMedia(gopro.take_photo()) #slikanje slike
        except rospy.ROSInterruptException:
            pass
        
        
ready=rospy.Subscriber('/ready',Bool, ready_callback)

if __name__ == '__main__':
    rospy.init_node('opencv_proba',anonymous=True)
    while not rospy.is_shutdown():
        rospy.spin()
