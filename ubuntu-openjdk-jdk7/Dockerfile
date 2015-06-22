# Setup OpenJDK 7 on Ubuntu 14.04 (Trusty)
FROM nevercast/ubuntu-mirrors:latest
MAINTAINER Josh Lloyd <j.nevercast@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends openjdk-7-jdk && apt-get clean
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
