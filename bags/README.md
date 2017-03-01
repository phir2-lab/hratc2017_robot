# Bags for the Testing Phase

This directory contains a ROS bag of the robot operating in the arena. A square trajectory was performed, with 5 corners georeferrenced (P1, ... , P5).

The file "coords.txt" contains the corners' coordinates, which can be seen below:

![Alt text](./square_coords.png?raw=true "Square trajectory with referenced corners and obstacles")

## Topics in the bag

1. Laser scanners
..* /scan
..* /scan_hokuyo

2. Wheel Odometry
..* /RosAria/pose

3. IMU
..* /imu/data
..* /imu/mag

4. GPS
..* /gps/fix

5. Transforms
..* /tf

## Usage

Execute the launch file in directory /aux_files to run RVIZ along with the ROS bag. To run only the ROS bag, use the "rosbag play" command.