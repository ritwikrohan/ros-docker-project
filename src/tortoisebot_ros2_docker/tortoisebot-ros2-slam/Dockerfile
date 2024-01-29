# Start from ROS base image
FROM ros:galactic

ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Exclude the problematic packages and their dependencies
RUN apt-get update && apt-get install -y \
  git \
  ros-galactic-joint-state-publisher \
  ros-galactic-robot-state-publisher \
  ros-galactic-cartographer \
  ros-galactic-cartographer-ros \
  ros-galactic-gazebo-plugins \
  ros-galactic-teleop-twist-keyboard \
  ros-galactic-teleop-twist-joy \
  ros-galactic-xacro ros-galactic-nav2* \
  ros-galactic-urdf \
  ros-galactic-rviz2 \
  ros-galactic-v4l2-camera \
  --no-install-recommends \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Create a catkin workspace
WORKDIR /
RUN mkdir -p /ros2_ws/src
WORKDIR /ros2_ws/src

# Copy your source files into the workspace
COPY ./tortoisebot_slam_copy /ros2_ws/src/tortoisebot_slam
COPY ./tortoisebot_navigation_copy /ros2_ws/src/tortoisebot_navigation
COPY ./tortoisebot_description_copy /ros2_ws/src/tortoisebot_description

WORKDIR /ros2_ws

RUN rosdep update
RUN rosdep install --from-paths src --ignore-src -r -y

# Source the workspace setup.bash
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

RUN /bin/bash -c 'source /opt/ros/galactic/setup.bash && colcon build'

RUN echo "source /ros2_ws/install/setup.bash" >> /etc/bash.bashrc

# Expose default ROS 2 ports
EXPOSE 11311

# Set the entry point to the ROS entry point
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/galactic/setup.bash && source /ros2_ws/install/setup.bash && ros2 launch tortoisebot_slam cartographer.launch.py use_sim_time:=True"]
# CMD ["ros2 launch tortoisebot_slam cartographer.launch.py use_sim_time:=True"]
# ENTRYPOINT ["/bin/bash"]