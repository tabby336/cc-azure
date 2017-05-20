from flask import Flask, jsonify, abort, request, make_response, url_for

from xml.etree import ElementTree
from auth import AzureAuthClient
import requests

app = Flask(__name__, static_url_path = "", static_folder = "static")


@app.route('/')
def index():
    return app.send_static_file('index.html')

    
@app.route('/translate', methods=['POST'])
def translate():
    # global bearer_token
    # print bearer_token
    print "Am here"
    print request.json

    client_secret = '41578f022a0841ee83364daf3e0e571c'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    print bearer_token


    # Call to Microsoft Translator Service
    headers = {"Authorization ": bearer_token}
    print request.json["text"]
    translateUrl = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}'.format(request.json["text"], "en")
    

    translationData = requests.get(translateUrl, headers = headers)
    print translationData
    # parse xml return values
    translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
    print dir(translation)
    print vars(translation)
    # display translation
    print "The translation is---> ", translation.text


    return jsonify({"text": translation.text})

if __name__ == '__main__':
    # global bearer_token
    # print bearer_token
    app.run()
