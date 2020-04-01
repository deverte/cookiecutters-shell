"""A one line summary of the program.

Overall program description (it can consist of several lines).
"""

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.pass_context
@click.option('-t', '--text-option', default='Default value.', help='Text option help.')
def main(ctx, text_option):
    """{{cookiecutter.app_name}} program description."""
    click.echo(f'Text option: {text_option}')
    if ctx.invoked_subcommand is None:
        click.echo('Invoked without subcommand.')
    else:
        click.echo('Invoked with subcommand.\n')

@main.command(help='Command with option help.')
@click.option('--flag-on/--flag-off', default=False, help='Flag option help.')
def copt(flag_on):
    """Command with option description."""
    click.echo(f'Flag: {flag_on}')

@main.command(help='Command with argument help.')
@click.argument('argument')
def carg(argument):
    """Command with argument description."""
    click.echo(f'Argument: {argument}')

main()