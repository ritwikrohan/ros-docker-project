# Start from ROS base image
FROM osrf/ros:noetic-desktop-full-focal

# Create a catkin workspace
WORKDIR /
RUN mkdir -p /simulation_ws/src
WORKDIR /simulation_ws/src

# Install Git
RUN apt-get update && apt-get install -y \
    git

# Create a volume for ROS packages
COPY ./tortoisebot_description_copy /simulation_ws/src/tortoisebot_description
COPY ./tortoisebot_gazebo_copy /simulation_ws/src/tortoisebot_gazebo

WORKDIR /simulation_ws

# Build your ROS packages
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# Source the workspace every time a new shell is opened in the container
RUN echo source /simulation_ws/devel/setup.bash >> ~/.bashrc

# Set the entry point to start the ROS launch file
ENTRYPOINT ["/bin/bash", "-c","source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch tortoisebot_gazebo tortoisebot_playground.launch"]
