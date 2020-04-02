# poetry-dash-app-simple

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Hooks](#Hooks)
4. [Documentation](#Documentation)
    1. [Requirements](#Requirements)
    2. [Dash App Structure](#Dash-app-structure)
    3. [Scripts](#Scripts)
    4. [Coconut](#Coconut)
5. [Author](#Author)
6. [License](#License)

---


## About
Creates [Dash](https://dash.plotly.com/) app skeleton (with dependencies) that tries to follow [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)-like design pattern (if we talk about the file structure).

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:poetry-dash-app-simple
```

**Usage**  
```sh
cc z:poetry-dash-app-simple
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
- [Poetry - Local configuration](https://python-poetry.org/docs/configuration/#local-configuration)

### Dash app structure
This `Cookiecutter` template provides the following `Dash` app structure.

**.gitignore**  
Pre-defined files that will be ignored by git.

**pyproject.toml**  
The main file with project's description (dependencies, commands, build instructions, etc.). See [Poetry - pyproject.toml](https://python-poetry.org/docs/pyproject/).

**README.md**  
File with app's description / short documentation.

**{app_name}**  
Directory with your `Dash` app.

**{app_name}/\_\_main__.py**  
App entry point that starts `Dash` server.

**{app_name}/app.py**  
`Dash` server initialization (grabs all views and controllers).

**{app_name}/widgets**  
Folder with `Dash` widgets. Here you can add the new widgets with [dash-widget](../dash-widget) `Cookiecutter`.

**{app_name}/widgets/controller.py**  
`Dash` app controller.

**{app_name}/widgets/layout.py**  
`Dash` app layout (view).

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