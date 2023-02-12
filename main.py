from ast import Return
from crypt import methods
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/discount',methods = ['POST'])
def discount():
    if request.method == 'POST':
        item1 = int(request.form['item1'])
        item2 = int(request.form['item2'])
        item3 = int(request.form['item3'])
        item4 = int(request.form['item4'])
        item5 = int(request.form['item5'])
        result = item1+item2+item3+item4+item5
        discount = 0

        if result <= 1000:
            rate = 10
            discount = .9 * result
        elif result > 1000 and result <= 2000:
            rate = 20
            discount = .8 * result
        else:
            rate = 30
            discount = .7 * result
    
    return render_template('results.html', result=[discount,rate,result])

if __name__ == '__main__':
    app.run(host='127.0.0.1')
