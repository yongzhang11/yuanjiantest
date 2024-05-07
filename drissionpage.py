# @Time：2024/5/6 19:27
# @Author: Allan
import time

from DrissionPage import WebPage
from config.publicpage import PublicPage

page = WebPage()
page.get('https://stu-fbt-uat.class-demo.com/')
page.ele('#upgrade-id-ok').click()
ele = page.ele('.user-name')

if ele:
    time.sleep(1)
    page.ele('.study-check ').click()
else:
    PublicPage.login(15639799731,111111)




