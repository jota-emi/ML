import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray

def callback(data):
    for x in range(10):
	if (x%2==0)
	   aux++;
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', aux)

def listener():


    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('Recnumbers', Int32[], callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

