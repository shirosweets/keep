import click
from keep.cli import pass_context


@click.command('push', short_help='Pushes the local database to remote.')
@pass_context
def cli(ctx):
    """Saves a new command"""
    cmd = click.prompt('Command : ')
    desc = click.prompt('Description : ')
    print(type(cmd))
    print(type(desc))

    if ctx.verbose:
        ctx.log('Initialized the repository')
