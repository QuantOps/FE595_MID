from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/<name>', methods=['GET', 'POST'])
def aws_flask_app(name):
    if request.method=='GET':
        return "Hello, {}! I'm the AWS_FLASK_APP! \n".format(name)
    elif request.method=='POST':
        user_data = request.form["body"]
        res = {'status': '200'}
        return "Hello, {}! I'm the AWS_FLASK_APP! ".format(name) + "The data that you entered is: {}\n".format(user_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
