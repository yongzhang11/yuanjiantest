import time

from DrissionPage import WebPage

page = WebPage(timeout=5)
class PublicPage:
    def login(phone,password):
        page.ele('#login').click()
        page.ele('#login-phone').click()
        page.ele('#loginform-phone').input(phone)
        page.ele('#loginform-code').input('222222')
        page.ele('#mobile-login-idm-ok').click()
        text1 = page.ele('#login-code-error').texts()
        for i in text1:
            if i == '验证码不正确':
                page.ele('#loginform-code').clear()
                page.ele('#loginform-code').input(password)
                page.ele('#mobile-login-idm-ok').click()
                time.sleep(1)
                page.ele('#upgrade-id-ok').click()
            else:
                print('测试通过')