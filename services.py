from models import Task
from typing import List, Optional

class TaskService:
    """Serviço para gerenciar operações relacionadas às tarefas."""
    
    @staticmethod
    def get_all_tasks() -> List[Task]:
        """Retorna todas as tarefas ordenadas por data de criação."""
        return Task.get_all_ordered()
    
    @staticmethod
    def get_task_by_id(task_id: int) -> Task:
        """Busca uma tarefa pelo ID."""
        return Task.get_by_id(task_id)
    
    @staticmethod
    def create_task(title: str, description: str = None, emoji: str = "📘") -> Task:
        """Cria uma nova tarefa."""
        if not title or not title.strip():
            raise ValueError("O título da tarefa é obrigatório")
        
        task = Task(
            title=title.strip(),
            description=description.strip() if description else None,
            emoji=emoji or "📘"
        )
        task.save()
        return task
    
    @staticmethod
    def update_task(task_id: int, title: str = None, description: str = None, emoji: str = None) -> Task:
        """Atualiza uma tarefa existente."""
        task = Task.get_by_id(task_id)
        
        if title is not None and not title.strip():
            raise ValueError("O título da tarefa é obrigatório")
        
        task.update(
            title=title.strip() if title else None,
            description=description.strip() if description else None,
            emoji=emoji
        )
        return task
    
    @staticmethod
    def delete_task(task_id: int) -> bool:
        """Remove uma tarefa."""
        task = Task.get_by_id(task_id)
        task.delete()
        return True
    
    @staticmethod
    def search_tasks(query: str) -> List[Task]:
        """Busca tarefas por título ou descrição."""
        if not query or not query.strip():
            return TaskService.get_all_tasks()
        
        search_term = f"%{query.strip()}%"
        return Task.query.filter(
            (Task.title.ilike(search_term)) | 
            (Task.description.ilike(search_term))
        ).order_by(Task.created_at.desc()).all()
    
    @staticmethod
    def get_task_count() -> int:
        """Retorna o número total de tarefas."""
        return Task.query.count()