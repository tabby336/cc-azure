from flask import Flask, jsonify, abort, request, make_response, url_for

# from xml.etree import ElementTree
# from auth import AzureAuthClient
# import requests

app = Flask(__name__, static_url_path = "", static_folder = "static")

# client_secret = '41578f022a0841ee83364daf3e0e571c'
# auth_client = AzureAuthClient(client_secret)
bearer_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzY29wZSI6Imh0dHBzOi8vYXBpLm1pY3Jvc29mdHRyYW5zbGF0b3IuY29tLyIsInN1YnNjcmlwdGlvbi1pZCI6ImQxNWY3ODMwMjU4ZDQxZWQ5ZjcwODIzZWZlNzczYzI1IiwicHJvZHVjdC1pZCI6IlRleHRUcmFuc2xhdG9yLkYwIiwiY29nbml0aXZlLXNlcnZpY2VzLWVuZHBvaW50IjoiaHR0cHM6Ly9hcGkuY29nbml0aXZlLm1pY3Jvc29mdC5jb20vaW50ZXJuYWwvdjEuMC8iLCJhenVyZS1yZXNvdXJjZS1pZCI6Ii9zdWJzY3JpcHRpb25zL2ZlYjhmMjcyLWI1ZTItNGJhMC1hZDk2LTViZTY1Y2Y5MzJiYS9yZXNvdXJjZUdyb3Vwcy9teVJlc291cmNlR3JvdXAvcHJvdmlkZXJzL01pY3Jvc29mdC5Db2duaXRpdmVTZXJ2aWNlcy9hY2NvdW50cy9jYy1henVyZS10cmFuc2xhdGUtdGV4dCIsImlzcyI6InVybjptcy5jb2duaXRpdmVzZXJ2aWNlcyIsImF1ZCI6InVybjptcy5taWNyb3NvZnR0cmFuc2xhdG9yIiwiZXhwIjoxNDk1MjY0NjYyfQ.cNlfPgjrYMRsqNo8B3Ujq9xoBL4sTVX8HawCPhF-_z8'

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
    translateUrl = "https://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(request.json["text"], request.json["lang"])

    translationData = requests.get(translateUrl, headers = headers)
    # parse xml return values
    translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
    # display translation
    print "The translation is---> ", translation.text


    return jsonify({"text": translation.text})

if __name__ == '__main__':
    print bearer_token
    app.run()
