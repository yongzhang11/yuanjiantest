# @Time：2024/5/6 19:27
# @Author: Allan
import time
from config.publicpage import PublicPage
from config.publicpage import page

page.get('https://stu-fbt-uat.class-demo.com/')
page.ele('#upgrade-id-ok').click()
ele = page.ele('.user-name')

def xunyuan_login(pohen,passwprd):
    if ele:
        time.sleep(1)
        page.ele('.study-check ').click()
    else:
        PublicPage.login(pohen,passwprd)
        PublicPage.page_screenshot_comparison()
    page.quit()



