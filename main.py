from app.cli.command_cli import app as cli_app

# from app.api.web_api import app as api_app
from loguru import logger
import typer


def main():
    # Aquí puedes determinar cómo deseas ejecutar la CLI o el servidor de API
    # Por ejemplo, podrías usar argumentos de línea de comandos para decidir qué iniciar

    # if "web" in typer.argv:  # Si se pasa 'web' en la línea de comandos
    #     logger.info("starting web server")
    #     # import uvicorn
    #     # uvicorn.run(api_app, host="0.0.0.0", port=8000)
    # else:  # Por defecto, se ejecuta la CLI
        logger.info("starting CLI")
        cli_app()


if __name__ == "__main__":
    main()
