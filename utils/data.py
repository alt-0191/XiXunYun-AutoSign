import urllib.parse
import os

# 读取 Secrets

school_id = os.environ.get('SCHOOL_ID')
account = os.environ.get('ACCOUNT')
password = os.environ.get('PASSWORD')
longitude = os.environ.get('LONGITUDE')
latitude = os.environ.get('LATITUDE')
address = os.environ.get('ADDRESS')
address_name = os.environ.get('ADDRESS_NAME')
province = os.environ.get('PROVINCE')
city = os.environ.get('CITY')
pushPlus_set = os.environ.get('PUSHPLUS_SET')
pushPlus_token = os.environ.get('PUSHPLUS_TOKEN')

# 检查并输出每个变量的存在状态
variables = {
    'school_id': school_id,
    'account': account,
    'password': password,
    'longitude': longitude,
    'latitude': latitude,
    'address_name': address_name,
    'address': address,
    'province': province,
    'city': city,
    'pushPlus_set': pushPlus_set,
    'pushPlus_token': pushPlus_token,
}

for key, value in variables.items():
    if value is not None:
        print(f"变量 {key} 存在")
    else:
        print(f"变量 {key} 不存在")

# 需要转义的变量列表
to_quote = ['address_name', 'province', 'city', 'address']

# 对需要转义的变量进行转义处理
for var in to_quote:
    if variables[var] is not None:
        variables[var] = urllib.parse.quote(variables[var])
        print(f"已对 {var} 进行转义处理: {variables[var]}")
    else:
        print(f"无法对 {var} 进行转义处理，因为变量不存在")

