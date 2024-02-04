# @Time：2024/2/3 19:30
# @Author: Allan
import time

from config.driver_config import DriverConfig
import pytest


driver = DriverConfig().driver_config()

class logint:

    def chaungjianfangan(user, password, fanganmingcheng):
        driver.maximize_window()
        url = 'https://admin-uat.yuanjian.live/login'
        driver.get(url)

        Xpath = driver.find_element_by_xpath
        Id = driver.find_element_by_id

        Xpath('//*[@id="loginEvent"]/button').click()
        Id('phone').send_keys(user)
        Id('password').send_keys(password)
        Xpath('//*[@id="w0"]/div[5]/button').click()
        list = []
        for i in range(1, 7):
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
        driver.implicitly_wait(10)
        Xpath('//li[@id="nav-main-left-online"][2]').click()
        Xpath('//a[text()= "创建考试" ]').click()
        Xpath("//h3[text()='线上考试']/../..//button[text()='立即创建']").click()
        driver.implicitly_wait(10)
        Id('create-plan-name').send_keys(123)
        time.sleep(10)
        driver.close()

