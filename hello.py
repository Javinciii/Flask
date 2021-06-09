from flask import Flask
from flask import request
from flask import escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    params = request.form
    if params['username']=='admin' and params['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

# @app.route('/user/<username>')
# def user():
#     return 'welcome'

@app.route('/user/<name>', methods = ['GET', 'POST'])
def user_page(name):
    return 'User page %s' % escape(name)

@app.route('/test_url')
def test_url_for():
    print((url_for('index')))
    print(url_for('user_page', name = '哈哈'))
    print(url_for('test_url_for', num = 2))
    return 'test_url'
