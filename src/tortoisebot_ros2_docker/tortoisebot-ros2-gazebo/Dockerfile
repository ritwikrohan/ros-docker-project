# Use the official ROS 2 Galactic base image
FROM ros:galactic

ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

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
  ros-galactic-v4l2-camera \
  python3-dev \
  --no-install-recommends \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


# Create a catkin workspace
WORKDIR /ros2_ws/src
RUN mkdir -p /ros2_ws/src

# Install Git and other dependencies
RUN apt-get update && apt-get install -y \
    git \
    # Add any additional dependencies here \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy your ROS packages into the workspace
COPY ./tortoisebot_description_copy /ros2_ws/src/tortoisebot_description
COPY ./tortoisebot_gazebo_copy /ros2_ws/src/tortoisebot_gazebo
COPY ./tortoisebot_bringup_copy /ros2_ws/src/tortoisebot_bringup
COPY ./ydlidar-ros2_copy /ros2_ws/src/ydlidar-ros2

WORKDIR /ros2_ws

RUN rosdep update
RUN rosdep install --from-paths src --ignore-src -r -y

# Build your ROS packages
RUN /bin/bash -c "source /opt/ros/galactic/setup.bash && colcon build"

# Source the workspace every time a new shell is opened in the container
RUN echo source /ros2_ws/install/setup.bash >> ~/.bashrc

EXPOSE 11311


# Set the entry point to start the ROS launch file
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/galactic/setup.bash && source /ros2_ws/install/setup.bash && ros2 launch tortoisebot_bringup bringup.launch.py use_sim_time:=True"]
# CMD ["ros2 launch tortoisebot_bringup bringup.launch.py use_sim_time:=True"]
# ENTRYPOINT ["/bin/bash"]