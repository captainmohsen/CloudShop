from flask import Flask, json , render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/',)
def get_status():
  return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/payment', methods=['GET'])
def payment():
    return render_template('login.html')

@app.route('/gadget', methods=['GET'])
def gadget():
    return render_template('login.html')

@app.route('/information', methods=['GET'])
def get_information():
    return render_template('login.html')

@app.route('/ask_question', methods=['GET'])
def ask_question():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True)
