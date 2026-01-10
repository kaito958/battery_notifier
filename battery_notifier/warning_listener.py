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
    except Exception:
        # 強制終了時のエラーを無視して静かに終了
        pass
    finally:
        # ノードを破棄
        if node:
            node.destroy_node()
        # 通信がまだ有効な場合のみシャットダウン（二重終了防止）
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()