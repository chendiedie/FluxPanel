# [AI注释] 导入必要的模块
import datetime
from sqlalchemy import Column, Integer, DateTime, String, text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from urllib.parse import quote_plus
from config.env import DataBaseConfig

# [AI注释] 构建MySQL数据库连接URL
# 使用quote_plus对密码进行URL编码，确保特殊字符能够正确传输
ASYNC_SQLALCHEMY_DATABASE_URL = (
    f'mysql+asyncmy://{DataBaseConfig.db_username}:{quote_plus(DataBaseConfig.db_password)}@'
    f'{DataBaseConfig.db_host}:{DataBaseConfig.db_port}/{DataBaseConfig.db_database}'
)

# [AI注释] 如果是PostgreSQL数据库，使用PostgreSQL的连接URL
if DataBaseConfig.db_type == 'postgresql':
    ASYNC_SQLALCHEMY_DATABASE_URL = (
        f'postgresql+asyncpg://{DataBaseConfig.db_username}:{quote_plus(DataBaseConfig.db_password)}@'
        f'{DataBaseConfig.db_host}:{DataBaseConfig.db_port}/{DataBaseConfig.db_database}'
    )

# [AI注释] 创建异步数据库引擎
# 配置连接池参数和日志输出
async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL,
    echo=DataBaseConfig.db_echo,  # 是否打印SQL语句
    max_overflow=DataBaseConfig.db_max_overflow,  # 连接池最大溢出数
    pool_size=DataBaseConfig.db_pool_size,  # 连接池大小
    pool_recycle=DataBaseConfig.db_pool_recycle,  # 连接回收时间
    pool_timeout=DataBaseConfig.db_pool_timeout,  # 连接超时时间
)

# [AI注释] 创建异步会话工厂
# 配置自动提交和自动刷新行为
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)

# [AI注释] 定义基础模型类
# 继承自AsyncAttrs和DeclarativeBase，支持异步操作和声明式模型定义
class Base(AsyncAttrs, DeclarativeBase):
    pass

# [AI注释] 定义基础混入类
# 提供所有模型共有的字段和功能
class BaseMixin:
    """model的基类,所有model都必须继承"""
    # [AI注释] 主键ID，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # [AI注释] 创建时间，默认为当前时间
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now, comment='创建时间')
    
    # [AI注释] 更新时间，在记录更新时自动更新为当前时间
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now,
                         onupdate=datetime.datetime.now, index=True, comment='更新时间')
    
    # [AI注释] 删除标志，0表示存在，2表示删除
    del_flag = Column(String(1), nullable=False, default='0', server_default=text("'0'"), comment='删除标志（0代表存在 2代表删除）')
    
    # [AI注释] 创建者ID
    create_by = Column(Integer, nullable=False, comment='创建者')
    
    # [AI注释] 部门ID
    dept_id = Column(Integer, nullable=False, comment='部门id')