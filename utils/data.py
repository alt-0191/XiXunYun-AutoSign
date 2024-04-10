import os
import urllib.parse

class EnvironmentVariables:
    def __init__(self):
        self.variables = {
            'school_id': None,
            'account': None,
            'password': None,
            'longitude': None,
            'latitude': None,
            'address_name': None,
            'address': None,
            'province': None,
            'city': None,
            'pushPlus_set': None,
            'pushPlus_token': None,
        }

    def read_environment_variables(self):
        for key in self.variables.keys():
            self.variables[key] = os.environ.get(key)

    def check_variables_existence(self):
        for key, value in self.variables.items():
            if value is not None:
                print(f"变量 {key} 存在")
            else:
                print(f"变量 {key} 不存在")

    def quote_variables(self, to_quote):
        for var in to_quote:
            if self.variables[var] is not None:
                self.variables[var] = urllib.parse.quote(self.variables[var])
                print(f"已对 {var} 进行转义处理: {self.variables[var]}")
            else:
                print(f"无法对 {var} 进行转义处理，因为变量不存在")

# 创建环境变量管理对象
env_vars_manager = EnvironmentVariables()

# 读取环境变量
env_vars_manager.read_environment_variables()

# 检查并输出变量的存在状态
env_vars_manager.check_variables_existence()

# 需要转义的变量列表
to_quote = ['address_name', 'province', 'city', 'address']

# 对需要转义的变量进行转义处理
env_vars_manager.quote_variables(to_quote)
