FROM ubuntu:trusty
MAINTAINER Josh Lloyd <j.nevercast@gmail.com>
COPY mirrors.lst /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get clean -y && apt-get update -y && apt-get upgrade -y
