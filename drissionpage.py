# @Time：2024/5/6 19:27
# @Author: Allan

import time
from config.publicpage import PublicPage, page
from selenium.common.exceptions import NoSuchElementException


def xunyuan_login(phone, password):
    """
    Function to log in to the Xunyuan platform.

    :param phone: str, phone number for login
    :param password: str, password for login
    """
    page.get('https://stu-fbt-uat.class-demo.com/')
    username_element = page.ele('.user-name')
    if username_element:
        time.sleep(1)  # Consider replacing with an explicit wait
        PublicPage.page_screenshot_comparison()
    else:
        PublicPage.login(phone, password)
        PublicPage.page_screenshot_comparison()
    page.quit()
