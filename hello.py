from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)

print(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

def make_bold(function_to_do):
    def wrapper_func():
        return f"<b>{function_to_do()}</b>"
    return wrapper_func
def make_emphasis(function_to_do):
    def wrapper_func():
        return f"<em>{function_to_do()}</em>"
    return wrapper_func
def make_underlined(function_to_do):
    def wrapper_func():
        return f"<u>{function_to_do()}</u>"
    return wrapper_func

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "Bye World!"

@app.route('/username/<name>/<int:age>')
def greek(name,age):
    return f"Hi I am {name + str(age)} I am {age} years old!!"


if __name__ == "__main__":
    app.run(debug=True)
