"""Dash app initializer."""

# DO NOT CHANGE!

from {{cookiecutter.app_name}}.dash_app.DashApp import DashApp

app = DashApp()
app.set_layout()
app.set_controllers()