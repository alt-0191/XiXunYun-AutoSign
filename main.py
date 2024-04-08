import httpx
import time

# 假设 randomize 是一个自定义模块
from utils.randomize import generate
from utils.location import encrypted_latitude, encrypted_longitude
from utils.wechatPush import send_push_notification
from utils.data import account, password, school_id, province, city, address, address_name, pushPlus_set



def login_and_get_token():
    token, uuid = generate()
    print(f"初始随机token为：{token}")

    url = f"https://api.xixunyun.com/login/api?token={token}&from=app&version=4.9.7&school_id={school_id}"
    payload = {
        'app_version': '4.9.7',
        'uuid': uuid,
        'request_source': 3,
        'platform': 2,
        'password': password,
        'system': '14',
        'school_id': school_id,
        'account': account,
        'app_id': 'cn.vanber.xixunyun.saas'
    }
    headers = {
        'User-Agent': 'okhttp/3.8.1',
        'content-type': 'application/x-www-form-urlencoded',
        'Host': 'api.xixunyun.com',
        'user-agent': 'okhttp/3.8.1'
    }

    try:
        with httpx.Client() as client:
            login_response = client.post(url, headers=headers, data=payload)
            login_response_data = login_response.json()
            if login_response_data.get('code') == 20000:
                cookies = login_response.cookies
                token = login_response.json()['data']['token']
                print("登录成功")
                print(f"获取cookies成功")
                print(f"获取token成功")
                return token, cookies
            else:
                print(f"登录失败，信息：{login_response_data.get('message')}")
                return None, None
    except httpx.RequestError as e:
        print(f"登录时发生请求错误：{e}")


def signin_with_token(token, cookies):
    time.sleep(5)  # 等待5秒
    url = f"https://api.xixunyun.com/signin_rsa?token={token}&from=app&version=4.9.7&school_id={school_id}"

    payload = {
        'address': address,
        'province': province,
        'city': city,
        'latitude': encrypted_latitude,
        'longitude': encrypted_longitude,
        'address_name': address_name
    }
    headers = {
        'User-Agent': 'okhttp/3.8.1',
        'Cookie': str(cookies),
        'content-type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Host': 'api.xixunyun.com',
        'Connection': 'keep-alive'
    }

    try:
        with httpx.Client() as client:
            sign_response_data = client.post(url, headers=headers, data=payload).json()
            sign_message = sign_response_data.get('message')

            if sign_response_data.get('code') == 20000:
                signin_result = "签到成功"
                print(f"{signin_result}，信息：{sign_message}")

                if pushPlus_set == 1:
                    send_push_notification(signin_result, sign_message)
                elif pushPlus_set == 0:
                    print("推送未开启，请检查推送设置")

            else:
                signin_result = "签到失败"
                print(f"{signin_result}，信息：{sign_message}")
                if pushPlus_set != 0:
                    send_push_notification(signin_result, sign_message)
                elif pushPlus_set == 0:
                    print("推送未开启，请检查推送设置")
                return None, None
                # 发送签到结果推送
    except httpx.RequestError as e:
        print(f"登录时发生请求错误：{e}")


if __name__ == "__main__":
    token, cookies = login_and_get_token()
    if token and cookies:
        signin_with_token(token, cookies)