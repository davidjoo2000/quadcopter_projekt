import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gazebo',
            name='gazebo',
            output='screen',
            arguments=['-s', 'libgazebo_ros_factory.so']
        ),
        Node(
            package='my_gazebo_control_pkg',
            executable='gazebo_control_node',
            name='gazebo_control_node',
            output='screen',
            parameters=[{'y_position': 1.0}]
        )
    ])
