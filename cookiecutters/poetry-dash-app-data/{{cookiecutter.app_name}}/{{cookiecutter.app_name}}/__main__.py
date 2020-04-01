"""`Dash` app that demonstrates the data initialization.

Let's assume that we want to initialize some varying div block with data.
`Dash` prevents us from using global variables with data that changes
over time and we need to use `dash_core_components.Store`.
Let `hide_extra_block` be some 'Input data', for example from the
keyboard or as command line argument.
We have `DashApp` class that implements `ininital_data` property
(`dict` or `Box`) which we can assign `hide_extra_block` value. Before
that it is recommended to set some default value to the `DashApp.initial_data`.
When we can make an assignment.
Also it is recommended to follow widgets hierarchy inside the
`DashApp.initial_data` `dict`.
After that we can start the server.
"""

from pydash import py_

from {{cookiecutter.app_name}}.data.initial_data import initial_data

from {{cookiecutter.app_name}}.dash_app.app import app as dash_app

debug = True

# Input data
hide_extra_block = True

# Data bindings
dash_app.initial_data = py_.default_to(None, initial_data)
dash_app.initial_data.extra_block_div.is_hidden = hide_extra_block

# Start server
dash_app.run_server(debug=debug, port=8077, threaded=True)