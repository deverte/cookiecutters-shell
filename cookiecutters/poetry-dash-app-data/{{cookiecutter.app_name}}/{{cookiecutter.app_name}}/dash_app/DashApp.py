from box import Box
import dash

class DashApp:
    """`Dash` app wrapper.

    Presents `Dash` app wrapper that grabs all layouts and controllers.
    Also it implements work with an initial data.

    Attributes:
        app: `Dash` app.
        initial_data: Data that affects on initial state of the program.
    """
    
    __app: dash.Dash = None
    __initial_data: Box = Box({})

    def set_layout(self):
        """Sets style, index and layout elements of the app.

        Sets external styles from `{app_name}/dash_app/widgets/view.py` file.
        Reads `index.html` file from the `{app_name}/dash_app/assets/markup/html`
        folder and applies it to the `app` property.
        Sets layout of the app from `{app_name}/dash_app/widgets/view.py` file.

        Raises:
            OSError: Raises when index file can not be read.
        """
        from {{cookiecutter.app_name}}.dash_app.widgets.view import external_stylesheets
        from {{cookiecutter.app_name}}.dash_app.widgets.view import view
        import os

        index_string = None

        try:
            index = open('{{cookiecutter.app_name}}/dash_app/assets/markup/html/index.html')
            index_string = index.read()
        except OSError:
            index_string = None

        self.__app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        self.__app.index_string = index_string or self.__app.index_string
        self.__app.layout = view

    def set_controllers(self):
        """Sets controllers.

        Sets controllers that imported into the `{app_name}/dash_app/сontrollers.py`
        file.
        """
        import {{cookiecutter.app_name}}.dash_app.controllers

    def run_server(self, *args, **kwargs):
        """Starts `Dash` server.

        Args:
            *args: positional arguments for the `dash.Dash.run_server` method.
            *kwargs: keyword arguments for the `dash.Dash.run_server` method.
        """
        self.app.run_server(*args, **kwargs)

    @property
    def app(self):
        return self.__app

    @property
    def initial_data(self):
        return self.__initial_data

    @initial_data.setter
    def initial_data(self, value):
        self.__initial_data = value