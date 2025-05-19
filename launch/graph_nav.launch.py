from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    bt_file = LaunchConfiguration('bt_file')

    return LaunchDescription([
        DeclareLaunchArgument(
            'bt_file',
            default_value=[
                '/home/colcon_ws/install/my_nav2_bt/share/my_nav2_bt/behavior_trees/graph_nav_with_stop.xml'
            ],
            description='Behavior Tree XML file'
        ),

        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[{
                'default_bt_xml_filename': bt_file,
            }]
        )
    ])
