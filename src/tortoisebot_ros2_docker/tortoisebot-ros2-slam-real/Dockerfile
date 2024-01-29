FROM ros:galactic

ARG USERNAME=tortoisebot
ARG USER_UID=1000
ARG USER_GID=$USER_UID

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
  ros-galactic-v4l2-camera

# Make the prompt a little nicer
RUN echo "PS1='${debian_chroot:+($debian_chroot)}\u@:\w\$ '" >> /etc/bash.bashrc 

RUN mkdir -p /ros2_ws/src

RUN git clone -b ros2-galactic --recursive https://github.com/rigbetellabs/tortoisebot.git /ros2_ws/src/tortoisebot

RUN rm -rf /ros2_ws/src/tortoisebot/tortoisebot_control

ADD ros_entrypoint.sh /

WORKDIR /ros2_ws

RUN rosdep update
RUN rosdep install --from-paths src --ignore-src -r -y

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /etc/bash.bashrc

ENV RMW_IMPLEMENTATION="rmw_cyclonedds_cpp"

RUN mkdir -p /var/lib/theconstruct.rrl/

COPY cyclonedds.xml /var/lib/theconstruct.rrl/cyclonedds.xml

ENV CYCLONEDDS_URI="file:///var/lib/theconstruct.rrl/cyclonedds.xml"

RUN /bin/bash -c 'source /opt/ros/$ROS_DISTRO/setup.bash && colcon build 2>&1 > /ros2_ws/build.log && exit 0'

RUN echo "source /ros2_ws/install/setup.bash" >> /etc/bash.bashrc

ENTRYPOINT ["bash", "/ros_entrypoint.sh"]
CMD ["ros2", "launch tortoisebot_slam cartographer.launch.py use_sim_time:=False"]