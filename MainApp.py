from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    print('hello world')
    print('How are you?')


if __name__ == "__main__":
    app.run()
