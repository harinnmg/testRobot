import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess


def generate_launch_description():
    # Get the package share directory
    pkg_share = get_package_share_directory('hello1')

    # Define the path to the world file
    world_file_name = 'hello1.world'
    world_path = os.path.join(pkg_share, 'world', world_file_name)

    # Define the path to the URDF file
    urdf_file_name = 'hello1.urdf'
    urdf_path = os.path.join(pkg_share, 'urdf', urdf_file_name)

    return LaunchDescription([
        # Start Gazebo server with the world file

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gzserver.launch.py')]),
            launch_arguments={'world': world_path}.items(),
        ),
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        # Start Gazebo client
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gzclient.launch.py')]),
        ),

        Node(
             package='joint_state_publisher',
             executable='joint_state_publisher',
             name='joint_state_publisher',
             ),
 
        # Publish the URDF to the robot_description topic
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            arguments=[urdf_path]
        ),
        
        # Spawn the robot entity
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=['-entity', 'test2', '-topic', 'robot_description', "-x", "0.0", "-y", "0.0", "-z", "0.0"],
            output="screen"
        )
    ])

if __name__ == '__main__':
    generate_launch_description()

