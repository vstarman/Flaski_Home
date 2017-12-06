# -*- coding:utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from iHome import create_app, db
from iHome import models


# 用工厂模式,根据不同参数生产不同app
app = create_app('development')
# 数据库迁移
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # app.run()
    # db.drop_all()
    # db.create_all()
    manager.run()
