from flask import Flask

app = Flask(__name__) #istanza della classe
app.run(debug=True, host='127.0.0.1', port=5000)
#In production, set debug to False