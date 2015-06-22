# Based on my own JRE image
FROM nevercast/ubuntu-openjdk-jre7:latest
MAINTAINER Josh Lloyd <j.nevercast@gmail.com>
# Install curl dep
RUN apt-get update && apt-get install -y curl
# Setup NodeSource
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -
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
