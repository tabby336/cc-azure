from flask import Flask, jsonify, abort, request, make_response, url_for

from xml.etree import ElementTree
from auth import AzureAuthClient
import requests

app = Flask(__name__, static_url_path = "", static_folder = "static")

client_secret = '41578f022a0841ee83364daf3e0e571c'
auth_client = AzureAuthClient(client_secret)
bearer_token = 'Bearer ' + auth_client.get_access_token()

@app.route('/')
def index():
    return app.send_static_file('index.html')

    
@app.route('/translate', methods=['POST'])
def translate():
    global bearer_token
    print "Am here"
    print request.json

    # Call to Microsoft Translator Service
    headers = {"Authorization ": bearer_token}
<<<<<<< HEAD
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(request.json["text"], request.json["lang"])
=======
    translateUrl = "https://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(request.json["text"], request.json["lang"])
>>>>>>> working

    translationData = requests.get(translateUrl, headers = headers)
    # parse xml return values
    translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
    # display translation
    print "The translation is---> ", translation.text


    return jsonify({"text": translation.text})

if __name__ == '__main__':
    app.run()
