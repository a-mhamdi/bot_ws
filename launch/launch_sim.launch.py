import os

from ament_index_python.packages import get_package_share_directory

from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'roue_bot'
    pkg_share = get_package_share_directory(package_name)

    pkg_gazebo_ros = FindPackageShare(package='gazebo_ros').find('gazebo_ros')

    bot_urdf_file = os.path.join(pkg_share, 'urdf', 'roue_bot.urdf.xacro')
    rviz_config_file = os.path.join(pkg_share, 'config', 'sim.rviz')

    # Create the launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # Declare the launch arguments
    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')

    # Start Gazebo server
    start_gazebo_server_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
        launch_arguments={'world': os.path.join(
            pkg_share, 'worlds', 'house.world')}.items()
    )

    start_gazebo_client_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            pkg_gazebo_ros, 'launch', 'gzclient.launch.py')),
    )

    # Spawn robot
    spawn_entity_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'roue_bot',
            '-topic', '/robot_description',
            '-x', '0',
            '-y', '0',
            '-z', '0.1'
        ],
        output='screen'
    )

    # rviz2
    start_rviz_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen'
    )

    # robot_state_publisher
    robot_state_publisher_cmd = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'use_sim_time': use_sim_time,
                     'robot_description': Command(['xacro ', bot_urdf_file])}],
        arguments=[bot_urdf_file],
        output='screen'
    )

    # Create the launch description and populate
    return LaunchDescription([
        declare_use_sim_time_argument,
        start_gazebo_server_cmd,
        start_gazebo_client_cmd,
        start_rviz_cmd,
        spawn_entity_cmd,
        robot_state_publisher_cmd
    ])
