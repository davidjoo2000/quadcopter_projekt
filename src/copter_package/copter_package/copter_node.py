import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.publisher_ = self.create_publisher(Twist, '/model_control_topic', 10)
        self.subscription = self.create_subscription(Twist, '/control_command_topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        # Process the control command and publish the corresponding movement command
        # Example: Publish a Twist message to control the model's movement on the y-axis
        twist_msg = Twist()
        twist_msg.linear.y = msg.linear.y  # Use the received command to control the y-axis movement
        self.publisher_.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
