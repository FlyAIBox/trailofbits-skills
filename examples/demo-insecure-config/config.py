"""
演示配置文件 - 包含多个不安全的默认值
用于insecure-defaults skill的演示

⚠️  警告: 这是一个故意包含安全问题的示例文件,仅用于教学目的!
         请勿在实际项目中使用这些配置!
"""

import os
from datetime import timedelta

# ============================================================================
# 🚨 问题1: 硬编码的数据库凭证
# ============================================================================
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://admin:admin@localhost/mydb'  # ❌ FAIL-OPEN
)

# ============================================================================
# 🚨 问题2: 硬编码的JWT密钥
# ============================================================================
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-123')  # ❌ FAIL-OPEN
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE = int(os.getenv('TOKEN_EXPIRE', '30'))

# ============================================================================
# 🚨 问题3: CORS允许所有来源
# ============================================================================
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')  # ❌ FAIL-OPEN

# ============================================================================
# 🚨 问题4: 弱密码哈希算法
# ============================================================================
HASH_ALGORITHM = os.getenv('HASH_ALGO', 'md5')  # ❌ WEAK DEFAULT

# ============================================================================
# 🚨 问题5: DEBUG模式默认开启
# ============================================================================
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')  # ❌ FAIL-OPEN
SENTRY_DSN = os.getenv('SENTRY_DSN', '')

# ============================================================================
# 🚨 问题6: 用户注册默认开启(如果是内部工具,应该关闭)
# ============================================================================
ENABLE_REGISTRATION = os.getenv('ENABLE_REGISTRATION', 'true') == 'true'  # ⚠️  REVIEW

# ============================================================================
# 🚨 问题7: 邮箱验证默认关闭
# ============================================================================
REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'false') == 'true'  # ⚠️  REVIEW

# ============================================================================
# 🚨 问题8: API限流默认关闭
# ============================================================================
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'false') == 'true'  # ⚠️  REVIEW
RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_NUM', '1000'))

# ============================================================================
# ✅ 好的配置: SSL验证默认开启
# ============================================================================
VERIFY_SSL = os.getenv('VERIFY_SSL', 'True').lower() == 'true'
SSL_CERT_PATH = os.getenv('SSL_CERT')

# ============================================================================
# 其他配置
# ============================================================================
# Redis配置
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')  # 空密码也是问题!

# 外部API密钥
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', 'sk_test_default123')  # ❌ 硬编码测试密钥
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', '')

# AWS配置
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'AKIAIOSFODNN7EXAMPLE')  # ❌ 示例密钥
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY')

# 会话配置
SESSION_COOKIE_SECURE = os.getenv('SESSION_SECURE', 'False').lower() == 'true'  # ❌ 默认不安全
SESSION_COOKIE_HTTPONLY = True  # ✅ 这个是好的
SESSION_COOKIE_SAMESITE = os.getenv('SESSION_SAMESITE', 'None')  # ❌ 默认最宽松

# Admin配置
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')  # ❌ 默认用户名
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')  # ❌ 默认密码
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')

# ============================================================================
# 修复建议(仅供参考,实际使用时请去掉注释)
# ============================================================================

"""
# ✅ 正确的配置方式:

# 1. 敏感配置必须显式设置,否则崩溃
DATABASE_URL = os.environ['DATABASE_URL']
SECRET_KEY = os.environ['SECRET_KEY']
CORS_ORIGINS = os.environ['CORS_ORIGINS'].split(',')

# 2. 加密算法不应该可配置,硬编码使用强算法
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 3. 安全配置使用安全的默认值
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')  # 默认WARNING而非DEBUG
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT', 'true') == 'true'  # 默认开启
REQUIRE_EMAIL_VERIFICATION = os.getenv('REQUIRE_EMAIL_VERIFICATION', 'true') == 'true'  # 默认开启

# 4. 启动时验证配置
def validate_config():
    if len(SECRET_KEY) < 32:
        raise ValueError("SECRET_KEY must be at least 32 characters")
    
    if not DATABASE_URL.startswith(('postgresql://', 'mysql://')):
        raise ValueError("Invalid DATABASE_URL format")
    
    if os.getenv('ENVIRONMENT') == 'production':
        if CORS_ORIGINS == ['*']:
            raise ValueError("CORS_ORIGINS cannot be '*' in production")
        
        if not SESSION_COOKIE_SECURE:
            raise ValueError("SESSION_COOKIE_SECURE must be True in production")

# 在应用启动时调用
validate_config()
"""

