# poetry-orange-widget

**version: 0.1**

---


- [About](#about)
- [Template variables](#template-variables)
- [Documentation](#documentation)
  - [Requirements](#requirements)
  - [Project structure](#project-structure)
  - [Widget development](#widget-development)
    - [Recommendations](#recommendations)
    - [Build instructions](#build-instructions)
  - [Widget installation](#widget-installation)
- [Author](#author)
- [License](#license)


---


## About
[Cookiecutter](https://cookiecutter.readthedocs.io/) template for [Orange](https://orange.biolab.si/) Widgets (Add-ons).

[Orange](https://orange.biolab.si/) is an awesome Data Science software with a convenient GUI for the fast algorythms prototyping and reproducible research by [University of Ljubljana's Bioinformatics Laboratory](https://fri.uni-lj.si/en/laboratory/biolab).

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:poetry-orange-widget
```

**Usage**  
```sh
cc z:poetry-orange-widget
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**widget_name**: *OWWidget* - Name of the Orange Widget.  
**category**: *Category* - Widget category (shown in the left menu).  


---


## Documentation
### Requirements
- [Poetry](https://python-poetry.org/)
- [Python](https://www.python.org/)
- [Orange](https://orange.biolab.si/)
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)


### Project structure
This `Cookiecutter` template provides the following project structure.

**pyproject.toml**  
Poetry project file that contains project settings and build instructions.

**README.md**  
File with the Widget description.

**{{cookiecutter.widget_name}}**  
Folder with the Widget source code.

**{{cookiecutter.widget_name}}/{{cookiecutter.widget_name}}.py**  
Widget source code.


### Widget development
#### Recommendations
For the Widget development, it is highly recommended to use these docs:

- [Orange Data Mining Library 3 documentation](https://orange-data-mining-library.readthedocs.io/en/latest/) (Orange data structures and algorythms)
- [Orange Development 3 documentation](https://orange-development.readthedocs.io/) (Orange Widgets)
- [AnyQt 0.0.2 documentation](https://anyqt.readthedocs.io/en/stable/index.html) (GUI)

These data processing libraries can also be useful:

- [NumPy](https://numpy.org/)
- [SciPy](https://www.scipy.org/)
- [pandas](https://pandas.pydata.org/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [scikit-learn](https://scikit-learn.org/stable/index.html)

#### Build instructions
For building the Widget, just run:

```sh
poetry build
```

By default, it will produce `.tar.gz` and `.whl` python packages inside the `./dist` directory.

### Widget installation
Widget can be installed as an ordinary python package (but it should be in the same environment as Orange).

With Poetry, you can install Widget as `.tar.gz`/`.whl` Python package, or by specifying a directory (editable mode by default [“Editable” Installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)).

```sh
poetry add ../path/to/widget/dist/OWYourWidget.tar.gz
poetry add ../path/to/widget/dist/OWYourWidget.whl
poetry add ../path/to/widget/OWYourWidget
```

Also, you can install it with `pip`:

```sh
pip install ../path/to/widget/dist/OWYourWidget.tar.gz
pip install ../path/to/widget/dist/OWYourWidget.whl
```

Or with `-e` flag for editable mode:

```sh
pip install -e ../path/to/widget/dist/OWYourWidget.tar.gz
pip install -e ../path/to/widget/dist/OWYourWidget.whl
```


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License

[MIT](/LICENSE)