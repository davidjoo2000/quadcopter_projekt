import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64, String

class MyNode(Node):
    def __init__(self):
        super().__init__('copter_node')
        self.move_up_pub = self.create_publisher(Float64, '/world/quadcopter/state', 10)

        # Read the launch argument
        self.move_up_height = self.get_parameter('move_up_height').value

        self.move_up()


    def move_up(self):
        msg = Float64()
        msg.data = self.move_up_height
        self.move_up_pub.publish(msg)

def main(args=None):
    
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
