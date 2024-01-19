import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/result',methods=['GET'])
def result():
    if request.method=='GET':
        number=request.args.get('num')
        button=request.args.get('math')

        num=int(number)
        if button=='+':
            sq=num+num
        else:
            sq=num-num
        #sq = square(number)
        #return f"sqaure is '{sq}'"
        return render_template('answer.html',num=num,sq=sq)

def square(number):
    return int(number)*int(number)

if __name__=='__main__':
    app.run(debug=True)
