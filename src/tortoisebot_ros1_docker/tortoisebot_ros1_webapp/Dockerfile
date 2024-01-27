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
#     ros-noetic-rosbridge-server \
#     && rm -rf /var/lib/apt/lists/*

# # Install additional dependencies
# RUN apt-get install -y \
#     python3-yaml

# RUN apt-get update && \
#     apt-get install -y python3-websocket ffmpeg && \
#     rm -rf /var/lib/apt/lists/*

# # Set environment variable
# ENV SLOT_ROSBRIDGE_PORT 20001

# # Copy the ROS packages from the host into the Docker image
# COPY ./course_web_dev_ros /simulation_ws/src/course_web_dev_ros
# COPY ./tortoisebot_webapp /simulation_ws/tortoisebot_webapp
# COPY ./web_video_server /simulation_ws/src/web_video_server
# COPY ./async_web_server_cpp /simulation_ws/src/async_web_server_cpp

# WORKDIR /simulation_ws

# # Initialize rosdep
# RUN rm /etc/ros/rosdep/sources.list.d/20-default.list && rosdep init && rosdep update

# # Install dependencies using rosdep
# RUN rosdep install --from-paths src --ignore-src -r -y

# # Build your ROS packages
# RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# # CMD to start your web application and launch files (adjust this according to your actual commands)
# CMD ["bash", "-c", "source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch course_web_dev_ros web.launch & nohup roslaunch course_web_dev_ros tf2_web.launch & cd /simulation_ws/tortoisebot_webapp && python -m http.server 7000"]


# Start from ROS base image
FROM osrf/ros:noetic-desktop-full-focal

# Create a catkin workspace
WORKDIR /
RUN mkdir -p /simulation_ws/src
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
    ros-noetic-rosbridge-server \
    && rm -rf /var/lib/apt/lists/*

# Install additional dependencies
RUN apt-get install -y \
    python3-yaml

RUN apt-get update && \
    apt-get install -y python3-websocket ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Set environment variable
ENV SLOT_ROSBRIDGE_PORT 20001

# Copy the ROS packages from the host into the Docker image
COPY ./course_web_dev_ros_copy /simulation_ws/src/course_web_dev_ros
COPY ./tortoisebot_webapp_copy /simulation_ws/tortoisebot_webapp
COPY ./web_video_server_copy /simulation_ws/src/web_video_server
COPY ./async_web_server_cpp_copy /simulation_ws/src/async_web_server_cpp
COPY ./tf2_web_republisher_copy /simulation_ws/src/tf2_web_republisher

WORKDIR /simulation_ws

# Initialize rosdep
RUN rm /etc/ros/rosdep/sources.list.d/20-default.list && rosdep init && rosdep update

# Install dependencies using rosdep
RUN rosdep install --from-paths src --ignore-src -r -y

# Build your ROS packages
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash; catkin_make"

# CMD to start your web application and launch files (adjust this according to your actual commands)
# CMD ["/bin/bash", "-c", "sleep 50 && source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch course_web_dev_ros web.launch & nohup roslaunch course_web_dev_ros tf2_web.launch & cd /simulation_ws/tortoisebot_webapp && python -m http.server 7000"]
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch course_web_dev_ros web.launch & roslaunch course_web_dev_ros tf2_web.launch & cd /simulation_ws/tortoisebot_webapp && python -m http.server 7000"]
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch course_web_dev_ros web.launch & roslaunch course_web_dev_ros tf2_web.launch & cd /simulation_ws/tortoisebot_webapp && python -m http.server 7000 && wait"]
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /simulation_ws/devel/setup.bash && roslaunch course_web_dev_ros web.launch & source /simulation_ws/devel/setup.bash && roslaunch course_web_dev_ros tf2_web.launch & cd /simulation_ws/tortoisebot_webapp && python -m http.server 7000 && wait"]

