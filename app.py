from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get('PORT', 5000)))
