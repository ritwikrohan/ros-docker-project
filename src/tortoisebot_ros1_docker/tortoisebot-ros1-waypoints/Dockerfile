# # Start from ROS base image
# FROM osrf/ros:noetic-desktop-full-focal

# # Create a catkin workspace
# WORKDIR /
# RUN mkdir -p /simulation_ws/src
# WORKDIR /simulation_ws/src

# # Install essential tools and ROS dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     python3-rosdep \
#     python3-rosinstall \
#     python3-vcstools \
#     python3 \
#     python-is-python3

# # Install ROS core packages
# RUN apt-get install -y \
#     ros-noetic-ros-core=1.5.0-1* \
#     ros-noetic-ros-base=1.5.0-1* \
#     ros-noetic-robot=1.5.0-1* \
#     && rm -rf /var/lib/apt/lists/*

# # Install additional dependencies
# RUN apt-get install -y \
#     python3-yaml

# # Copy the ROS packages from the host into the Docker image
# COPY ./course_web_dev_ros /simulation_ws/src/course_web_dev_ros

# WORKDIR /simulation_ws

# # Initialize rosdep
# RUN rm /etc/ros/rosdep/sources.list.d/20-default.list && rosdep init && rosdep update

# # Install dependencies using rosdep
# RUN rosdep install --from-paths src --ignore-src -r -y

# # Build your ROS packages
# RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# # Set the entry point to start the ROS master and source your workspace
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roscore & sleep 5 && source /simulation_ws/devel/setup.bash && rosrun course_web_dev_ros tortoisebot_action_server.py"]

# # Start from ROS base image
# FROM osrf/ros:noetic-desktop-full-focal

# # Create a catkin workspace
# WORKDIR /
# RUN mkdir -p /simulation_ws/src
# WORKDIR /simulation_ws/src

# # Install essential tools and ROS dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     python3-rosdep \
#     python3-rosinstall \
#     python3-vcstools \
#     python3 \
#     python-is-python3

# # Install ROS core packages
# RUN apt-get install -y \
#     ros-noetic-ros-core=1.5.0-1* \
#     ros-noetic-ros-base=1.5.0-1* \
#     ros-noetic-robot=1.5.0-1* \
#     && rm -rf /var/lib/apt/lists/*

# # Install additional dependencies
# RUN apt-get install -y \
#     python3-yaml

# VOLUME /simulation_ws/src/course_web_dev_ros

# WORKDIR /simulation_ws

# # Initialize rosdep
# RUN rm /etc/ros/rosdep/sources.list.d/20-default.list && rosdep init && rosdep update

# # Install dependencies using rosdep
# RUN rosdep install --from-paths src --ignore-src -r -y

# # Build your ROS packages
# RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# # Set the entry point to start the ROS master and source your workspace
# ENTRYPOINT ["/bin/bash"]


# Start from ROS base image
FROM osrf/ros:noetic-desktop-full-focal

# Create a catkin workspace
WORKDIR /simulation_ws/src

# Install essential tools and ROS dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    python3 \
    python-is-python3

# Install ROS core packages
RUN apt-get install -y \
    ros-noetic-ros-core=1.5.0-1* \
    ros-noetic-ros-base=1.5.0-1* \
    ros-noetic-robot=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*

# Install additional dependencies
RUN apt-get install -y \
    python3-yaml

COPY ./course_web_dev_ros_copy /simulation_ws/src/course_web_dev_ros

WORKDIR /simulation_ws

# Initialize rosdep
RUN rm /etc/ros/rosdep/sources.list.d/20-default.list && rosdep init && rosdep update

# Install dependencies using rosdep
RUN rosdep install --from-paths src --ignore-src -r -y

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# Set the entry point to run catkin_make only if the volume is not empty
ENTRYPOINT ["/bin/bash", "-c", "sleep 30 && source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && sleep 5 && source /simulation_ws/devel/setup.bash && rosrun course_web_dev_ros tortoisebot_action_server.py"]
