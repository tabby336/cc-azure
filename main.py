from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "", static_folder = "static")


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    # global bearer_token
    # print bearer_token
    app.run()
