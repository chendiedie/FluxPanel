# [AI注释] 导入数据库相关模块
from config.database import async_engine, AsyncSessionLocal, Base
from utils.log_util import logger

# [AI注释] 获取数据库会话的依赖函数
# 使用FastAPI的依赖注入系统，为每个请求提供独立的数据库会话
async def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接

    :return: 数据库会话对象
    """
    # [AI注释] 使用异步上下文管理器创建数据库会话
    # 确保会话在使用完毕后自动关闭
    async with AsyncSessionLocal() as current_db:
        yield current_db

# [AI注释] 初始化数据库表结构
# 在应用启动时执行，创建所有定义的数据表
async def init_create_table():
    """
    应用启动时初始化数据库连接

    :return: None
    """
    # [AI注释] 记录初始化开始
    logger.info('初始化数据库连接...')
    
    # [AI注释] 使用异步上下文管理器创建数据库连接
    # 执行所有模型类的create_all方法，创建对应的数据表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # [AI注释] 记录初始化完成
    logger.info('数据库连接成功')
