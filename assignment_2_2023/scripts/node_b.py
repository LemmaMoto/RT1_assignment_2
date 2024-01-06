#!/usr/bin/env python3

import rospy
from assignment_2_2023.msg import Vel
from assignment_2_2023.srv import Input, InputResponse

class LastTargetService:
    def __init__(self):
        self.last_des_x = 0
        self.last_des_y = 0

        rospy.init_node('last_target_service')
        rospy.loginfo("Last target node initialized")

        rospy.Subscriber("/pos_vel", Vel, self.get_last_target)
        rospy.Service('input', Input, self.result_callback)

    def get_last_target(self, _):
        self.last_des_x = rospy.get_param('/des_pos_x')
        self.last_des_y = rospy.get_param('/des_pos_y')

    def result_callback(self, _):
        response = InputResponse()
        response.input_x = self.last_des_x
        response.input_y = self.last_des_y

        return response

    def spin(self):
        rospy.spin()

if __name__ == "__main__":
    service = LastTargetService()
    service.spin()