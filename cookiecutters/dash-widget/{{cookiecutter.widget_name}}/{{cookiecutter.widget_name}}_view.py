"""{{cookiecutter.widget_name}} view."""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# from {app_name}.widgets.{parents}.{{cookiecutter.widget_name}}.{children} import {view_imports}

layout = html.Div(
    children=[
        dcc.Store(id='{{cookiecutter.widget_name}}_store', storage_type='memory'),
        # dcc.Store(id='{{cookiecutter.widget_name}}_store', storage_type='local'),
        # dcc.Store(id='{{cookiecutter.widget_name}}_store', storage_type='session'),

        dbc.Row(
            children=[
                # {view_imports}
            ]
        )
    ],
    id='{{cookiecutter.widget_name}}'
)