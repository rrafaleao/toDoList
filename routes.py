from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Task

# Blueprint para as rotas principais
main = Blueprint('main', __name__)

@main.route("/")
def index():
    """Página inicial que lista todas as tarefas."""
    tasks = Task.get_all_ordered()
    return render_template("index.html", tasks=tasks)

@main.route("/add", methods=["GET", "POST"])
def add_task():
    """Adiciona uma nova tarefa."""
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        
        # Validação simples
        if title:
            try:
                task = Task(
                    title=title,
                    description=description,
                )
                task.save()
                flash("Tarefa adicionada com sucesso!", "success")
                return redirect(url_for("main.index"))
            except Exception as e:
                flash(f"Erro ao adicionar tarefa: {str(e)}", "danger")
        else:
            flash("O título da tarefa é obrigatório.", "danger")
    
    tasks = Task.query.all()
    return render_template("add_task.html", tasks=tasks)

@main.route("/task/<int:task_id>", methods=["GET", "POST"])
def task_detail(task_id):
    """Exibe os detalhes da tarefa e permite edição."""
    task = Task.get_by_id(task_id)

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")

        if title:
            try:
                task.update(title=title, description=description, )
                flash("Tarefa atualizada com sucesso!", "success")
                return redirect(url_for("main.index"))
            except Exception as e:
                flash(f"Erro ao atualizar tarefa: {str(e)}", "danger")
        else:
            flash("O título da tarefa é obrigatório.", "danger")

    tasks = Task.query.all()
    return render_template("task_detail.html", task=task, tasks=tasks)

@main.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Exclui uma tarefa."""
    task = Task.get_by_id(task_id)
    try:
        task.delete()
        flash("Tarefa excluída com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao excluir tarefa: {str(e)}", "danger")
    
    return redirect(url_for("main.index"))