# -*- coding:utf-8 -*-
from qiniu import Auth, put_data

access_key = '未注册,pass'
secret_key = '未注册,pass'

bucket_name = 'FlaskIHome'
key = 'my-python-logo.png'


def storage_image(data):
    """用于七牛云上传照片"""
    if not data:
        return None

    q = Auth(access_key, secret_key)
    # 指定存储名字
    token = q.upload_token(bucket_name)
    ret, info = put_data(token, None, data)

    if info.status_code != 200:
        raise Exception('七牛云上传文件失败')

    return ret.get('key')

if __name__ == '__main__':
    file_name = raw_input('请输入文件名: ')
    with open(file_name, 'rb') as f:
        storage_image(f.read())