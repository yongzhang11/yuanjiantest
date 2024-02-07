# @Time：2024/2/3 19:30
# @Author: Allan
import time
from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()
Xpath = driver.find_element_by_xpath
Id = driver.find_element_by_id


class Public_Methods:

    def Login(user, password):
        driver.maximize_window()
        url = 'https://admin-uat.yuanjian.live/login'
        driver.get(url)
        Xpath('//*[@id="loginEvent"]/button').click()
        Id('phone').send_keys(user)
        Id('password').send_keys(password)
        Xpath('//*[@id="w0"]/div[5]/button').click()

    def Creating_Solution(fanganmingcheng):
        elements1 = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/table/tbody/tr/td/a')
        number = len(elements1)
        list = []
        for i in range(1, number + 1):
            element = Xpath(f'/html/body/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td[1]/a')
            list.append(element.text)
        if any(fanganmingcheng in elements for elements in list):
            # 存在 fanganmingcheng，点击对应的元素
            for elements in list:
                if fanganmingcheng in elements:
                    Xpath(f'//a[contains(text(),"{fanganmingcheng}")]').click()
        else:
            # 不存在 fanganmingcheng，执行创建项目的操作
            Id('btn_createplan').click()
            time.sleep(2)
            Id('create-project-name').send_keys(fanganmingcheng)
            Xpath('//*[@id="create_step_2"]/div[2]/div[3]/div/div/div/button').click()
            time.sleep(2)
            Xpath('//*[@id="create_button"]').click()

    def Creath_Exam(exam, name):
        driver.implicitly_wait(10)
        Xpath('//li[@id="nav-main-left-online"][2]').click()
        exist = len(driver.find_elements_by_xpath('//a[text()= "创建考试" ]'))
        print(exist)
        if exist >= 1:
            Xpath('//a[text()= "创建考试" ]').click()
            Xpath(f"//h3[text()='{exam}']/../..//button[text()='立即创建']").click()
            driver.implicitly_wait(10)
            Id('create-plan-name').send_keys(name)
            Xpath("//span[@class='input-date']/input[@placeholder='考试开始时间']").click()
            Xpath("//div[@class='botflex jedatebtn']/span[contains(text(),'确定')]").click()
            Xpath("//button[contains(text(),'下一步')]").click()
            Xpath("//a[contains(text(),'稍后添加')]").click()
            Xpath("//button[contains(text(),'完成并进入考试首页')]").click()
        else:
            pass
            listing = len(driver.find_elements_by_xpath("//ul[@class='list-interview']/li//h3"))
            Exam_Names = []
            for i in range(1, listing + 1):
                Exam_Name = Xpath(f"//ul[@class='list-interview']/li[{i}]//h3/a")
                Exam_Names.append(Exam_Name.text)
            if any(name in elements for elements in Exam_Names):
                for elements in Exam_Names:
                    if name in elements:
                        Xpath(f'//a[contains(text(),"{name}")]').click()
