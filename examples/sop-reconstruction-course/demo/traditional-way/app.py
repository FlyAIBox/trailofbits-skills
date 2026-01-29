"""
传统方式开发的用户注册API（存在多个问题）

这个示例展示了在没有Skill指导下，开发人员可能写出的问题代码。
"""

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 问题1: 数据库连接没有池化，每次都创建新连接
def get_db():
    conn = sqlite3.connect('users.db')
    return conn

# 问题2: 没有表结构初始化
# 问题3: 没有索引优化

@app.route('/register', methods=['POST'])
def register():
    # 问题4: 没有输入验证
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    # 问题5: 没有检查必填字段
    # 问题6: 没有邮箱格式验证
    # 问题7: 没有密码强度检查
    
    conn = get_db()
    cursor = conn.cursor()
    
    # 问题8: 密码明文存储 🔥🔥🔥
    # 问题9: SQL注入风险（虽然用了参数化，但其他地方可能有）
    # 问题10: 没有用户名唯一性检查（应该先SELECT）
    
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        conn.commit()
        user_id = cursor.lastrowid
        
        # 问题11: 返回了敏感信息（密码）
        # 问题12: 没有返回token
        return jsonify({
            'user_id': user_id,
            'username': username,
            'password': password  # 🔥 绝对不应该返回密码！
        })
    
    except sqlite3.IntegrityError:
        # 问题13: 错误消息泄露信息（可以用于用户名枚举）
        return jsonify({'error': 'Username already exists'}), 400
    
    except Exception as e:
        # 问题14: 直接返回异常信息（信息泄露）
        return jsonify({'error': str(e)}), 500
    
    finally:
        # 问题15: 连接没有在异常时正确关闭
        conn.close()

# 问题16: 没有日志记录
# 问题17: 没有速率限制（可被暴力注册攻击）
# 问题18: 没有单元测试
# 问题19: 没有类型注解
# 问题20: 没有文档字符串

if __name__ == '__main__':
    # 问题21: Debug模式在生产环境开启 🔥
    app.run(debug=True, host='0.0.0.0')  # 暴露在公网

