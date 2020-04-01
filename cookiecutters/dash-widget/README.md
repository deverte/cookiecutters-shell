# dash-widget

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Documentation](#Documentation)
4. [Author](#Author)
5. [License](#License)

---


## About
Creates `Dash` widget for the [Dash](https://dash.plotly.com/) app that follows [dash-app](../dash-app) `Cookiecutter` structure.

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:dash-widget
```

**Usage**  
```sh
cc z:dash-widget
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**widget_name**: dash_widget - Name of the `Dash` widget.


---


## Documentation
### Requirements
See [dash-app Requirements](../dash-app#Requirements).

### Widget structure
**{widget_name}/controller.py**  
Widget controller.

**{widget_name}/view**  
Widget view.


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License
[MIT](/LICENSE)