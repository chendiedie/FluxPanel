import argparse
import os
import sys
from dotenv import load_dotenv
from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Literal


# [AI注释] 应用基本配置类
# 继承自BaseSettings，用于管理应用的基本设置
class AppSettings(BaseSettings):
    """
    应用配置
    """
    # [AI注释] 应用环境，默认为开发环境
    app_env: str = 'dev'
    # [AI注释] 应用名称
    app_name: str = 'FluxServer'
    # [AI注释] API根路径
    app_root_path: str = '/dev-api'
    # [AI注释] 静态文件路径
    app_static_path: str = os.path.join(os.getcwd(), "static/templates")
    # [AI注释] 服务器监听地址
    app_host: str = '0.0.0.0'
    # [AI注释] 服务器监听端口
    app_port: int = 9099
    # [AI注释] 应用版本号
    app_version: str = '1.0.0'
    # [AI注释] 是否启用热重载
    app_reload: bool = True
    # [AI注释] 工作进程数
    app_workers: int = 5
    # [AI注释] 是否启用IP地理位置查询
    app_ip_location_query: bool = True
    # [AI注释] 是否允许多设备同时登录
    app_same_time_login: bool = True


# [AI注释] JWT认证配置类
# 用于管理JWT相关的配置参数
class JwtSettings(BaseSettings):
    """
    Jwt配置
    """
    # [AI注释] JWT密钥
    jwt_secret_key: str = 'b01c66dc2c58dc6a0aabfe2144256be36226de378bf87f72c0c795dda67f4d55'
    # [AI注释] JWT算法
    jwt_algorithm: str = 'HS256'
    # [AI注释] JWT过期时间（分钟）
    jwt_expire_minutes: int = 1440
    # [AI注释] Redis中JWT的过期时间（分钟）
    jwt_redis_expire_minutes: int = 30


# [AI注释] 数据库配置类
# 用于管理数据库连接相关的配置
class DataBaseSettings(BaseSettings):
    """
    数据库配置
    """
    # [AI注释] 数据库类型，支持mysql或postgresql
    db_type: Literal['mysql', 'postgresql'] = 'mysql'
    # [AI注释] 数据库主机地址
    db_host: str = '127.0.0.1'
    # [AI注释] 数据库端口
    db_port: int = 3306
    # [AI注释] 数据库用户名
    db_username: str = 'root123'
    # [AI注释] 数据库密码
    db_password: str = 'xxxx'
    # [AI注释] 数据库名称
    db_database: str = 'xxxx'
    # [AI注释] 是否打印SQL语句
    db_echo: bool = True
    # [AI注释] 连接池最大溢出数
    db_max_overflow: int = 10
    # [AI注释] 连接池大小
    db_pool_size: int = 50
    # [AI注释] 连接池回收时间（秒）
    db_pool_recycle: int = 3600
    # [AI注释] 连接池超时时间（秒）
    db_pool_timeout: int = 30


# [AI注释] Redis配置类
# 用于管理Redis连接相关的配置
class RedisSettings(BaseSettings):
    """
    Redis配置
    """
    # [AI注释] Redis主机地址
    redis_host: str = '127.0.0.1'
    # [AI注释] Redis端口
    redis_port: int = 6379
    # [AI注释] Redis用户名
    redis_username: str = ''
    # [AI注释] Redis密码
    redis_password: str = ''
    # [AI注释] Redis数据库索引
    redis_database: int = 2


# [AI注释] 阿里云OSS配置类
# 用于管理阿里云对象存储服务相关的配置
class ALIOssSettings(BaseSettings):
    # [AI注释] 阿里云OSS访问密钥
    ALI_OSS_KEY: str = 'xxxx'
    # [AI注释] 阿里云OSS访问密钥密码
    ALI_OSS_SECRET: str = 'xxxx'
    # [AI注释] 阿里云OSS终端节点
    ALI_OSS_END_POINT: str = 'xxxx'
    # [AI注释] 阿里云OSS前缀
    ALI_OSS_PRE: str = 'xxxx'
    # [AI注释] 阿里云OSS存储桶名称
    ALI_OSS_BUCKET: str = 'xxxx'
    # [AI注释] 上传方法
    UPLOAD_METHOD: str = 'xxxx'


