from flask import Flask, render_template, request, redirect, url_for, flash, session
from services.auth_service import register_user, login_user, list_users, delete_user
from db import create_tables
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Chave para sessões e flash messages

def create_app():
    """Inicializa a aplicação e cria as tabelas"""
    create_tables.create_tables()
    return app

# Cria as tabelas ao iniciar
create_app()

@app.route('/')
def index():
    """Redireciona para o dashboard se logado, senão para login"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        password = request.form.get('password')
        
        if not identifier or not password:
            flash('Preencha todos os campos.', 'danger')
            return redirect(url_for('login'))
        
        ok, name = login_user(identifier, password)
        if ok:
            session['user_id'] = True  # Simplificado - idealmente use o ID real
            session['user_name'] = name
            session['user_login'] = identifier
            session['is_admin'] = True  # Simplificado - implemente sua lógica de admin
            flash(f'Bem-vindo, {name}!', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Login ou senha inválidos.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Página de registro de novo usuário"""
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        
        if not all([name, login, password]):
            flash('Preencha todos os campos.', 'danger')
            return redirect(url_for('register'))
        
        if register_user(name, login, password):
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
        
        flash('Login já existe. Escolha outro.', 'danger')
        return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard principal - requer login"""
    if 'user_id' not in session:
        flash('Faça login para continuar.', 'danger')
        return redirect(url_for('login'))
    
    users = list_users()
    return render_template('dashboard.html', 
                         users=users,
                         total_users=len(users),
                         active_users=len(users))  # Simplificado

@app.route('/logout')
def logout():
    """Encerra a sessão do usuário"""
    session.clear()
    flash('Você saiu do sistema.', 'success')
    return redirect(url_for('login'))

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    """Exclui um usuário (requer admin)"""
    if 'user_id' not in session or not session.get('is_admin'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('dashboard'))
    
    if delete_user(user_id):
        flash('Usuário excluído com sucesso.', 'success')
    else:
        flash('Erro ao excluir usuário.', 'danger')
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    # Em produção, remova debug=True e use um servidor WSGI apropriado
    app.run(debug=True)