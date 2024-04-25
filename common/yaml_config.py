# @Time：2024/3/15 9:23
# @Author: Allan

import yaml


class GentConf:
    def __init__(self):
        # 打开配置文件
        with open("../config/environment.yaml", "r", encoding="utf-8") as env_file:
            # 加载配置文件内容到self.env变量中
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_env(self, name):
        # 从self.env字典中根据name键获取对应的值
        return self.env[name]

    def get_env_multipleValued(self, name, i=0):
        # 获取环境变量中指定名称的列表
        return self.env[name][i]

