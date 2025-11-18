FROM nvcr.io/nvidia/isaac-sim:4.2.0
# Add this near the end of your Dockerfile
# ---------------------------
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

ARG USER=developer
RUN apt-get update && apt-get install -y sudo \
    && useradd -ms /bin/bash ${USER} \
    && usermod -aG sudo ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


RUN apt-get update && apt-get install -y curl gnupg2 lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | apt-key add - && \
    echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros2.list && \
    apt-get update && apt-get install -y \
      ros-humble-desktop python3-rosdep python3-colcon-common-extensions \
      build-essential git cmake python3-pip && \
    rosdep init && rosdep update && rm -rf /var/lib/apt/lists/*