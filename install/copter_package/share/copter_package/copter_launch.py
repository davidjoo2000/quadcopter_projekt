from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('move_up_height', default_value='2.0', description='Height for drone lift-off'),

        ExecuteProcess(
            cmd=['ign', 'gazebo', '-v', '4', '-r', 'kopter.sdf', '--render-engine', 'ogre'],
            output='screen'
        ),
        ExecuteProcess(
        cmd=['ros2','run ros_gz_bridge parameter_bridge /world/quadcopter/pose/info@geometry_msgs/msg/Pose@ignition.msgs.Pose'],
        output='screen',
        shell=True
),
        Node(
            package='copter_package',
            executable='copter_node',
            name='copter',
            output='screen',
            parameters=[{'move_up_height': LaunchConfiguration('move_up_height')}]
        )
    ])
