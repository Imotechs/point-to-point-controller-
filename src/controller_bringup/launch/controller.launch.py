from launch import LaunchDescription
import os
from ament_index_python.packages import get_package_share_path
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
def generate_launch_description():
    urdf_path = os.path.join(get_package_share_path('robot_controller'),'urdf','my_robot.urdf.xacro'
    )
    rviz_conf_path = os.path.join(get_package_share_path('robot_controller'),'rviz','urdf_config.rviz')

    
    robot_description = ParameterValue(Command(["xacro ", urdf_path]), value_type=str)

    robot_state_publisher_node =Node(
        package ="robot_state_publisher",
        executable ="robot_state_publisher",
        parameters=[{"robot_description":robot_description}]
    )
    joint_state_publisher_node =Node(
        package ="joint_state_publisher_gui",
        executable ="joint_state_publisher_gui"
    )
    rviz = Node(
        package ="rviz2",
        executable ="rviz2",
        arguments=['-d',rviz_conf_path]
    )
    return LaunchDescription( [
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz]

    )