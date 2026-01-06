import launch
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='battery_notifier',
            executable='battery_publisher',
            name='battery_publisher',
            output='screen',
        ),
        launch_ros.actions.Node(
            package='battery_notifier',
            executable='warning_listener',
            name='warning_listener',
            output='screen',
        ),
    ])
