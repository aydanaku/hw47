from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/<test>/') #принимает переменную вместо <test>
# def homepage(test):
#     # return 'Hello world!'
#     test = test.upper()
#     return render_template('index.html', my_var=test)

# @app.route('/')
# def homepage():
#     f = open('goods.txt', 'r', encoding='utf-8')
#     txt = f.readlines()
#     return render_template('index.html', goods=txt)

@app.route('/')
def homepage():
    f = open('goods.xlsx', 'r', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)