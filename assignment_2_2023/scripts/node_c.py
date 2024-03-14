#!/usr/bin/env python3
"""
..module:: node_c
    :platform: Unix
    :synopsis: This script defines a ROS node that provides a service to get the distance and average velocity.
..moduleauthor:: Emanuele Bua Odetti

Subscribe to:
    /pos_vel
Publish to:
    None
Service:
    /info_service
Parameters:
    /des_pos_x
    /des_pos_y
    /window_size

This script defines a ROS node that provides a service to get the distance and average velocity.
It uses the custom service type Ave_pos_vel to receive requests and send responses with the distance and average velocity.
The InfoService class initializes the node and provides a callback function to handle the service requests.
The main() function initializes the ROS node and starts the service.
Note: This script assumes the presence of the necessary ROS packages and message types.
"""


import rospy
import math
from assignment_2_2023.msg import Vel
from assignment_2_2023.srv import Ave_pos_vel, Ave_pos_velResponse


# Define a class for the service
class InfoService:
    """
    InfoService class to provide a service to get the distance and average velocity.
    """

    def __init__(self):
        """
        Initialize the InfoService class.
        args:
            None
        returns:
            None
        """
        # Initialize class variables for the average velocity and distance
        self.average_vel_x = 0
        self.distance = 0

        # Initialize the node with the name 'info_service'
        rospy.init_node('info_service')
        rospy.loginfo("Info service node initialized")

        # Provide a service named 'info_service', using the custom service type Ave_pos_vel
        rospy.Service("info_service", Ave_pos_vel, self.get_values)
        # Subscribe to the '/pos_vel' topic, using the custom message type Vel
        rospy.Subscriber("/pos_vel", Vel, self.get_distance_and_averagevelocity)

    # Callback function for the subscriber
    def get_distance_and_averagevelocity(self, msg):
        """
        Callback function to handle the subscriber messages.
        args:
            msg: Vel
        returns:
            None
        """

        # Get the desired x and y positions from the parameter server
        des_x = rospy.get_param('/des_pos_x')
        des_y = rospy.get_param('/des_pos_y')

        # Get the window size for the velocity calculation from the parameter server
        velocity_window_size = rospy.get_param('/window_size')
        
        # Get the actual x and y positions from the message
        actual_x = msg.pos_x
        actual_y = msg.pos_y
        
        # Calculate the distance between the desired and actual positions
        des_coordinates = [des_x, des_y]
        actual_coordinates = [actual_x, actual_y]
        self.distance = math.dist(des_coordinates, actual_coordinates)

        # Calculate the average velocity
        if isinstance(msg.vel_x, list):
            vel_data = msg.vel_x[-velocity_window_size:]
        else:
            vel_data = [msg.vel_x]

        self.average_vel_x = sum(vel_data) / min(len(vel_data), velocity_window_size)


    # Callback function for the service
    def get_values(self, _):
        """
        Callback function to handle the service requests.
        args:
            _: Ave_pos_velRequest
        returns:
            Ave_pos_velResponse
        """      
        # Return a response with the distance and average velocity
        return Ave_pos_velResponse(self.distance, self.average_vel_x)		      

    # Function to keep the node running
    def spin(self):
        """
        Function to keep the node running.
        args:
            None
        returns:
            None
        """
        rospy.spin()

# Main function
if __name__ == "__main__":
    # Create an instance of the service class
    service = InfoService()
    dist_vel_service = rospy.ServiceProxy('info_service', Ave_pos_vel)

    while not rospy.is_shutdown():
            # Call the service
            response = dist_vel_service()
 
            rospy.loginfo(f"Service response:\n {response}")
 

    # Start the node
    service.spin()