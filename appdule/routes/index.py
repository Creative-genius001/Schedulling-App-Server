from flask import Flask
app = Flask(__name__)


#create a new appointment route
@app.route('/create', methods=['POST'])
def create():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True)