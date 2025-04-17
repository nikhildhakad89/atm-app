from flask import Flask, request, render_template_string

app = Flask(__name__)
balance = 0

@app.route('/')
def home():
    return render_template_string("""
        <h1>Simple ATM</h1>
        <form action="/deposit" method="post">
            <input type="number" name="amount" placeholder="Deposit Amount">
            <button type="submit">Deposit</button>
        </form>
        <form action="/withdraw" method="post">
            <input type="number" name="amount" placeholder="Withdraw Amount">
            <button type="submit">Withdraw</button>
        </form>
        <p>Current Balance: {{balance}}</p>
    """, balance=balance)

@app.route('/deposit', methods=['POST'])
def deposit():
    global balance
    balance += int(request.form['amount'])
    return home()

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    balance -= int(request.form['amount'])
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
