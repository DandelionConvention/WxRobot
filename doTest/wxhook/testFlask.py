from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    print(request.headers)
    print(request.stream.read().decode('gbk'))
    return ""


if __name__ == '__main__':
    app.run(port=8880)