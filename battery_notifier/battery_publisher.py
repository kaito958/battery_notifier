# SPDX-FileCopyrightText: 2025 Kaito Kubota
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil  # Library to get battery status


class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(String, 'battery_level', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = "Charging" if battery.power_plugged else "Discharging"
            msg = String()
            msg.data = f"Current Battery: {percent}% ({plugged})"
            self.publisher_.publish(msg)
            self.get_logger().info(f'{msg.data}')
        else:
            self.get_logger().warn('Battery information not available.')


def main(args=None):
    rclpy.init(args=args)
    battery_publisher = BatteryPublisher()
    rclpy.spin(battery_publisher)
    battery_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
