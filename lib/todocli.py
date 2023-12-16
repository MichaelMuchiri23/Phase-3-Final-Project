import typer
from rich.console import Console
from rich.table import Table
from main import query_todo

console = Console()

app = typer.Typer()

@app.command()
def add(title:str, description:str, category_id:int, tag_id:int):
    typer.echo(f"adding {title}, {description}, {category_id}, {tag_id}")
    todo = [title, description, category_id, tag_id]
    query_todo.create(todo)
    show()

@app.command()
def delete(task_id: int):
    result = query_todo.delete_task(task_id)
    if result is True:
        typer.echo(f"Task with ID {task_id} deleted successfully.")
        show()
    else:
        typer.echo(result)  # Print the error message if the task was not found

@app.command()
def update(task_id: int, title: str = None, description: str = None, category_id: int = None, tag_id: int = None):
    query_todo.update_task(task_id, title, description, category_id, tag_id)
    show()

@app.command() 
def show():
    console.print("[bold magenta]Todos[/bold magenta]!")

    table = Table(show_header=True, header_style="bold red")
    table.add_column("#", style="dim", width=6 )
    table.add_column("Todo", min_width=20, style="cyan")
    table.add_column("Description", min_width=12, justify="right", style="magenta")
    table.add_column("Category", min_width=12, justify="right", style="white")
    table.add_column("Status of task", min_width=12, justify="right", style="green")


    all_tasks=query_todo.fetch_all()
    for task in all_tasks:
        table.add_row(*task)
    
    console.print(table)
    console.print(query_todo.fetch_all())
   

if __name__ == "__main__":
    app()