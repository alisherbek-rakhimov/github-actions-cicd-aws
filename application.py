from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@application.route('/help')
def helppage():
    return '<h1>Help Page!</h1>'


@application.route('/user')
def usermain_page():
    return "User's Main Page!"


@application.route('/user/<username>')
def show_user_page(username: str):
    return f"{username.upper()}'s Main Page!"


@application.route('/path/<path:subpath>')
def print_subpath(subpath):
    return f"subpath is: {subpath}!"


if __name__ == '__main__':
    # app.debug = True
    application.run()
