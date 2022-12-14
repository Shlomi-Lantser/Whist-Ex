from flask import Flask
from flask import Blueprint
import socket

view = Blueprint('view' , __name__)

@view.route('/')
def homePage():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    returning = "<h1>Hello welcome to my web app , The instance IP Address is: <h1>" + IPAddr
    return returning


def create_app():
    app = Flask(__name__)
    app.register_blueprint(view)
    return app

app = create_app()


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
