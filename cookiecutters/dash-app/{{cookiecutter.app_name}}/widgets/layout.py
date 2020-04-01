"""{{cookiecutter.app_name}} view."""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# from {{cookiecutter.app_name}}.widgets.{children} import {view_imports}

external_stylesheets = [dbc.themes.BOOTSTRAP]

layout = html.Div(
    children=[
        dcc.Store(id='{{cookiecutter.app_name}}_store', storage_type='memory'),
        # dcc.Store(id='{{cookiecutter.app_name}}_store', storage_type='local'),
        # dcc.Store(id='{{cookiecutter.app_name}}_store', storage_type='session'),

        dbc.Row(
            children=[
                # {view_imports}
            ]
        )
    ],
    id='{{cookiecutter.app_name}}'
)