from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_project',
            executable='slam_node',
            output='screen'
        )
    ])
