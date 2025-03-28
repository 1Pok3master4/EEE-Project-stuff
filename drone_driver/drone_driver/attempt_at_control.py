#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose
from std_msgs.msg import Empty
from sensor_msgs.msg import Imu, Image


flag  = False
class DroneControl(Node):
    def __init__(self):
        super().__init__("drone_controller")
        #self.pose_subscription = self.create_subscription(Pose, "/simple_drone/gt_pose", self.pose_callback, 10)
        #self.imu_subscription = self.create_subscription(Imu, "/simple_drone/imu/out", self.acc_callback, 10)
        #self.vel_cmd = self.create_publisher(Twist, "/simple_drone/cmd_vel", 10)
        self.start = self.create_publisher(Empty, "/simple_drone/takeoff", 10)


        self.cam = self.create_subscription(Image, "/simple_drone/bottom/image_raw", self.cam_callback, 10)
        self.start.publish(Empty())
    

    def cam_callback(self, img: Image):
        global flag
        if flag:
            return
        
        print("asdjhajkfhsdjkfhsdjkf" + str(len(img.data)))
        print(img.encoding)
        print(img.step, img.width, img.height)
        flag = True
        
    def pose_callback(self, msg: Pose):
        pose_z = msg.position.z
        self.get_logger().info("pose abf" + str(pose_z))

        vel = Twist()
        vel.linear.z = 2.0
        self.vel_cmd.publish(vel)
       

    def acc_callback(self, msg: Imu):
        acc_z = msg.linear_acceleration.z
        self.get_logger().info("acc " + str(acc_z))
        
        

def main(args=None):
    rclpy.init(args=args)
    node = DroneControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

