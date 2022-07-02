from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    result = var_1 / 21.3
    print(result)
    volume = round(result, 2) * 0.01
    commission = volume * 100
    goal = commission * 2
    
    entry = result
    return render_template('result.html', entry=entry, volume=round(volume, 2), commission=int(commission), goal=int(goal))

if __name__ == '__main__':
    app.run(debug=True)