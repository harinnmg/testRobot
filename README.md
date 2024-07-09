# testRobot
Hello!!, this is a simple differential drive robot designed in solidworks and the exported to URDF to work in ROS Noetic Environment. The design is inspired from following video with some changes: 
https://youtu.be/PIxHKowQ-wc?si=v8nfEqY__DkjLwTz

The robot has been simulated in Gazebo with additional plugins. SLAM has been implemented using gmapping package, and the autonomous navigation has implemented.
For ROS2 add the following line in terminal before launching 
```
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:/path/to/libgazebo_ros_api_plugin.so
```
