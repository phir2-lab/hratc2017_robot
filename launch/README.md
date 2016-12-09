# HRATC 2017 Launch Files

Launch files for the HRATC 2017 robot

## Files
###trouble.launch
Full launch file. Runs the following packages (dependencies):
* RosAria
* um6
* nmea_navsat_driver
* sick_tim
* robot_localization
* tf
* metal_detector_msgs
* hokuyo_node


## Topic List

These are the topics available for the robot.

| Ros topic name                      | Ros topic type                        |
| ----------------------------------- | ------------------------------------- |
| /RosAria/battery_recharge_state     | std_msgs/Int8                         |
| /RosAria/battery_state_of_charge    | std_msgs/Float32                      |
| /RosAria/battery_voltage            | std_msgs/Float64                      |
| /RosAria/cmd_vel                    | geometry_msgs/Twist                   |
| /RosAria/motors_state               | std_msgs/Bool                         |
| /RosAria/parameter_descriptions     | dynamic_reconfigure/ConfigDescription |
| /RosAria/parameter_updates          | dynamic_reconfigure/Config            |
| /RosAria/pose                       | nav_msgs/Odometry                     |
| /diagnostics                        | diagnostic_msgs/DiagnosticArray       |
| /gps/fix                            | sensor_msgs/NavSatFix                 |
| /hokuyo_node/parameter_descriptions | dynamic_reconfigure/ConfigDescription |
| /hokuyo_node/parameter_updates      | dynamic_reconfigure/Config            |
| /imu/data                           | sensor_msgs/Imu                       |
| /imu/mag                            | geometry_msgs/Vector3Stamped          |
| /imu/rpy                            | geometry_msgs/Vector3Stamped          |
| /imu/temperature                    | std_msgs/Float32                      |
| /laser/parameter_descriptions       | dynamic_reconfigure/ConfigDescription |
| /laser/parameter_updates            | dynamic_reconfigure/Config            |
| /metal_detector                     | [metal_detector_msgs/Coil](https://raw.githubusercontent.com/lsa-pucrs/metal_detector_msgs/lsa-metal-detector/msg/Coil.msg)          |
| /odometry/filtered                  | nav_msgs/Odometry                     |
| /odometry/gps                       | nav_msgs/Odometry                     |
| /rosout                             | rosgraph_msgs/Log                     |
| /rosout_agg                         | rosgraph_msgs/Log                     |
| /scan                               | sensor_msgs/LaserScan                 |
| /scan_hokuyo                        | sensor_msgs/LaserScan                 |
| /tf                                 | tf2_msgs/TFMessage                    |
| /tf_static                          | tf2_msgs/TFMessage                    |
| /time_reference                     | sensor_msgs/TimeReference             |
| /vel                                | geometry_msgs/TwistStamped            |



## Nodes

The image below shows how the robot's nodes are connected via their topics in a graph (viewed using [rqt_graph](http://wiki.ros.org/rqt_graph)).
The circles represent the nodes, while the boxes represent the topics. The arrows' direction indicates whether a node publishes (outward) or
subscribes (inward) to the topic.

For the cases where a node has no connections, that node simply publishes data which is not (yet) used explicitly by any other node. For example,
the "/detector" node publishes to the topic "/metal_detector", but that topic is not subscribed by any other node. 

![alt text](./node_graph.png?raw=true "Nodes graph")