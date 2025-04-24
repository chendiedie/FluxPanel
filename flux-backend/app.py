# [AI注释] 导入必要的模块
# uvicorn是一个ASGI服务器实现，用于运行FastAPI应用
import uvicorn
# 从server模块导入app实例和AppConfig配置类
from server import app, AppConfig  # noqa: F401

# [AI注释] 程序入口点
# 当直接运行此脚本时，会执行以下代码
if __name__ == '__main__':
    # [AI注释] 使用uvicorn启动FastAPI应用
    # app: 指定要运行的FastAPI应用实例
    # host: 服务器监听的主机地址
    # port: 服务器监听的端口号
    # workers: 工作进程数，用于处理并发请求
    # reload: 是否启用热重载，开发环境建议开启
    uvicorn.run(
        app='app:app',
        host=AppConfig.app_host,
        port=AppConfig.app_port,
        workers=AppConfig.app_workers,
        reload=AppConfig.app_reload,
    )