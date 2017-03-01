# Bags for the Testing Phase

This directory contains a ROS bag of the robot operating in the arena. A square trajectory was performed, with 5 corners (P1, ... , P5) and obstacles georeferenced.

The file "coords.txt" contains the corners' coordinates, which can be seen below:

![Alt text](./square_coords.png?raw=true "Square trajectory with referenced corners and obstacles")

## Topics in the bag

Laser scanners
* /scan
* /scan_hokuyo

Wheel Odometry
* /RosAria/pose

IMU
* /imu/data
* /imu/mag

GPS
* /gps/fix

Transforms
* /tf

## Usage

Execute the launch file in directory /aux_files to run RVIZ along with the ROS bag. To run only the ROS bag, use the "rosbag play" command.