import rospy
from std_msgs.msg import Int32MultiArray
import random

def talker():
    pub = rospy.Publisher('numbers', Int32MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	for x in range(10):
		n[] = random.randint(1,101)
        #rospy.loginfo(n)
        pub.publish(n)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