# [AI注释] 文件上传配置类
# 用于管理文件上传相关的配置
class UploadSettings:
    """
    上传配置
    """
    # [AI注释] 上传文件URL前缀
    UPLOAD_PREFIX: str = '/profile'
    # [AI注释] 上传文件存储路径
    UPLOAD_PATH: str = 'flux_admin/upload_path'
    # [AI注释] 上传机器标识
    UPLOAD_MACHINE: str = 'A'
    # [AI注释] 允许上传的文件扩展名列表
    DEFAULT_ALLOWED_EXTENSION: list = [
        # 图片格式
        'bmp',
        'gif',
        'jpg',
        'jpeg',
        'png',
        # Office文档格式
        'doc',
        'docx',
        'xls',
        'xlsx',
        'ppt',
        'pptx',
        'html',
        'htm',
        'txt',
        # 压缩文件格式
        'zip',
        'gz',
        'bz2',
        # 视频格式
        'mp4',
        'avi',
        'rmvb',
        # PDF格式
        'pdf',
    ]
    # [AI注释] 下载文件存储路径
    DOWNLOAD_PATH: str = 'flux_admin/download_path'

    def __init__(self):
        if not os.path.exists(self.UPLOAD_PATH):
            os.makedirs(self.UPLOAD_PATH)
        if not os.path.exists(self.DOWNLOAD_PATH):
            os.makedirs(self.DOWNLOAD_PATH)


# [AI注释] 缓存路径配置类
# 用于管理缓存文件存储路径
class CachePathConfig:
    """
    缓存目录配置
    """
    # [AI注释] 缓存文件绝对路径
    PATH = os.path.join(os.path.abspath(os.getcwd()), 'caches')
    # [AI注释] 缓存文件相对路径
    PATHSTR = 'caches'


# [AI注释] 配置获取类
# 用于统一管理和获取各种配置
class GetConfig:
    """
    获取配置
    """

    def __init__(self):
        self.parse_cli_args()

    @lru_cache()
    def get_app_config(self):
        """
        获取应用配置
        """
        # 实例化应用配置模型
        return AppSettings()

    @lru_cache()
    def get_jwt_config(self):
        """
        获取Jwt配置
        """
        # 实例化Jwt配置模型
        return JwtSettings()

    @lru_cache()
    def get_database_config(self):
        """
        获取数据库配置
        """
        # 实例化数据库配置模型
        return DataBaseSettings()

    @lru_cache()
    def get_redis_config(self):
        """
        获取Redis配置
        """
        # 实例化Redis配置模型
        return RedisSettings()

    @lru_cache()
    def get_upload_config(self):
        """
        获取数据库配置
        """
        # 实例上传配置
        return UploadSettings()

    @lru_cache()
    def get_oss_config(self):
        """
        获取OSS配置
        """
        return ALIOssSettings()

    @staticmethod
    def parse_cli_args():
        """
        解析命令行参数
        """
        if 'uvicorn' in sys.argv[0]:
            # 使用uvicorn启动时，命令行参数需要按照uvicorn的文档进行配置，无法自定义参数
            pass
        else:
            # 使用argparse定义命令行参数
            parser = argparse.ArgumentParser(description='命令行参数')
            parser.add_argument('--env', type=str, default='', help='运行环境')
            # 解析命令行参数
            # args = parser.parse_args()
            args, unknown = parser.parse_known_args()
            # 设置环境变量，如果未设置命令行参数，默认APP_ENV为dev
            os.environ['APP_ENV'] = args.env if args.env else 'dev'
        # 读取运行环境
        run_env = os.environ.get('APP_ENV', '')
        # 运行环境未指定时默认加载.env.dev
        env_file = '.env.dev'
        # 运行环境不为空时按命令行参数加载对应.env文件
        if run_env != '':
            env_file = f'.env.{run_env}'
        # 加载配置
        load_dotenv(env_file)


# 实例化获取配置类
get_config = GetConfig()
# 应用配置
AppConfig = get_config.get_app_config()
# Jwt配置
JwtConfig = get_config.get_jwt_config()
# 数据库配置
DataBaseConfig = get_config.get_database_config()
# Redis配置
RedisConfig = get_config.get_redis_config()
# 上传配置
UploadConfig = get_config.get_upload_config()
# OSS配置
OSSConfig = get_config.get_oss_config()
