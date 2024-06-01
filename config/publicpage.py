import time

from DrissionPage import WebPage
import cv2
import os
import numpy as np

COMPARISON_FOLDER = "tmp\\comparison_images"
ORIGINAL_IMAGE = "tmp\\original_image"
page = WebPage(timeout=5)


class PublicPage:
    def login(self, password):
        page.ele('#login').click()
        page.ele('#login-phone').click()
        page.ele('#loginform-phone').input(self)
        page.ele('#loginform-code').input('222222')
        page.ele('#mobile-login-idm-ok').click()
        text1 = page.ele('#login-code-error').texts()
        for i in text1:
            if i == '验证码不正确':
                page.ele('#loginform-code').clear()
                page.ele('#loginform-code').input(password)
                page.ele('#mobile-login-idm-ok').click()
                time.sleep(2)
            else:
                print('测试通过')

    def page_screenshot_comparison(self=None):
        screenshot_path = os.path.join(COMPARISON_FOLDER, "actual_screenshot.png")
        time.sleep(3)
        page.get_screenshot(path=COMPARISON_FOLDER, name='actual_screenshot.png', full_page=True)
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
            output_folder = "tmp\\output_images"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_file = os.path.join(output_folder, "result_image.png")
            cv2.imwrite(output_file, result_image)
            print("比对截图失败")
        else:
            print("比对截图成功")
