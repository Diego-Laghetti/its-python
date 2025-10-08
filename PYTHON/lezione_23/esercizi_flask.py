from flask import Flask, url_for

app = Flask(__name__)

#flask --app esercizi_flask run --debug --host 127.0.0.1 --port 5000

"""
1. Generazione link interni

Usare url_for per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).

"""

@app.route("/errore")
def errore():
    return 1 / 0  # divisione per zero

@app.route("/about")
def about() -> str:
    return "<div>Ciao sto facendo gli esercizi di flask 🧐🧐🧐</div>"


@app.route('/user/<nome>')
def user(nome):
    return f"<h3>Benvenuto, {nome}!</h3>"


@app.route('/square/<int:n>')
def square(n):
    return f"<h3>{n**2}</h3>"


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return f"<h3>{a+b}</h3>"


@app.route('/')
def home() -> str:
 return f"""<ul><li><a href="{url_for('about')}">about</a></li>
            <li><a href="{url_for('user', nome = 'Roberto')}">Visita il profilo di Roberto</a></li>
            <li><a href="{url_for('square', n=3)}">Scopri quanto fa 3x3</a></li>
            <li><a href="{url_for('sum', a=2, b=2)}">Scopri quanto fa 2+2</a></li></ul>"""


"""
2. Navigazione dinamica

Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.
"""


@app.route('/elenco')
def elenco() -> str:
    return f"""<ul>
    <li><a href="{url_for('user', nome = 'Peppe 1')}">Visita il profilo di Peppe 1</a></li>
    <li><a href="{url_for('user', nome = 'Peppe 2')}">Visita il profilo di Peppe 2</a></li>
    <li><a href="{url_for('user', nome = 'Peppe 3')}">Visita il profilo di Peppe 3</a></li>
    <li><a href="{url_for('user', nome = 'Peppe 4')}">Visita il profilo di Peppe 4</a></li></ul>"""


"""
3. Mini blog

Definire route /post/<int:id> che restituisca un articolo fittizio.

Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.
"""


@app.route("/post/<int:id>")
def post(id) -> str:
    return f"<h3>Ciao questo è il post numero {id} 🤓</h3>"


@app.route('/posts')
def posts() -> str:
    return f"""<ul>
    <li><a href="{url_for('post', id = 1)}">Post 1</a></li>
    <li><a href="{url_for('post', id = 2)}">Post 2</a></li>
    <li><a href="{url_for('post', id = 3)}">Post 3</a></li>
    <li><a href="{url_for('post', id = 4)}">Post 4</a></li></ul>"""
