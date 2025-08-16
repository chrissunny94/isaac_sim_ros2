import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool
import cv2
from cv_bridge import CvBridge

class ImageConversionNode(Node):
    def __init__(self):
        super().__init__('image_conversion_node')
        self.mode = 2  # 1: Greyscale, 2: Color (default: Color)
        self.bridge = CvBridge()

        # Subscribe to usb_cam topic
        self.subscription = self.create_subscription(
            Image,
            '/usb_cam/image_raw',        # Change as per your camera topic
            self.image_callback,
            10
        )

        # Publisher for converted images
        self.publisher = self.create_publisher(Image, '/output_image', 10)

        # Service to set mode
        self.srv = self.create_service(SetBool, 'set_mode', self.set_mode_callback)

    def image_callback(self, msg):
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        if self.mode == 1:
            # Convert to grayscale
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            out_msg = self.bridge.cv2_to_imgmsg(cv_img, encoding='mono8')
        else:
            # Publish as color (BGR8)
            out_msg = self.bridge.cv2_to_imgmsg(cv_img, encoding='bgr8')
        self.publisher.publish(out_msg)

    def set_mode_callback(self, request, response):
        self.mode = 1 if request.data else 2
        response.success = True
        response.message = "Set to Greyscale" if self.mode == 1 else "Set to Color"
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ImageConversionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
