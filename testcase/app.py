import time

import pytest

# from config.public import driver
# from drissionpage import Jijiahyunke_login

if __name__ == '__main__':
    pytest.main(['-m login', '--html=../report/report.html'])
    # Jijiahyunke_login(15639799731, 111111)
    # driver.close()
