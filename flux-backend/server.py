# [AI注释] 导入必要的模块和工具
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

# [AI注释] 导入项目自定义模块
from config.env import AppConfig
from config.get_db import init_create_table
from config.get_redis import RedisUtil
from config.get_scheduler import SchedulerUtil
from exceptions.handle import handle_exception
from mcp_server.ai_websocket import init_ai_websocket
from middlewares.handle import handle_middleware
from router import router_manager
from sub_applications.handle import handle_sub_applications
from utils.common_util import worship
from utils.log_util import logger
from fastapi import FastAPI, Request
from utils.response_util import ResponseUtil

# [AI注释] 定义应用生命周期管理函数
# 使用@asynccontextmanager装饰器来管理FastAPI应用的生命周期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # [AI注释] 应用启动时的初始化操作
    logger.info(f'{AppConfig.app_name}开始启动')
    worship()  # 执行一些初始化操作
    await init_create_table()  # 初始化数据库表
    app.state.redis = await RedisUtil.create_redis_pool()  # 创建Redis连接池
    await RedisUtil.init_sys_dict(app.state.redis)  # 初始化系统字典
    await RedisUtil.init_sys_config(app.state.redis)  # 初始化系统配置
    await SchedulerUtil.init_system_scheduler()  # 初始化系统调度器
    await init_ai_websocket(app)  # 初始化AI WebSocket连接
    # await mcp_starter.start(app)  # 注释掉的MCP启动器
    handle_sub_applications(app)  # 挂载子应用
    logger.info(f'{AppConfig.app_name}启动成功')
    yield
    # [AI注释] 应用关闭时的清理操作
    await RedisUtil.close_redis_pool(app)  # 关闭Redis连接池
    await SchedulerUtil.close_system_scheduler()  # 关闭系统调度器

# [AI注释] 创建FastAPI应用实例
# 配置应用的基本信息，包括名称、描述、版本等
app = FastAPI(
    title=AppConfig.app_name,
    description=f'{AppConfig.app_name}接口文档',
    version=AppConfig.app_version,
    lifespan=lifespan,
    root_path=AppConfig.app_root_path,
)

# [AI注释] 定义HTTP中间件
# 用于拦截和处理所有HTTP请求
@app.middleware("http")
async def block_post_requests(request: Request, call_next):
    # [AI注释] 演示环境下的请求限制
    # 这里注释掉了对POST等修改请求的限制
    # if request.url.path not in ("/logout", "/login") and request.method in ("POST", "PUT", "PATCH", "DELETE"):
    #     return ResponseUtil.error(msg="演示环境，暂不允许修改数据")
    # 继续处理其他请求
    response = await call_next(request)
    return response

# [AI注释] 加载各种中间件和处理器
handle_middleware(app)  # 加载自定义中间件
handle_exception(app)  # 加载全局异常处理

# [AI注释] 注册所有路由
app.include_router(router_manager.register_router())

