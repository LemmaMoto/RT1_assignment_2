#!/usr/bin/env python3

import rospy
import math
from assignment_2_2023.msg import Vel
from assignment_2_2023.srv import Ave_pos_vel, Ave_pos_velResponse

def get_distance_and_averagevelocity(msg):
    
    global success, average_vel_x, distance

    des_x = rospy.get_param('/des_pos_x')
    des_y = rospy.get_param('/des_pos_y')

    velocity_window_size = rospy.get_param('/window_size')
    
    actual_x = msg.pos_x
    actual_y = msg.pos_y
    
    des_coordinates = [des_x, des_y]
    actual_coordinates = [actual_x, actual_y]
    distance = math.dist(des_coordinates, actual_coordinates)

    if isinstance(msg.vel_x, list):
        vel_data = msg.vel_x[-velocity_window_size:]
    else:
        vel_data = [msg.vel_x]

    average_vel_x = sum(vel_data) / min(len(vel_data), velocity_window_size)

    print("Distance= ", distance, "Average velocity = ", average_vel_x)

        
def get_values(_):      
    global average_vel_x, distance
    
    print("Distance= ", distance, "Average velocity = ", average_vel_x)

    
    return Ave_pos_velResponse(distance, average_vel_x)		      

def info_service_main():
    global velocity_window_size

    rospy.init_node('info_service')
    rospy.loginfo("Info service node initialized")
    
    rospy.Service("info_service", Ave_pos_vel, get_values)

    rospy.Subscriber("/pos_vel", Vel, get_distance_and_averagevelocity)

    rospy.spin()

if __name__ == "__main__":
    info_service_main()