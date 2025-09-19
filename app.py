from flask import Flask
from config import Config
from models import db
from routes import main

def create_app():
    """Factory function para criar a aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa o banco de dados
    db.init_app(app)
    
    # Registra as rotas
    app.register_blueprint(main)
    
    # Cria as tabelas no banco de dados
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)