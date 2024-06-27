#! /bin/python
'''
Convert geometry_msgs::Vector3Stamped to sensor_msgs::MagneticField.

Subscriptions:
    /imu/mag (Vector3Stamped)

Publications:
    /imu/mag_repacked (MagneticField)
'''


from geometry_msgs.msg import Vector3Stamped
from sensor_msgs.msg import MagneticField
import rospy

rospy.init_node("imu_mag_repacking")
pub = rospy.Publisher("/imu/mag_repacked", MagneticField, queue_size=1)

def callback(data):
    mag_msg = MagneticField()
    mag_msg.header = data.header
    mag_msg.magnetic_field = data.vector
    pub.publish(mag_msg)

sub = rospy.Subscriber("/imu/mag", Vector3Stamped, callback)

r = rospy.Rate(100)
while not rospy.is_shutdown():
    r.sleep()


