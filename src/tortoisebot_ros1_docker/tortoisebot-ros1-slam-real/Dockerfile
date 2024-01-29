FROM ros:noetic

RUN apt-get update && apt-get install -y \
    ros-noetic-gmapping \
    git \
    ros-noetic-joy \
    ros-noetic-teleop-twist-joy \
    ros-noetic-teleop-twist-keyboard \
    ros-noetic-amcl \
    ros-noetic-map-server \
    ros-noetic-move-base \
    ros-noetic-urdf \
    ros-noetic-xacro \
    ros-noetic-rqt-image-view \
    ros-noetic-gmapping \
    ros-noetic-navigation \
    ros-noetic-joint-state-publisher \
    ros-noetic-robot-state-publisher \
    ros-noetic-slam-gmapping \
    ros-noetic-dwa-local-planner \
    ros-noetic-rviz \
    ros-noetic-joint-state-publisher-gui \
    libvmmalloc-dev \
    libraspberrypi-bin \
    libraspberrypi-dev \
    python3-dev \
    python3-rpi.gpio

# Make the prompt a little nicer
RUN echo "PS1='${debian_chroot:+($debian_chroot)}\u@:\w\$ '" >> /etc/bash.bashrc 

# RUN mkdir -p /docker
RUN mkdir -p /noetic_ws/src

RUN git clone -b noetic --recursive https://github.com/rigbetellabs/tortoisebot.git /noetic_ws/src/tortoisebot

# RUN git clone https://github.com/rg-masterclass/docker.git /docker

RUN rm -rf /noetic_ws/src/tortoisebot/tortoisebot_control
RUN rm -rf /noetic_ws/src/tortoisebot/tortoisebot_gazebo
RUN rm -rf /noetic_ws/src/tortoisebot/tortoisebot_navigation
RUN rm -rf /noetic_ws/src/tortoisebot/tortoisebot_firmware
RUN rm -rf /noetic_ws/src/tortoisebot/raspicam_node
RUN rm -rf /noetic_ws/src/tortoisebot/tortoisebot_description
RUN rm -rf /noetic_ws/src/tortoisebot/ydlidar_ros

# RUN mv /docker/tortoisebot /noetic_ws/src/
# RUN rm -rf /docker

ADD ros_entrypoint.sh /

WORKDIR /noetic_ws

RUN rosdep update
RUN rosdep install --from-paths src --ignore-src -r -y

COPY mapping.launch /noetic_ws/src/tortoisebot/tortoisebot_slam/launch/

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /etc/bash.bashrc

RUN /bin/bash -c 'source /opt/ros/$ROS_DISTRO/setup.bash &&\
catkin_make --directory /noetic_ws -DCMAKE_BUILD_TYPE=Debug'

RUN echo "source /noetic_ws/devel/setup.bash" >> /etc/bash.bashrc

ENTRYPOINT ["bash", "/ros_entrypoint.sh"]
CMD ["roslaunch", "tortoisebot_slam mapping.launch"]