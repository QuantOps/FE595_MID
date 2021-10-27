from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/<name>', methods=['GET', 'POST'])
def aws_flask_app(name):
    user_data = request.form["body"]
    return "Hello, {}!, I'm the AWS_FLASK_APP!".format(name) + "The data that you entered is: {}\n".format(user_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
