cmake_minimum_required(VERSION 3.5)
project(slam_project)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(slam_node src/main.cpp)
ament_target_dependencies(slam_node rclcpp)
install(TARGETS slam_node
  DESTINATION lib/${PROJECT_NAME})

ament_package()
