#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import Float32MultiArray

class ESP32SerialBridge(Node):
    def __init__(self):
        super().__init__('esp32_serial_bridge')

        self.serial_port = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        self.publisher_ = self.create_publisher(Float32MultiArray, 'esp32/sensors', 10)
        self.timer = self.create_timer(0.1, self.read_serial_data)

    def read_serial_data(self):
        if self.serial_port.in_waiting:
            try:
                line = self.serial_port.readline().decode('utf-8').strip()
                parts = [float(x) for x in line.split(',') if x]
                msg = Float32MultiArray()
                msg.data = parts
                self.publisher_.publish(msg)
            except Exception as e:
                self.get_logger().warn(f'Erro ao ler linha: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = ESP32SerialBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
