import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool


class WarningListener(Node):
    def __init__(self):
        super().__init__('warning_listener')
        self.subscription = self.create_subscription(
            Float32, 'battery_status', self.listener_callback, 10)
        self.alert_publisher = self.create_publisher(Bool, 'battery_alert', 10)

    def listener_callback(self, msg):
        battery_level = msg.data
        self.get_logger().info(f'Received battery level: {battery_level}%')

        alert = Bool()
        if battery_level <= 20.0:
            self.get_logger().warn('Battery Low!')
            alert.data = True
        else:
            alert.data = False

        self.alert_publisher.publish(alert)


def main(args=None):
    rclpy.init(args=args)
    node = WarningListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
    