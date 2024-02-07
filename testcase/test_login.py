import pytest
from config.public import Public_Methods
from config.driver_config import DriverConfig

class Test1():
    @pytest.mark.login
    def test_login1(self):
        driver = DriverConfig().driver_config()
        Public_Methods.Login(15639799731, 'Zy1996321')
        Public_Methods.Creating_Solution('123')
        Public_Methods.Creath_Exam("线上考试", '1234')
        driver.close()



