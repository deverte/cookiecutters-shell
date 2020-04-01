# poetry-click-app

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Hooks](#Hooks)
4. [Documentation](#Documentation)
    1. [Requirements](#Requirements)
    2. [Click app structure](#Click-app-structure)
    3. [Scripts](#Scripts)
    4. [Coconut](#Coconut)
5. [Author](#Author)
6. [License](#License)

---


## About
Creates [Click](https://palletsprojects.com/p/click/) app skeleton with dependencies.

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:poetry-click-app
```

**Usage**  
```sh
cc z:poetry-click-app
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**app_name**: click_app - Name of the `Click` app.  
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
- [Click](https://palletsprojects.com/p/click/)  
- [argparse](https://docs.python.org/3/library/argparse.html)
- [PyInstaller](https://www.pyinstaller.org/)

### Click app structure
This `Cookiecutter` template provides the following `Click` app structure.

**.gitignore**  
Pre-defined files that will be ignored by git.

**poetry.toml**  
File with `Poetry` settings. Contains the setting that makes virtual environment inside project directory. See [Poetry - Local configuration](https://python-poetry.org/docs/configuration/#local-configuration).

**pyproject.toml**  
The main file with project's description (dependencies, commands, build instructions, etc.). See [Poetry - pyproject.toml](https://python-poetry.org/docs/pyproject/).

**README.md**  
File with app's description / short documentation.

**{app_name}**  
Directory with your `Click` app.

**{app_name}/\_\_main__.py**  
App entry point.

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
[MIT](/LICENSE)