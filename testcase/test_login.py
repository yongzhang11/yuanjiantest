import pytest
import time
from config.public import Public_Methods
from config.driver_config import DriverConfig

class Test1():
    @pytest.mark.login
    def test_login1(self):
        # 获取驱动器配置
        driver = DriverConfig().driver_config()
        time.sleep(3)
        # 调用登录方法，传入手机号和密码
        Public_Methods.Login(15639799731, 'Zy1996321')
        # 调用创建解决方案方法，传入方案名称
        Public_Methods.Creating_Solution('123')
        # 调用创建考试方法，传入考试名称和方案ID
        Public_Methods.Creath_Exam("线上考试", '1234')
        # 关闭驱动器
        driver.quit()
        driver.close()
    def test_login2(self):
        # 获取驱动器配置
        driver = DriverConfig().driver_config()