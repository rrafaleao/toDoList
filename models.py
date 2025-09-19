from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Instância do SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    """Modelo para representar uma tarefa no banco de dados."""
    
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
    
    def to_dict(self):
        """Converte o objeto Task para dicionário."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def get_all_ordered(cls):
        """Retorna todas as tarefas ordenadas por data de criação (mais recentes primeiro)."""
        return cls.query.order_by(cls.created_at.desc()).all()
    
    @classmethod
    def get_by_id(cls, task_id):
        """Busca uma tarefa pelo ID."""
        return cls.query.get_or_404(task_id)
    
    def save(self):
        """Salva a tarefa no banco de dados."""
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e
    
    def update(self, title=None, description=None):
        """Atualiza os dados da tarefa."""
        try:
            if title is not None:
                self.title = title
            if description is not None:
                self.description = description
            self.updated_at = datetime.utcnow()
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e
    
    def delete(self):
        """Remove a tarefa do banco de dados."""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e