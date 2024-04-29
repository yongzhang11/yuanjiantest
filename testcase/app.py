import pytest

from config.public import driver

if __name__ == '__main__':
    pytest.main(['-m login', '--html=../report/report.html'])
    # driver.close()
