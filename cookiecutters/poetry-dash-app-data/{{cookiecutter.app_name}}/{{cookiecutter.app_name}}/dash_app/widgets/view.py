"""{{cookiecutter.app_name}} view."""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

## Styles
external_stylesheets = [] # DO NOT DELETE!

## Views
## Insert here children views.
# from {{cookiecutter.app_name}}.dash_app.widgets.{children}.{child} import view_{child}

view = html.Div(
    [
        ## Data
        dcc.Store(id='extra_block_store', storage_type='memory'),
        # dcc.Store(id='{{cookiecutter.app_name}}_store', storage_type='memory'),
        # dcc.Store(id='{{cookiecutter.app_name}}_store', storage_type='local'),
        # dcc.Store(id='{{cookiecutter.app_name}}_store', storage_type='session'),

        ## View
        ## Insert here your widgets layout `view_{child}`
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div('{{cookiecutter.app_name}}', id='header', className='display-1')
                    ],
                    width={"size": 6, "offset": 3}
                )
            ],
            justify='center'
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button('Show/Hide Extra Block', id='show_hide_button')
                    ],
                    width={"size": 6, "offset": 3}
                )
            ],
            justify='center'
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            'Extra Block',
                            id='extra_block_div',
                            className='display-2',
                            hidden=True,
                        )
                    ],
                    width={"size": 6, "offset": 3}
                )
            ],
            justify='center'
        )
    ]
)