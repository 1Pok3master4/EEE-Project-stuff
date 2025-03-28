import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mocha1410/ros2_ws/src/ROS2-Drone-Basic-Course-for-Beginners/drone_driver/install/drone_driver'
