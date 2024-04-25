安装docker    
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
yum install -y yum-utils \
    yum-config-manager \
    --add-repo \
    http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
   
设置阿里源
yum install docker-ce -y

下载Docker

systemctl start docker

启动Docker

systemctl enable docker

查看是否有镜像

docker search centos

运行镜像及参数

docker run -itd --name=容器名称 镜像ID 

参数说明：

-i：交互式操作。

-t：终端

-d：后台运行

--restart=always：开机自启动

进入容器

docker exec -it 镜像ID /bin/bash

安装Docker-compose

curl -L "https://github.com/docker/compose/releases/download/1.27.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

docker-compose version

设置开机启动

1.Create a Docker Network

- docker network create grid

2.下载镜像

- hub

docker pull selenium/hub:latest

- chrome
selenium/node-chrome:latest

3.运行镜像

docker run -d -p 4442-4444:4442-4444 --net grid --restart: always   --name selenium-hub selenium/hub:latest

docker run -d  -p 5900:5900  --net grid -e SE_EVENT_BUS_HOST=selenium-hub 

--restart: always  
--shm-size="2g" 
-e SE_EVENT_BUS_PUBLISH_PORT=4442 
-e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 
-e SE_NODE_SCREEN_WIDTH=1280 
-e SE_NODE_SCREEN_HEIGHT=800 
-e SE_NODE_MAX_SESSIONS=5
selenium/node-chrome:latest

VNC登录：
Vnc Server：IP:5900
password:secret

运行 app.py文件就行



