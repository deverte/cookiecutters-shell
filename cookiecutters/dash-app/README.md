# dash-app

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Documentation](#Documentation)
    1. [Requirements](#Requirements)
    2. [Dash app structure](#Dash-app-structure)
4. [Author](#Author)
5. [License](#License)

---


## About
Creates simple [Dash](https://dash.plotly.com/) app skeleton (without any dependencies) that tries to follow [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)-like design pattern (if we talk about the file structure).

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:dash-app
```

**Usage**  
```sh
cc z:dash-app
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**app_name**: dash_app - Name of the `Dash` app.


---


## Documentation
### Requirements
#### Apps
- [Python](https://www.python.org/)
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [Poetry](https://python-poetry.org/) (optional)
- [Conda](https://www.anaconda.com/distribution/) (optional)

#### Python packages
- [Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)

If these packages aren't installed in your environment, please install via [poetry](https://python-poetry.org/) (**recommended**), pip, or [conda](https://www.anaconda.com/distribution/).  
**pip example**:
```sh
pip install dash dash-bootstrap-components
```

Now you can create your own `Dash` app.  
Some useful links:  
- [Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Github - Awesome Dash](https://github.com/ucg8j/awesome-dash)

### Dash app structure
This `Cookiecutter` template provides the following `Dash` app structure.

**\_\_main__.py**  
App entry point that starts `Dash` server.

**app.py**  
`Dash` server initialization (grabs all views and controllers).

**widgets**  
Folder with `Dash` widgets. Here you can add the new widgets with [dash-widget](../dash-widget) `Cookiecutter`.

**widgets/controller.py**  
`Dash` app controller.

**widgets/layout.py**  
`Dash` app layout (view).


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License
[MIT](/LICENSE)