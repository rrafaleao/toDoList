from datetime import datetime
from flask import flash
import re

def validate_task_data(title: str, description: str = None) -> dict:
    """
    Valida os dados de uma tarefa.
    
    Args:
        title: Título da tarefa
        description: Descrição da tarefa
    
    Returns:
        dict: Dicionário com os dados validados e limpos
    
    Raises:
        ValueError: Se algum dado for inválido
    """
    errors = []
    
    # Validação do título
    if not title or not title.strip():
        errors.append("O título da tarefa é obrigatório")
    elif len(title.strip()) > 100:
        errors.append("O título deve ter no máximo 100 caracteres")
    
    # Validação da descrição
    if description and len(description.strip()) > 1000:
        errors.append("A descrição deve ter no máximo 1000 caracteres")
        
    if errors:
        raise ValueError("; ".join(errors))
    
    return {
        'title': title.strip() if title else None,
        'description': description.strip() if description else None,
    }

def format_datetime(dt: datetime, format_str: str = "%d/%m/%Y %H:%M") -> str:
    """
    Formata uma data/hora para string.
    
    Args:
        dt: Objeto datetime
        format_str: Formato desejado
    
    Returns:
        str: Data formatada
    """
    if not dt:
        return ""
    return dt.strftime(format_str)

def flash_success(message: str):
    """Exibe uma mensagem de sucesso."""
    flash(message, "success")

def flash_error(message: str):
    """Exibe uma mensagem de erro."""
    flash(message, "danger")

def flash_warning(message: str):
    """Exibe uma mensagem de aviso."""
    flash(message, "warning")

def flash_info(message: str):
    """Exibe uma mensagem de informação."""
    flash(message, "info")

def sanitize_html(text: str) -> str:
    """
    Remove tags HTML perigosas do texto.
    
    Args:
        text: Texto a ser sanitizado
    
    Returns:
        str: Texto sanitizado
    """
    if not text:
        return ""
    
    # Remove tags script e style
    text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove atributos perigosos
    text = re.sub(r'on\w+\s*=\s*["\'][^"\']*["\']', '', text, flags=re.IGNORECASE)
    text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
    
    return text.strip()