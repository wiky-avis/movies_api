import click

from settings.config import Config


@click.group()
def cli():
    pass


@cli.command(help="api")
def api():
    import app

    app.app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)


if __name__ == '__main__':
    cli()
