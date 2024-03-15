import pytest
import time

from common.yaml_config import GentConf
from config.public import Public_Methods
from config.driver_config import DriverConfig


class Test1:
    @pytest.mark.login
    def test_login1(self):
        # 获取驱动器配置
        driver = DriverConfig().driver_config()
        time.sleep(3)
        # 调用登录方法，传入手机号和密码
        Public_Methods.Login(GentConf().get_env("username"),
                             GentConf().get_env("password"))
        # 调用创建解决方案方法，传入方案名称
        Public_Methods.Creating_Solution(GentConf().get_env("schemeID"))
        # 调用创建考试方法，传入考试名称和方案ID
        Public_Methods.Creath_Exam(GentConf().get_env_multipleValued("ExaminationForm"),
                                   GentConf().get_env("ExaminationTitle"))
        # 关闭驱动器
        driver.close()

    def test_login2(self):
        # 获取驱动器配置
        driver = DriverConfig().driver_config()
