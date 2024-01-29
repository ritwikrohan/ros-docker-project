#!/bin/bash
set -e

# setup ros environment
source /opt/ros/$ROS_DISTRO/setup.bash
source /noetic_ws/devel/setup.bash

sleep 10s

$@