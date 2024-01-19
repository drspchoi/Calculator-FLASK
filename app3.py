from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index3.html')


@app.route('/result', methods=['GET'])
def result():
    if request.method == 'GET':
        expression = request.args.get('expression', '')

        try:
            result = eval(expression)
        except Exception as e:
            result = "Error: " + str(e)

        return render_template('index3.html', num=expression, sq=result, calculation_success=True)


if __name__ == '__main__':
    app.run(debug=True)