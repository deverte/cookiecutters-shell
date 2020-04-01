"""A one line summary of the program.

Overall program description (it can consist of several lines).
"""

from {{cookiecutter.app_name}}.app import app

app.run_server(debug=True, port=8077, threaded=True) # Debug
# app.run_server(debug=False, port=8077, threaded=True) # Release