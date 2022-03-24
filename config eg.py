# 数据库的配置信息
# 字符串类型

HOSTNAME = None # 域名或IP地址，例如127.0.0.1
PORT     = '3306'
DATABASE = 'library'
USERNAME = None # 用户名
PASSWORD = None # 密码
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SECRET_KEY = None # 密钥

BOOKS_ROOT_PATH = "项目路径/static/books"