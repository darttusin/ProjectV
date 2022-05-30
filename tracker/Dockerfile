# Перед сборкой обязательно необходимо поместить веса с названием yolov4.weights в папку data

FROM ubuntu:18.04

# Set temp work directory
# for package configuration
WORKDIR /usr/src/cache

# Update apt packages
RUN apt update
RUN apt upgrade -y

# Install python 3.6
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.6 -y

# Add 3.6 to the available alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

# Set python3.6 as the default python
RUN update-alternatives --set python /usr/bin/python3.6

# Install pip
RUN apt install python3-pip -y
RUN python -m pip install --upgrade pip

# Install libraries
RUN apt-get install --assume-yes git libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev cmake
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype
RUN yes | apt-get install ubuntu-restricted-extras
RUN yes | apt-get install gstreamer1.0-tools gstreamer1.0-x

# Install pip packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Clone OpenCV repo
RUN git clone https://github.com/opencv/opencv.git
WORKDIR /usr/src/cache/opencv
RUN git checkout 4.1.0

# Pre-build OpenCV
RUN mkdir build
WORKDIR /usr/src/cache/opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D PYTHON_EXECUTABLE=$(which python3) \
-D BUILD_opencv_python2=OFF \
-D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
-D PYTHON3_EXECUTABLE=$(which python3) \
-D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
-D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
-D WITH_GSTREAMER=ON \
-D BUILD_EXAMPLES=ON ..

# Build OpenCV
RUN make -j$(nproc)

# Install OpenCV
RUN make install
RUN ldconfig

# Set working directory for code
WORKDIR /tracker

# Copy code data
COPY . /tracker

# Convert darknet weights to tensorflow model
RUN python save_model.py --model yolov4

# Install additional packages
RUN pip install fastapi uvicorn scipy

# Encoding constants
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Install remaining gstreamer plugins
RUN yes | apt-get install libgstreamer1.0-0 gstreamer1.0-dev gstreamer1.0-tools gstreamer1.0-doc
RUN yes | apt-get install gstreamer1.0-plugins-base gstreamer1.0-plugins-good 
RUN yes | apt-get install gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly 
RUN yes | apt-get install gstreamer1.0-libav
RUN yes | apt-get install gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

# Run server on localhost:8081
CMD ["uvicorn", "server:fapp", "--host", "0.0.0.0", "--port", "8081"]