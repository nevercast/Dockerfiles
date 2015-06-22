# Based on my own JRE image
FROM nevercast/ubuntu-openjdk-jre7:latest
MAINTAINER Josh Lloyd <j.nevercast@gmail.com>
# Setup NodeSource
ADD https://deb.nodesource.com/setup_0.12 /tmp/s12
RUN bash /tmp/s12 && rm /tmp/s12
# Install Other dependencies
RUN apt-get update && apt-get install -y \
	g++ \
	gcc \
	git \
	make \
	nodejs \
	openssh-server \
	openssl
# Setup scales group
RUN addgroup --system scalesuser
# SSHD Config
# Clone scales
# Install scales
# Install certificate
# Start server perhaps?
