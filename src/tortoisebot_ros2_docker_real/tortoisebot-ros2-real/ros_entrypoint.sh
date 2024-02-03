#!/bin/bash
set -e

# # Specify the output directory and filename for cyclonedds.xml
# OUTPUT_FILE="/var/lib/theconstruct.rrl/cyclonedds.xml"

# # Create the directory if it doesn't exist
# mkdir -p "$(dirname "$OUTPUT_FILE")"

# # Get the host machine's IP address from the provided environment variable
# HOST_IP=$HOSTS_CONTENT

# # Check if the host IP is available
# if [ -z "$HOST_IP" ]; then
#   echo "Error: Host IP not provided through environment variable HOSTS_CONTENT."
#   exit 1
# fi

# # Generate cyclonedds.xml content
# cat <<EOL > "$OUTPUT_FILE"
# <?xml version="1.0" encoding="UTF-8" ?>
# <CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
#     <Domain id="any">
#         <General>
#             <NetworkInterfaceAddress>auto</NetworkInterfaceAddress>
#             <AllowMulticast>false</AllowMulticast>
#             <MaxMessageSize>65500B</MaxMessageSize>
#             <FragmentSize>4000B</FragmentSize>
#             <Transport>udp6</Transport>
#         </General>
#         <Discovery>
#             <Peers>
#                 <!-- Add dynamic peer address based on host IP -->
#                 <Peer address="$HOST_IP"/>
#                 <Peer address="husarnet-local"/>
#             </Peers>
#             <MaxAutoParticipantIndex>100</MaxAutoParticipantIndex>
#             <ParticipantIndex>auto</ParticipantIndex>
#         </Discovery>
#         <Internal>
#             <Watermarks>
#                 <WhcHigh>500kB</WhcHigh>
#             </Watermarks>
#         </Internal>
#         <Tracing>
#             <Verbosity>severe</Verbosity>
#             <OutputFile>stdout</OutputFile>
#         </Tracing>
#     </Domain>
# </CycloneDDS>
# EOL

# # Set CYCLONEDDS_URI environment variable to the generated cyclonedds.xml
# export CYCLONEDDS_URI="file://${OUTPUT_FILE}"

# setup ros environment
source /opt/ros/$ROS_DISTRO/setup.bash
source /ros2_ws/install/setup.bash


sleep 10s

$@