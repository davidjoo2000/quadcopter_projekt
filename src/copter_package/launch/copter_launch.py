import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-v','4' ,'-r','quadcopter.sdf','--render-engine ogre'],
            output='screen'),
        Node(
            package='copter_package',
            executable='copter_node',
            name='copter',
            output='screen',
            parameters=[{'y':'0'}]
        )
    ])
