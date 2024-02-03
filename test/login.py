# @Time：2024/2/3 19:30
# @Author: Allan
from config.driver_config import DriverConfig
import pytest


driver = DriverConfig().driver_config()
driver.get("https://www.baidu.com")