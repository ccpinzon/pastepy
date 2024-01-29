import typer

from app.core.manager_handler import ClipboardManager
from loguru import logger

app = typer.Typer()
manager = ClipboardManager()


@app.command()
def ls(limit: int = typer.Option(10, help="Number of entries to list")):
    """
    List the most recent entries in the clipboard history.
    """
    entries = manager.get_recent_entries(limit)
    for entry in entries:
        typer.echo(f"{entry.timestamp} - {entry.content}")


@app.command()
def add(
    content: str,
    app_name: str = typer.Option(
        "No app", help="Name of the application that added the entry"
    ),
):
    """
    Add a new entry to the clipboard history.
    """
    logger.info("Adding new entry {} from app {}", content, app_name)
    manager.add_new_entry(content, app_name)
    typer.echo(f"Added new entry: {content}, from application: {app_name}")


if __name__ == "__main__":
    app()
