from flask import Flask,request

from twilio.rest import Client
authtoken = '0eb85f3f072e3d8b72c0a17f60e51aa7'
sid = 'AC076ed4a3d3c61c5629decf6dbd74bacc'
app = Flask(__name__)
client = Client(sid, authtoken)

@app.route('/', methods = ['GET'])
def name():
    message = client.messages.create(to = 'whatsapp:+919902233996', from_ = 'whatsapp:+14155238886', body = 'hi how are u')
    print(message)
    return '<h1> hello world </h1>'

@app.route('/', methods = ['POST'])
def receive():
    receivedparameters = request.values.get('Body')
    print(receivedparameters)
    return '<Response></Response>'


if __name__ == '__main__':
    print('hello')
    app.run(debug= True)

