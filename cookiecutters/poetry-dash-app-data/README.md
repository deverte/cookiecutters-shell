# poetry-dash-app-simple

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Hooks](#Hooks)
4. [Documentation](#Documentation)
    1. [Requirements](#Requirements)
    2. [Dash app structure](#Dash-app-structure)
    3. [Scripts](#Scripts)
    4. [Coconut](#Coconut)
5. [Author](#Author)
6. [License](#License)

---


## About
Creates [Dash](https://dash.plotly.com/) app skeleton (with dependencies) that tries to follow [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)-like design pattern (if we talk about the file structure). Also this template demonstrates initializing the `Dash` app by some initial data.

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:poetry-dash-app-data
```

**Usage**  
```sh
cookiecutter poetry-dash-app-data
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**app_name**: dash_app - Name of the `Dash` app.  
**version**: 0.1.0 - App version.  
**description** - App description.  
**authors** - Authors of the App.


---


## Hooks
1. Deactivates `Cookiecutter`'s environment (for running [Rhyme](https://github.com/deverte/rhyme) in the project's [Poetry](https://python-poetry.org/) environment).
2. Installs all dependencies (**only packages**) for a project.


---


## Documentation
### Requirements
- [Python](https://www.python.org/)
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [Poetry](https://python-poetry.org/)
- [Rhyme](https://github.com/deverte/rhyme)
- [Coconut](http://coconut-lang.org/) (*optional*)

Some useful links:  
- [Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Github - Awesome Dash](https://github.com/ucg8j/awesome-dash)
- [PyInstaller](https://www.pyinstaller.org/)  
- [hamplify](https://github.com/Kangaroux/hamplify)
- [lesscpy](https://github.com/lesscpy/lesscpy)
- [Box](https://github.com/cdgriffith/Box)
- [pydash](https://pydash.readthedocs.io/en/latest/)

### Dash app structure
This `Cookiecutter` template provides the following `Dash` app structure.

**.gitignore**  
Pre-defined files that will be ignored by git.

**poetry.toml**  
File with `Poetry` settings. Contains the setting that makes virtual environment inside project directory. See [Poetry - Local configuration](https://python-poetry.org/docs/configuration/#local-configuration).

**pyproject.toml**  
The main file with project's description (dependencies, commands, build instructions, etc.). See [Poetry - pyproject.toml](https://python-poetry.org/docs/pyproject/).

**README.md**  
File with app's description / short documentation.

**{app_name}**  
Directory with your app.

**{app_name}/\_\_main__.py**  
App entry point that grabs initial data and starts `Dash` server.

**{app_name}/dash_app**  
Directory containing all files directly connected with `Dash` app.

**{app_name}/dash_app/app.py**  
`Dash` server initialization (grabs all views and controllers).

**{app_name}/dash_app/controllers.py**  
Controllers storage.

**{app_name}/dash_app/DashApp.py**  
Presents `Dash` app wrapper that grabs all layouts and controllers. Also it implements work with an initial data.

**{app_name}/dash_app/assets**  
Folder with `Dash` assets. Here you can add styles, scripts, favicon or change index layout. See [Dash - External resources](https://dash.plotly.com/external-resources).

**{app_name}/dash_app/assets/libs**  
Folder with external libraries such as `jQuery` or `Bootstrap`.

**{app_name}/dash_app/assets/markup**  
Folder with index layout.

**{app_name}/dash_app/assets/scripts**  
Folder with JavaScript scripts.

**{app_name}/dash_app/assets/styles**  
Folder with CSS styles.

**{app_name}/dash_app/widgets**  
Folder with `Dash` widgets. Here you can add the new widgets with [dash-widget](../dash-widget) `Cookiecutter`.

**{app_name}/dash_app/widgets/controller.py**  
`Dash` app controller.

**{app_name}/dash_app/widgets/layout.py**  
`Dash` app layout (view).

**{app_name}/data**  
Folder with app data (initial data, configurations, databases, serialization).

**{app_name}/data/initial_data.py**  
App initial data. See [Dash - Store](https://dash.plotly.com/dash-core-components/store).

**{app_name}/model**  
Folder with data model classes.

**{app_name}/model**  
Folder with utils.

**tests/***  
Folder with tests. See [pytest](https://docs.pytest.org/en/latest/).

### Scripts
Run scripts via [Rhyme](https://github.com/deverte/rhyme).

```sh
rhyme <script_name>
```

Format:
> **script name** - Description.

**run** - Start program.  
**haml** - HAML -> HTML compilation inside `{app_name}/dash_app/assets/markup/haml` folder.  
**less** - LESS -> CSS compilation inside `{app_name}/dash_app/assets/styles/less` folder.  
**build** - Build single executable program via [PyInstaller](https://www.pyinstaller.org/).  
**exec** - Execute the built program single executable (which was built via **build** script).  
**build_dir** - Build program as folder with dependencies via [PyInstaller](https://www.pyinstaller.org/). Program that was build with this method works *faster*. Also this method useful for *testing*.  
**exec_dir** - Execute the built program from the folder (which was built via **build_dir** script).  
**clear** - Removes all traces by [PyInstaller](https://www.pyinstaller.org/) (*build**, *dist* folders and **.spec* files). ***Caution***: it also removes built executable files.

Also you can add additional scripts (or change defined scripts) in the `pyproject.toml` file.  

### Coconut
If you like functional programming, you can use [Coconut](http://coconut-lang.org/) language and it's transpiler.

To add `Coconut`, just run:
```sh
poetry add coconut coconut[watch] --dev
```

For comfortable usage, you can add `src` folder and write some scripts into the `pyproject.toml` file.
```toml
compile = "coconut src {app_name} -a"
watch = "coconut src {app_name} -a -w"
```

For automatic retranspiling, you can just run the following command:
```sh
rhyme watch
```


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License
[MIT](/License)