import click


@click.group()
def cli():
    pass


@cli.command(help="api")
def api():
    import app

    app.app.run(host="127.0.0.1", port=8000, debug=True)


if __name__ == '__main__':
    cli()
