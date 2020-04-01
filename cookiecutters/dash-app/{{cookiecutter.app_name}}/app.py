"""Creates and initializes {{cookiecutter.app_name}} dash app."""

import dash

from {{cookiecutter.app_name}}.widgets.layout import layout
from {{cookiecutter.app_name}}.widgets.layout import external_stylesheets

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = layout

# import {controllers}
import {{cookiecutter.app_name}}.widgets.controller