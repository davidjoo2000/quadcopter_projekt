import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('move_up_height', default_value='2.0', description='Height for drone lift-off'),
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-v','4' ,'-r','quadcopter.sdf','--render-engine ogre'],
            output='screen'),
        Node(
            package='copter_package',
            executable='copter_node',
            name='copter',
            output='screen',
            parameters=[{'move_up_height': '2.0'}]
        )
    ])
