# @Time：2024/5/6 19:27
# @Author: Allan
import time

from DrissionPage import WebPage

page = WebPage()
page.get('https://stu-fbt-uat.class-demo.com/')
page.ele('#upgrade-id-ok').click()
ele = page.ele('.user-name')
if ele:
    page.ele('.study-check ').click()
else:
    time.sleep(1)
    page.ele('#login').click()
    page.ele('#login-phone').click()
    page.ele('#loginform-phone').input('13524687901')
    page.ele('#loginform-code').input('222222')
    page.ele('#mobile-login-idm-ok').click()
    text1 = page.ele('#login-code-error').texts()
    for i in text1:
        if i == '验证码不正确':
            page.ele('#loginform-code').clear()
            page.ele('#loginform-code').input('111111')
            page.ele('#mobile-login-idm-ok').click()
            page.ele('#no-wechat-link').click()
            time.sleep(1)
            page.ele('#upgrade-id-ok').click()
        else:
            print('测试通过')
