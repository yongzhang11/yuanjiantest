# @Time：2024/2/3 19:30
# @Author: Allan
import time
from config.driver_config import DriverConfig
import cv2
import os
import numpy as np

driver = DriverConfig().driver_config()
Xpath = driver.find_element_by_xpath
Id = driver.find_element_by_id
COMPARISON_FOLDER = "comparison_images"
ORIGINAL_IMAGE = "original_image"


class Public_Methods:

    def Login(self, password):
        # 最大化浏览器窗口
        driver.maximize_window()
        # 设置登录URL
        url = 'https://admin-uat.yuanjian.live/login'
        # 打开登录页面
        driver.get(url)
        # 点击登录按钮
        Xpath('//*[@id="loginEvent"]/button').click()
        # 在用户名输入框中输入用户名
        Id('phone').send_keys(self)
        # 在密码输入框中输入密码
        Id('password').send_keys(password)
        # 点击登录按钮
        Xpath('//*[@id="w0"]/div[5]/button').click()

    def Creating_Solution(self):
        # 找到网页上的指定元素列表
        elements1 = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/table/tbody/tr/td/a')
        # 获取元素列表的长度
        number = len(elements1)
        # 创建一个空列表用于存储文本
        list = []
        # 遍历元素列表，将每个元素的文本内容添加到list中
        for i in range(1, number + 1):
            element = Xpath(f'/html/body/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td[1]/a')
            list.append(element.text)
        # 如果列表中存在self，则点击对应的元素
        if any(self in elements for elements in list):
            # 存在 self，点击对应的元素
            for elements in list:
                if self in elements:
                    Xpath(f'//a[contains(text(),"{self}")]').click()
        else:
            # 不存在 self，执行创建项目的操作
            # 点击创建项目的按钮
            Id('btn_createplan').click()
            # 等待2秒钟，确保页面加载完成
            time.sleep(2)
            # 在创建项目的输入框中输入项目名称
            Id('create-project-name').send_keys(self)
            # 点击下一步按钮
            Xpath('//*[@id="create_step_2"]/div[2]/div[3]/div/div/div/button').click()
            # 等待2秒钟，确保页面加载完成
            time.sleep(2)
            # 点击创建按钮
            Xpath('//*[@id="create_button"]').click()

    def Creath_Exam(exam, name):
        # 隐式等待10秒，让页面元素加载完成
        driver.implicitly_wait(10)
        # 点击id为"nav-main-left-online"的li元素的第二个子元素
        Xpath('//li[@id="nav-main-left-online"][2]').click()
        # 查找页面上是否存在文本为"创建考试"的a元素，并计算其数量
        exist = len(driver.find_elements_by_xpath('//a[text()= "创建考试" ]'))
        # 打印a元素的数量
        print(exist)
        # 如果a元素的数量大于等于1，则执行以下操作
        if exist >= 1:
            # 点击文本为"创建考试"的a元素
            Xpath('//a[text()= "创建考试" ]').click()
            # 点击文本为exam的h3元素的上级元素的上级元素的button元素，按钮文本为"立即创建"
            Xpath(f"//h3[text()='{exam}']/../..//button[text()='立即创建']").click()
            # 隐式等待10秒，让页面元素加载完成
            driver.implicitly_wait(10)
            # 在id为"create-plan-name"的元素中输入name
            Id('create-plan-name').send_keys(name)
            # 点击class为"input-date"的span元素的input子元素，placeholder为"考试开始时间"
            Xpath("//span[@class='input-date']/input[@placeholder='考试开始时间']").click()
            # 点击class为"botflex jedatebtn"的div元素的span子元素，文本中包含"确定"
            Xpath("//div[@class='botflex jedatebtn']/span[contains(text(),'确定')]").click()
            # 点击文本中包含"下一步"的button元素
            Xpath("//button[contains(text(),'下一步')]").click()
            # 点击文本中包含"稍后添加"的a元素
            Xpath("//a[contains(text(),'稍后添加')]").click()
            # 点击文本中包含"完成并进入考试首页"的button元素
            Xpath("//button[contains(text(),'完成并进入考试首页')]").click()
        else:
            # 如果没有找到文本为"创建考试"的a元素，则执行以下操作
            pass
            # 查找页面上class为"list-interview"的ul元素的li子元素中的h3元素数量
            listing = len(driver.find_elements_by_xpath("//ul[@class='list-interview']/li//h3"))
            # 初始化一个空列表，用于存储考试名称
            Exam_Names = []
            # 遍历li元素，从第1个到第listing个
            for i in range(1, listing + 1):
                # 获取第i个li元素中的h3子元素的a子元素的文本，作为考试名称
                Exam_Name = Xpath(f"//ul[@class='list-interview']/li[{i}]//h3/a")
                # 将考试名称添加到列表中
                Exam_Names.append(Exam_Name.text)
            # 如果考试名称列表中存在与name相同的元素
            if any(name in elements for elements in Exam_Names):
                # 遍历考试名称列表
                for elements in Exam_Names:
                    # 如果元素中包含name
                    if name in elements:
                        # 点击包含name的a元素
                        Xpath(f'//a[contains(text(),"{name}")]').click()

    def test_screenshot_comparison(url):
        # 打开网页
        driver.get(url)
        # 获取页面截图
        screenshot_path = os.path.join(COMPARISON_FOLDER, "actual_screenshot.png")
        if not os.path.exists(COMPARISON_FOLDER):
            os.makedirs(COMPARISON_FOLDER)
        driver.save_screenshot(screenshot_path)
        actual_image = cv2.imread(screenshot_path)
        # 加载参考截图
        reference_image_path = os.path.join(ORIGINAL_IMAGE, "reference_screenshot.png")
        if not os.path.exists(ORIGINAL_IMAGE):
            os.makedirs(ORIGINAL_IMAGE)
        reference_image = cv2.imread(reference_image_path)

        # 将图片转换为灰度图像
        gray_image1 = cv2.cvtColor(actual_image, cv2.COLOR_BGR2GRAY)
        gray_image2 = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

        # 计算两张灰度图像的差异
        diff_image = cv2.absdiff(gray_image1, gray_image2)

        threshold = 0.001
        diff_mask = diff_image > threshold
        total_pixels = gray_image1.size
        diff_pixels = np.count_nonzero(diff_image)
        percentage_diff = diff_pixels / total_pixels
        if percentage_diff > threshold:
            result_image = reference_image.copy()
            result_image[diff_mask] = [0, 0, 255]  # 红色
            # 保存结果图像到指定文件夹
            output_folder = "output_images"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_file = os.path.join(output_folder, "result_image.png")
            cv2.imwrite(output_file, result_image)
