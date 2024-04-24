1.安装配置Docker
安装docker    
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
- yum install -y yum-utils \
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




4.test
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# 定义远程浏览器的地址
remote_url = "http://10.1.2.218:4444"

# 定义浏览器配置
chrome_options = Options()

# 添加所需的浏览器选项
#chrome_options.add_argument('--headless')  # 设置无头模式
chrome_options.add_argument('--disable-gpu')  # 禁用 GPU 加速

# 创建远程浏览器实例
driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)

# 将浏览器窗口最大化
driver.maximize_window()

# 打开指定的网页
driver.get("https://www.baidu.com")
time.sleep(2)
driver.save_screenshot('screenshot1.png')
print("截图完成")

# 关闭浏览器
driver.quit()


docker-compose.yml文件：
version: '3'
services:
  selenium-hub:
    image: selenium/hub:latest
    ports:
      - 4442-4444:4442-4444
    networks:
      - grid
    restart: always

  selenium-node-chrome:
    image: selenium/node-chrome:latest
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
      - SE_EVENT_BUS_PUBLISH_PORT=4442
      - SE_EVENT_BUS_SUBSCRIBE_PORT=4443
      - SE_NODE_SCREEN_WIDTH=1280
      - SE_NODE_SCREEN_HEIGHT=800
      - SE_NODE_MAX_SESSIONS=8
    shm_size: 2g
    ports:
      - 5900:5900
    networks:
      - grid
    restart: always

  selenium-node-chrome2:   # 添加的第二个 Chrome 节点
    image: selenium/node-chrome:latest
    environment:
      - SE_EVENT_BUS_HOST=selenium-hub
      - SE_EVENT_BUS_PUBLISH_PORT=4442
      - SE_EVENT_BUS_SUBSCRIBE_PORT=4443
      - SE_NODE_SCREEN_WIDTH=1280
      - SE_NODE_SCREEN_HEIGHT=800
      - SE_NODE_MAX_SESSIONS=8
    shm_size: 2g
    ports:
      - 5901:5900   # 使用不同的 VNC 端口
    networks:
      - grid
    restart: always

networks:
  grid:

说明：
这个Docker Compose文件定义了两个服务：selenium-hub和selenium-node-chrome。selenium-hub服务使用selenium/hub:latest镜像，并将端口4442-4444映射到主机的相同端口。selenium-node-chrome服务使用selenium/node-chrome:latest镜像，并设置了事件总线主机、事件发布和订阅端口、屏幕宽度和高度以及最大会话数等环境变量。它还将共享内存大小设置为2GB（shm_size: 2g）。
这两个服务都连接到grid网络，以允许容器之间的通信。
在与docker-compose.yml文件相同的目录中运行docker-compose up -d，容器将在后台启动，您将拥有一个具有指定配置的Selenium Grid环境。
注意：在使用此YAML文件之前，请确保已在系统上安装了Docker Compose。


