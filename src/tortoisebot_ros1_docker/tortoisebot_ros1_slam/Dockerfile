# # Start from ROS base image
# FROM osrf/ros:noetic-desktop-full-focal

# # Create a catkin workspace
# WORKDIR /
# RUN mkdir -p /simulation_ws/src
# WORKDIR /simulation_ws/src

# # Install Git
# RUN apt-get update && apt-get install -y \
#     git \
#     sudo \
#     && sudo apt-get update \
#     && sudo apt-get install -y ros-noetic-slam-gmapping

# # Copy the ROS packages from the host into the Docker image
# COPY ./tortoisebot/tortoisebot_slam /simulation_ws/src/tortoisebot_slam
# COPY ./tortoisebot/tortoisebot_navigation /simulation_ws/src/tortoisebot_navigation

# WORKDIR /simulation_ws

# # Build your ROS packages
# RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# # Source the workspace every time a new shell is opened in the container
# RUN echo source /simulation_ws/devel/setup.bash >> ~/.bashrc

# # Set the entry point to start the ROS launch file
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch tortoisebot_slam mapping.launch"]



# Start from ROS base image
FROM osrf/ros:noetic-desktop-full-focal

# Create a catkin workspace
WORKDIR /
RUN mkdir -p /simulation_ws/src
WORKDIR /simulation_ws/src

# Install Git
RUN apt-get update && apt-get install -y \
    git \
    sudo \
    && sudo apt-get update \
    && sudo apt-get install -y ros-noetic-slam-gmapping

# Create a volume for ROS packages
COPY ./tortoisebot_slam_copy /simulation_ws/src/tortoisebot_slam
COPY ./tortoisebot_navigation_copy /simulation_ws/src/tortoisebot_navigation
COPY ./tortoisebot_description_copy /simulation_ws/src/tortoisebot_description

WORKDIR /simulation_ws

# Build your ROS packages
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# Source the workspace every time a new shell is opened in the container
RUN echo source /simulation_ws/devel/setup.bash >> ~/.bashrc

# Set the entry point to start the ROS launch file
ENTRYPOINT ["/bin/bash", "-c", "sleep 20 && source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch tortoisebot_slam mapping.launch"]



