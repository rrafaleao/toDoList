import os

class Config:
    """Classe de configuração da aplicação."""
    
    # Chave secreta para sessões e flash messages
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cr3t_k3y'
    
    # Configuração do banco de dados
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(basedir, "tasks.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações adicionais
    DEBUG = True