# [AI注释] 导入必要的模块
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from config.database import Base, BaseMixin

# [AI注释] 系统用户模型类
# 继承自Base，表示这是一个数据库模型
class SysUser(Base):
    """
    用户信息表
    """

    # [AI注释] 指定数据库表名
    __tablename__ = 'sys_user'

    # [AI注释] 用户ID，主键，自增
    user_id = Column(Integer, primary_key=True, autoincrement=True, comment='用户ID')
    # [AI注释] 部门ID，外键关联部门表
    dept_id = Column(Integer, default=None, comment='部门ID')
    # [AI注释] 用户账号，用于登录
    user_name = Column(String(30), nullable=False, comment='用户账号')
    # [AI注释] 用户昵称，显示名称
    nick_name = Column(String(30), nullable=False, comment='用户昵称')
    # [AI注释] 用户类型，00表示系统用户
    user_type = Column(String(2), default='00', comment='用户类型（00系统用户）')
    # [AI注释] 用户邮箱
    email = Column(String(50), default='', comment='用户邮箱')
    # [AI注释] 手机号码
    phonenumber = Column(String(11), default='', comment='手机号码')
    # [AI注释] 用户性别，0男1女2未知
    sex = Column(String(1), default='0', comment='用户性别（0男 1女 2未知）')
    # [AI注释] 用户头像地址
    avatar = Column(String(100), default='', comment='头像地址')
    # [AI注释] 用户密码，加密存储
    password = Column(String(100), default='', comment='密码')
    # [AI注释] 账号状态，0正常1停用
    status = Column(String(1), default='0', comment='帐号状态（0正常 1停用）')
    # [AI注释] 删除标志，0存在2删除
    del_flag = Column(String(1), default='0', comment='删除标志（0代表存在 2代表删除）')
    # [AI注释] 最后登录IP地址
    login_ip = Column(String(128), default='', comment='最后登录IP')
    # [AI注释] 最后登录时间
    login_date = Column(DateTime, comment='最后登录时间')
    # [AI注释] 创建者账号
    create_by = Column(String(64), default='', comment='创建者')
    # [AI注释] 创建时间
    create_time = Column(DateTime, comment='创建时间', default=datetime.now())
    # [AI注释] 更新者账号
    update_by = Column(String(64), default='', comment='更新者')
    # [AI注释] 更新时间
    update_time = Column(DateTime, comment='更新时间', default=datetime.now())
    # [AI注释] 备注信息
    remark = Column(String(500), default=None, comment='备注')

# [AI注释] 用户角色关联模型
# 用于维护用户和角色的多对多关系
class SysUserRole(Base):
    """
    用户和角色关联表
    """

    # [AI注释] 指定数据库表名
    __tablename__ = 'sys_user_role'

    # [AI注释] 用户ID，联合主键
    user_id = Column(Integer, primary_key=True, nullable=False, comment='用户ID')
    # [AI注释] 角色ID，联合主键
    role_id = Column(Integer, primary_key=True, nullable=False, comment='角色ID')

# [AI注释] 用户岗位关联模型
# 用于维护用户和岗位的多对多关系
class SysUserPost(Base):
    """
    用户与岗位关联表
    """

    # [AI注释] 指定数据库表名
    __tablename__ = 'sys_user_post'

    # [AI注释] 用户ID，联合主键
    user_id = Column(Integer, primary_key=True, nullable=False, comment='用户ID')
    # [AI注释] 岗位ID，联合主键
    post_id = Column(Integer, primary_key=True, nullable=False, comment='岗位ID')

# [AI注释] 用户微信信息模型
# 继承自Base和BaseMixin，包含基础字段和微信特有字段
class UserWechat(Base, BaseMixin):
    """
    用户微信信息
    """

    # [AI注释] 指定数据库表名
    __tablename__ = 'user_wechat'

    # [AI注释] 关联的用户ID
    user_id = Column(Integer, nullable=False, comment='用户ID')
    # [AI注释] 用户所在城市
    city = Column(String(100), nullable=True, comment='城市')
    # [AI注释] 用户所在国家
    country = Column(String(100), nullable=True, comment='国家')
    # [AI注释] 微信头像URL
    head_img_url = Column(String(255), nullable=True, comment='微信头像')
    # [AI注释] 微信昵称
    nickname = Column(String(255), nullable=True, comment='微信昵称')
    # [AI注释] 微信openid，唯一标识
    openid = Column(String(255), unique=True, nullable=False, comment='openid')
    # [AI注释] 微信unionid
    union_id = Column(String(255), nullable=False, comment='union_id')
    # [AI注释] 用户手机号，唯一标识
    user_phone = Column(String(15), unique=True, nullable=False, comment='手机号')
    # [AI注释] 用户所在省份
    province = Column(String(255), nullable=True, comment='省份')
    # [AI注释] 用户性别
    sex = Column(Integer, nullable=True, comment='性别')
