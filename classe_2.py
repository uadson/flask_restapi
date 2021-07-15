from flask import Flask


app = Flask(__name__)

# Pattern is GET
@app.route('/')
def hello():
    return 'Hello World'

@app.route('/<num>', methods=['GET'])
def count(num):
    return f'The number is: {num}.'

if __name__ == '__main__':
    app.run(debug=True)