# -*- coding:utf-8 -*-
import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf.csrf import CSRFProtect


class Config(object):
    """工厂配置基类"""
    # 设置csrf秘钥
    SECRET_KEY = 'Fd7ygWLwQ3cFVRgt9gjejniDdQKhVfZjC2bIHtS3/+dleW3QI5CTlZRb6MFJdsV2'

    # 开启调试模式
    DEBUG = True

    # 配置数据库链接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.23.150:3306/Flask_iHome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # 关闭修改跟踪

    # 配置redis
    REDIS_HOST = '192.168.23.150'
    REDIS_PORT = 6379

    # Session扩展配置,默认保存在客户cookie里
    SESSION_TYPE = 'redis'      # 指定session保存方式:redis
    SESSION_USE_SIGNER = True   # 加密cookie中的session_id
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)   # 使用redis实例
    PERMANENT_SESSION_LIFETIME = 86400   # session有效期


app = Flask(__name__)
# 用定义的配置类,并从中加载配置
app.config.from_object(Config)
# 配置数据库
db = SQLAlchemy(app)
# 配置redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 配置Session
Session(app)
# 配置csrf,校验表单,防止跨站请求伪造
CSRFProtect(app)


@app.route('/', methods=['post', 'get'])
def index():
    session['name'] = 'xiaohua'
    redis_store.set('name', 'xiaoli')
    return 'index'


if __name__ == '__main__':
    app.run()

