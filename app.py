from flask import Flask,request

from twilio.rest import Client
authtoken = '61220712d90504790e02b0512ba82b05'
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
    if receivedparameters.casefold() == "hi":
        messagefrom = str(request.values.get('From'))
        message1 = client.messages.create(to = messagefrom, from_ = 'whatsapp:+14155238886', body = 'hi how are u')
        print(message1)
    elif receivedparameters.casefold() == "iam fine":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'good going') 
        
    elif receivedparameters.casefold() == "iam not fine":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'how can i help u')                
    
    elif receivedparameters.casefold() == "who is your best friend":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'rak,var,tej,sush')
    elif receivedparameters.casefold() == "tell about rak":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'A big fan of Jimin and jhope')
    elif receivedparameters.casefold() == "tell about var":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'her boyfriend is in korea')
    elif receivedparameters.casefold() == "tell about tej":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'jin is her boy friend')
    elif receivedparameters.casefold() == "tell about sush":
        message2 = client.messages.create(to = str(request.values.get('From')), from_ = 'whatsapp:+14155238886', body = 'she is a non korean fan')
    
    return '<Response></Response>'


if __name__ == '__main__':
    print('hello')
    app.run(debug= True)

