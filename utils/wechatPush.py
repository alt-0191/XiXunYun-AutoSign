import httpx
from utils.data import pushPlus_token as token


def send_push_notification(title, content):
    title = title  # 改成你要的标题内容
    content = content  # 改成你要的正文内容
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content
    }
    headers = {'Content-Type': 'application/json'}

    try:
        with httpx.Client() as client:
            push_response = client.post(url, json=data, headers=headers)
            if push_response.status_code == 200:
                push_response_data = push_response.json()
                if push_response_data.get('code') == 200:
                    print("签到结果推送成功")
                else:
                    print(f"签到结果推送失败，返回码：{push_response_data.get('code')}，消息：{push_response_data.get('msg')}")
            else:
                print(f"请求失败，状态码：{push_response.status_code}")
    except httpx.RequestError as e:
        print(f"请求错误：{e}")
