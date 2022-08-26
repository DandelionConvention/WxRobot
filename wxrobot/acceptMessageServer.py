from flask import Flask,request
from .Messagedelivery import Messages

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    message = request.stream.read().decode('gbk')
    print(f'accept -> :{message}')
    Messages(message).handMessage()
    return ""

"""
    后续使用celer分布式
"""

# if __name__ == '__main__':
#     # redis_pool = redis.ConnectionPool(host='127.0.0.1', port = 6379, password = '123', db = 7)
#     # redis_conn = redis.Redis(connection_pool=redis_pool)
#     app.run(port=8880)