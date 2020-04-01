# cookiecutters-shell

1. [About](#About)
2. [Cookiecutters](#Cookiecutters)
    1. [class-py](#class-py)
3. [Documentation](#Documentation)
    1. [Cookiecutter](#Cookiecutter-optional)
    2. [Downloading](#Downloading-optional)
    3. [Usage](#Usage-recommended)
3. [Author](#Author)
4. [License](#License)

---


## About
Some useful [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/) templates.

Before using, please **read** [Documentation](#Documentation) first.


---


## Cookiecutters
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip

### [class-py](/class-py)
Creates `Python` class in the **current** directory.
```sh
cc shell:class-py
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