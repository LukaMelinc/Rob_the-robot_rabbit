#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import time

def main():
    rospy.init_node('my_rob_demo', anonymous=True)

    # Publishers for each joint controller
    publishers = {
        "shoulder_left_front": rospy.Publisher('rob/shoulder_left_front_position_controller/command', Float64, queue_size=1),
        "front_left_joint": rospy.Publisher('rob/front_left_joint_position_controller/command', Float64, queue_size=1),
        "shoulder_right_front": rospy.Publisher('rob/shoulder_right_front_position_controller/command', Float64, queue_size=1),
        "front_right_joint": rospy.Publisher('rob/front_right_joint_position_controller/command', Float64, queue_size=1),
        "shoulder_left_back": rospy.Publisher('rob/shoulder_left_back_position_controller/command', Float64, queue_size=1),
        "back_left_joint": rospy.Publisher('rob/back_left_joint_position_controller/command', Float64, queue_size=1),
        "shoulder_right_back": rospy.Publisher('rob/shoulder_right_back_position_controller/command', Float64, queue_size=1),
        "back_right_joint": rospy.Publisher('rob/back_right_joint_position_controller/command', Float64, queue_size=1)
    }
    initan = 0.52

    #WALKING LOOP

    poses = [
    {
            # move front legs state
            "angles": {
                "shoulder_left_front": 4.9,
                "front_left_joint": initan - 1.4,
                "shoulder_right_front": 4.9,
                "front_right_joint": initan - 1.4,
                "shoulder_left_back": -0.92,
                "back_left_joint": initan - 1.4,
                "shoulder_right_back": -0.92,
                "back_right_joint": initan - 1.4
            },
            "timeout": 0.9  # Another custom time
        },
        {
            # move front legs state
            "angles": {
                "shoulder_left_front": 4.9,
                "front_left_joint": initan - 1.4,
                "shoulder_right_front": 4.9,
                "front_right_joint": initan - 1.4,
                "shoulder_left_back": 0.48,
                "back_left_joint": initan - 1.55,
                "shoulder_right_back": 0.48,
                "back_right_joint": initan - 1.55
            },
            "timeout": 0.9  # Another custom time
        },
         {
            # move front legs state
            "angles": {
                "shoulder_left_front": 4.9,
                "front_left_joint": initan - 3,
                "shoulder_right_front": 4.9,
                "front_right_joint": initan - 3,
                "shoulder_left_back": 0.48,
                "back_left_joint": initan - 1.55,
                "shoulder_right_back": 0.48,
                "back_right_joint": initan - 1.55
            },
            "timeout": 0.9  # Another custom time
        },
        {
            # move front legs state
            "angles": {
                "shoulder_left_front": 4.9,
                "front_left_joint": initan - 1.4,
                "shoulder_right_front": 4.9,
                "front_right_joint": initan - 1.4,
                "shoulder_left_back": -0.92,
                "back_left_joint": initan - 1.4,
                "shoulder_right_back": -0.92,
                "back_right_joint": initan - 1.4
            },
            "timeout": 0.9  # Another custom time
        }

    ]

    # Give the publishers some time to connect
    rospy.sleep(1.0)
#
    # Iterate through poses
    for pose in poses:
        angles = pose["angles"]
        timeout = pose["timeout"]


        rospy.loginfo(f"Publishing pose: {angles}")
        for joint, angle in angles.items():
            publishers[joint].publish(angle)


        # Wait for the robot to reach the pose before moving to the next
        rospy.loginfo(f"Waiting for {timeout} seconds...")
        rospy.sleep(timeout)

    rospy.loginfo("All poses published to the robot controllers.")



if __name__ == '__main__':
    main()