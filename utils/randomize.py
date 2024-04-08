import secrets


# 生成一个长度为 32 的 URL 安全的随机字符串作为 token,其实根本用不到,写完懒得改了
def generate():
    token = str(secrets.token_urlsafe(32))

    # uuid似乎没有实际作用，仅作为广告标识符
    uuid = str(secrets.token_hex(8))

    return token, uuid