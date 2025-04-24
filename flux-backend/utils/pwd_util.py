# [AI注释] 导入密码加密上下文
from passlib.context import CryptContext

# [AI注释] 创建密码加密上下文实例
# 使用bcrypt算法进行密码加密，标记auto为不推荐使用的算法
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# [AI注释] 密码工具类
# 提供密码加密和验证的功能
class PwdUtil:
    """
    密码工具类
    """

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        """
        工具方法：校验当前输入的密码与数据库存储的密码是否一致

        :param plain_password: 当前输入的密码（明文）
        :param hashed_password: 数据库存储的密码（哈希值）
        :return: 校验结果，True表示密码匹配，False表示不匹配
        """
        # [AI注释] 使用passlib的verify方法验证密码
        # 该方法会自动处理salt和哈希算法
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, input_password):
        """
        工具方法：对当前输入的密码进行加密

        :param input_password: 输入的密码（明文）
        :return: 加密后的密码（哈希值）
        """
        # [AI注释] 使用passlib的hash方法加密密码
        # 该方法会自动生成salt并使用bcrypt算法进行加密
        return pwd_context.hash(input_password)

# [AI注释] 测试代码
# 用于验证密码加密和验证功能是否正常工作
if __name__ == '__main__':
    # [AI注释] 测试密码加密
    # 对相同的密码进行两次加密，结果应该不同（因为使用了不同的salt）
    print(PwdUtil.get_password_hash("admin123"))
    print(PwdUtil.get_password_hash("admin123"))
    
    # [AI注释] 测试密码验证
    # 验证明文密码和哈希值是否匹配
    hash_pwd = '$2a$10$7JB720yubVSZvUI0rEqK/.VqGOZTH.ulu33dHOiBE8ByOhJIrdAu2'
    print(PwdUtil.verify_password('admin123', hash_pwd))