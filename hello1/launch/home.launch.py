from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    urdf_file_name = 'urdf/hello1.urdf'

    urdf = os.path.join(
        get_package_share_directory('hello1'),
        urdf/hello1.urdf)

    return LaunchDescription([
        Node(
            package='gazebo_ros', executable='spawn_entity.py',
            arguments=['-entity', 'test2', '-file', urdf],
            output='screen'),
    ])

