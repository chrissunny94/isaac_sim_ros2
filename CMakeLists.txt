cmake_minimum_required(VERSION 3.5)
project(image_conversion)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(cv_bridge REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  image_conversion/image_conversion_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
