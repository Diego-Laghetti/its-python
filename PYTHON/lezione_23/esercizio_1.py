from flask import Flask, url_for

app = Flask(__name__) #istanza della classe
'''app.run(debug=True) #fa partire il server (l'app)'''

#path statico
@app.route('/') 
def home() -> str: #funzione per definire l'home page
    return "<h3>Hello world!</h3>"

#path dinamico (url dinamico)
@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age: int) -> str:
    return f"Profilo di {username}, età: {age}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='playdido', age= 20))
