# @Time：2024/3/15 9:23
# @Author: Allan

import yaml


class GentConf:
    def __init__(self):
        with open("../config/environment.yaml", "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_env(self, name):
        return self.env[name]

    def get_env_multipleValued(self, name, i=0):
        return self.env[name][i]


# if __name__ == '__main__':
#     print(type(GentConf().get_env("schemeID")))
