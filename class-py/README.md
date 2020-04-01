# class-py

1. [About](#About)
2. [Template variables](#Template-variables)
3. [Hooks](#Hooks)
4. [Documentation](#Documentation)
5. [Author](#Author)
6. [License](#License)

---


## About
Creates `Python` class in the **current** directory.  
Default class docstrings corresponds to a [Google Style](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) styleguide (because this style is well suited to modular programs).

**Installation**  
```sh
cookiecutter https://github.com/deverte/cookiecutters-shell/blob/master/zip/class-py.zip
```

**Usage**  
```sh
cookiecutter class-py
```

**Important**  
Now this `Cookiecutter` raises *OSException* because post install hook deletes temporary folder in which `Cookiecutter` works. But it still works correctly.


---


## Template variables
Format:
> **variable**: *default value* - Description.

**class_name**: *PythonClass* - Name of the class (and file) to be created.


---


## Hooks
1. Creates temporary directory for the class file.
2. Moves class file to the current directory.
3. Removes temporary directory (this step raises *OSException*).


---


## Documentation
Just add your methods or properties to the created class and import it to your module.


---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License
MIT