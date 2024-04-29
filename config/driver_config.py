# @Time：2024/2/3 19:13
# @Author: Allan
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        # 定义远程浏览器的地址
        remote_url = "http://10.1.2.218:4444"
        # 定义浏览器配置
        chrome_options = Options()
        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # 本地浏览器实例
        driver = webdriver.Chrome()
        # 创建远程浏览器实例
        # driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
        # 删除所有cookies
        driver.delete_all_cookies()
        # yield driver
        # 关闭浏览器
        # driver.quit()

        return driver
