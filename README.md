# cookiecutters-shell


- [About](#about)
- [Cookiecutters](#cookiecutters)
  - [Python](#python)
    - [class-py](#class-pycookiecuttersclass-py)
  - [Dash](#dash)
    - [dash-app](#dash-appcookiecuttersdash-app)
    - [dash-widget](#dash-widgetcookiecuttersdash-widget)
    - [poetry-dash-app-simple](#poetry-dash-app-simplecookiecutterspoetry-dash-app-simple)
    - [poetry-dash-app-data](#poetry-dash-app-datacookiecutterspoetry-dash-app-data)
  - [Click](#click)
    - [poetry-click-app](#poetry-click-appcookiecutterspoetry-click-app)
  - [Orange](#orange)
    - [poetry-orange-widget](#poetry-orange-widgetcookiecutterspoetry-orange-widget)
  - [PyTorch](#pytorch)
    - [pytorch-lstm-time-series](#pytorch-lstm-time-seriescookiecutterspytorch-lstm-time-series)
  - [LaTeX](#latex)
    - [journal-project-tex](#journal-project-texcookiecuttersjournal-project-tex)
- [Documentation](#documentation)
  - [Cookiecutter (optional)](#cookiecutter-optional)
  - [Downloading (optional)](#downloading-optional)
  - [Usage (recommended)](#usage-recommended)
- [Author](#author)
- [License](#license)


---


## About
Some useful [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/) templates.

Before using, please **read** [Documentation](#Documentation) first.


---


## Cookiecutters
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip

### Python
#### [class-py](/cookiecutters/class-py)
Creates `Python` class in the **current** directory.
```sh
cc shell:class-py
```

### Dash
#### [dash-app](/cookiecutters/dash-app)
Creates simple [Dash](https://dash.plotly.com/) app skeleton (without any dependencies) that tries to follow [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)-like design pattern (if we talk about the file structure).
```sh
cc shell:dash-app
```

#### [dash-widget](/cookiecutters/dash-widget)
Creates `Dash` widget for the [Dash](https://dash.plotly.com/) app that follows [dash-app](/cookiecutters/dash-app) `Cookiecutter` structure.
```sh
cc shell:dash-widget
```

#### [poetry-dash-app-simple](/cookiecutters/poetry-dash-app-simple)
Creates [Dash](https://dash.plotly.com/) app skeleton (with dependencies) that tries to follow [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)-like design pattern (if we talk about the file structure).
```sh
cc shell:poetry-dash-app-simple
```

#### [poetry-dash-app-data](/cookiecutters/poetry-dash-app-data)
Creates [Dash](https://dash.plotly.com/) app skeleton (with dependencies) that tries to follow [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)-like design pattern (if we talk about the file structure). Also this template demonstrates initializing the `Dash` app by some initial data.
```sh
cc shell:poetry-dash-app-data
```

### Click
#### [poetry-click-app](/cookiecutters/poetry-click-app)
Creates [Click](https://palletsprojects.com/p/click/) app skeleton with dependencies.
```sh
cc shell:poetry-click-app
```

### Orange
#### [poetry-orange-widget](/cookiecutters/poetry-orange-widget)
[Orange](https://orange.biolab.si/) Widget (Add-on) template.
```sh
cc shell:poetry-orange-widget
```

### PyTorch
#### [pytorch-lstm-time-series](/cookiecutters/pytorch-lstm-time-series)
Creates notebook with LSTM-based neural network for time series prediction with [PyTorch](https://pytorch.org/) machine learning framework.
```sh
cc shell:pytorch-lstm-time-series
```

### LaTeX
#### [journal-project-tex](/cookiecutters/journal-project-tex)
Creates `LaTeX` project with `Journal` style by `deverte`.
```sh
cc shell:journal-project-tex
```


---


## Documentation
For simplifying `cookiecutters-shell` repository management and navigation between cookiecutters, it was decided to use only one repository for all cookiecutters.  
For this reason cookiecutters bundled as **zip** files.  

### Cookiecutter (optional)
As `Cookiecutter` is very useful template generator, some templates you can use very often. For this reason it is good to set short **alias** for the `cookiecutter` program. This repository recommends to use `cc` alias. **Important**: ensure that you already don't have program with name `cc`, or `cc` alias.

There are instructions for some shells:  
**Bash (Unix / GNU/Linux / ...)**  
In `~/.bashrc` file add:
```sh
alias cc = /path/to/cookiectuer/cookiecutter
```

**PowerShell (Windows)**  
In your [profile file](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-7) file add:
```sh
Set-Alias -Name cc -Value /path/to/cookiectuer/cookiecutter.exe
```

**CMD (Windows)**  
First, setup your cmd startup script (see [Command Processor\AutoRun](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779439(v=ws.10)?redirectedfrom=MSDN)).
Then add it to your startup script:
```sh
DOSKEY cc = /path/to/cookiectuer/cookiecutter.exe
```


### Downloading (optional)
For simplifying downloading of cookiecutters from this repository, it is reccomending to add `shell` abbreviation to the `cookiecutter-config.yaml` file (see [Cookiecutter - User Config](https://cookiecutter.readthedocs.io/en/1.7.0/advanced/user_config.html)).  
Just add the next string to the `abbreviations` section of the `cookiecutter-config.yaml` file:
```yaml
shell: https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip
```

Now you can download cookiecutters from this repository with the next command (for example, [class-py](/class-py)):
```sh
cc shell:class-py
```

### Usage (recommended)
The most convinient usage of zip-bundled cookiecutters is to add `z` abbreviation to the `cookiecutter-config.yaml` file.  
Just add the next string to the `abbreviations` section of the `cookiecutter-config.yaml` file (**don't forget** to specify the right `cookiecutters_dir`):
```yaml
z: /path/to/cookiecutters_dir/{0}.zip
```

Now you can run downloaded zip-bundled cookiecutters with the next command (for example, [class-py](/class-py)):
```sh
cc z:class-py
```


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License
[MIT](/LICENSE)