from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'mi_contraseña_secreta'  # Cambia esto en producción

# Simulación de una base de datos de usuarios
users = {
    'ronaldo': 'ronaldo1',
    'user2': 'password2'
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verificar usuario
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        flash('Nombre de usuario o contraseña incorrectos')
        return redirect(url_for('home'))


@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
