from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_bill', methods=['POST'])
def calculate_bill():
    size = request.form['size']
    bill = 0

    if size.lower() == 's':
        bill += 100
    elif size.lower() == 'm':
        bill += 200
    else:
        bill += 300

    add_pepperoni = request.form.get('pepperoni', 'N')
    if add_pepperoni == 'Y':
        if size.lower() == 's':
            bill += 30
        else:
            bill += 50

    extra_cheese = request.form.get('extra_cheese', 'N')
    if extra_cheese == 'Y':
        bill += 20

    return render_template('bill.html', bill=bill)

@app.route('/order', methods=['POST'])
def order():
    size = request.form['size']
    bill = 0

    if size.lower() == 's':
        bill += 100
    elif size.lower() == 'm':
        bill += 200
    else:
        bill += 300

    add_pepperoni = request.form.get('pepperoni', 'N')
    if add_pepperoni == 'Y':
        if size.lower() == 's':
            bill += 30
        else:
            bill += 50

    extra_cheese = request.form.get('extra_cheese', 'N')
    if extra_cheese == 'Y':
        bill += 20

    return render_template('bill.html', bill=bill)


if __name__ == '__main__':
    app.run(debug=True)
