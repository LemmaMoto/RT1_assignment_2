#!/usr/bin/env python3
"""
..module:: node_b
    :platform: Unix
    :synopsis: This script defines a ROS node that provides a service to get the last target position.
..moduleauthor:: Emanuele Bua Odetti

Subscribe to:
    None
Publish to:
    None
Service:
    /input
Parameters: 
    /des_pos_x
    /des_pos_y

This script defines a ROS node that provides a service to get the last target position.
It uses the custom service type Input to receive requests and send responses with the last desired x and y positions.
The LastTargetService class initializes
the node and provides a callback function to handle the service requests.
The main() function initializes the ROS node and starts the service.
Note: This script assumes the presence of the necessary ROS packages and message types.
"""


import rospy
from assignment_2_2023.msg import Vel
from assignment_2_2023.srv import Input, InputResponse

# Define a class for the service
class LastTargetService:
    """
    LastTargetService class to provide a service to get the last target position.
    """

    def __init__(self):
        """
        Initialize the LastTargetService class.
        args:
            None
        returns:
            None
        """

        # Initialize class variables for the last desired x and y positions
        self.last_des_x = 0
        self.last_des_y = 0

        # Initialize the node with the name 'last_target_service'
        rospy.init_node('last_target_service')
        rospy.loginfo("Last target node initialized")

        # Provide a service named 'input', using the custom service type Input
        rospy.Service('input', Input, self.result_callback)

    # Callback function for the service
    def result_callback(self, _):
        """
        Callback function to handle the service requests.
        args:
            _ : Input request
        returns:
            response : Input response
        """

        # Create a response message
        response = InputResponse()
        # Set the x and y inputs in the response to the last desired positions
        self.last_des_x = rospy.get_param('/des_pos_x')
        self.last_des_y = rospy.get_param('/des_pos_y')
        response.input_x = self.last_des_x
        response.input_y = self.last_des_y

        # Return the response
        return response

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
    service = LastTargetService()
    # Start the node
    service.spin()