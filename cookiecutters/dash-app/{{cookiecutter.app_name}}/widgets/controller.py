"""{{cookiecutter.app_name}} controller."""

import dash

# import dash_html_components as html
# import dash_core_components as dcc
# import dash_bootstrap_components as dbc

from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

from {{cookiecutter.app_name}}.app import app

@app.callback(
    Output('output_component_id', 'output_component_property'),
    [Input('input_component_id', 'input_component_property')],
    [State('state_component_id', 'state_component_property')]
)
def {{cookiecutter.app_name}}_callback(input_component_property_data, state_component_property_data):
    """A One line summary of the function in descriptive style (e.g. `fetches...`, not `fetch...`)

    Overall function description (it can consist of several lines).

    Args:
        arg: An `arg` description.
        *args: An `*args` description.
        **kwargs: A `**kwargs` description.

    Returns:
        Returns description (obligatory if exists). For
        example (optional):

        {'some_key_1': 'Some value 1',
         'some_key_2': 'Some value 2'}

    Raises:
        SomeException: A `SomeException` description.
    """
    return output_component_property_data