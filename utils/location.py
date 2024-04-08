import rsa
import base64
from utils.data import latitude, longitude

# 翻了网站没找到公钥，反编译apk拿到了
public_key_data = b'''-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlYsiV3DsG+t8OFMLyhdmG2P2J4GJwmwb1rKKcDZmTxEphPiYTeFIg4IFEiqDCATAPHs8UHypphZTK6LlzANyTzl9LjQS6BYVQk81LhQ29dxyrXgwkRw9RdWaMPtcXRD4h6ovx6FQjwQlBM5vaHaJOHhEorHOSyd/deTvcS+hRSQIDAQAB
    -----END PUBLIC KEY-----'''
public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key_data)


# 加密数据
def encrypt_data(data):
    encrypted_data = rsa.encrypt(str(data).encode(), public_key)
    return base64.b64encode(encrypted_data).decode()


# 加密经纬度数据
def encrypt():
    return encrypt_data(longitude), encrypt_data(latitude)


encrypted_longitude, encrypted_latitude = encrypt()
# print("加密后的经度:", encrypted_longitude)
# print("加密后的纬度:", encrypted_latitude)
