# Setup OpenJDK 7 on Ubuntu 14.04 (Trusty)
FROM nevercast/ubuntu-openjdk-jre7:latest
MAINTAINER Josh Lloyd <j.nevercast@gmail.com>
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openjdk-7-jdk
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
