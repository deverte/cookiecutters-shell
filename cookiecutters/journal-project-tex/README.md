# journal-project-tex

**version: 0.1**

---


- [About](#about)
- [Template variables](#template-variables)
- [Documentation](#documentation)
  - [Requirements](#requirements)
    - [TeX packages](#tex-packages)
  - [Project structure](#project-structure)
  - [Compilation instructions](#compilation-instructions)
- [Author](#author)
- [License](#license)


---


## About
[Cookiecutter](https://cookiecutter.readthedocs.io/) template for LaTeX project with `Journal` style by `deverte`.

**Installation**  
See [Documentation](../../../../#Documentation).
> cc = cookiecutter  
> shell = https://github.com/deverte/cookiecutters-shell/raw/master/zip/{0}.zip  
> z = /path/to/cookiecutters_dir/{0}.zip
```sh
cc shell:journal-project-tex
```

**Usage**  
```sh
cc z:journal-project-tex
```


---


## Template variables
Format:
> **variable**: *default value* - Description.

**project_name**: journal - Name of the LaTeX project.  


---


## Documentation
### Requirements
- [Python](https://www.python.org/) (***necessary***)
- [Pygments](https://pygments.org/) (*optional*)
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) (***necessary***)
- [MiKTeX](https://miktex.org/) or [TeX Live - TeX Users Group](http://www.tug.org/texlive/) (***necessary***)

#### TeX packages
- [babel](https://www.ctan.org/pkg/babel) (Multilingual support)
- [inputenc](https://www.ctan.org/pkg/inputenc) (Accept different input encodings)
- [fontspec](https://www.ctan.org/pkg/fontspec) (Advanced font selection)
- [sectsty](https://www.ctan.org/pkg/sectsty) (Control sectional headers)
- [xcolor](https://www.ctan.org/pkg/xcolor) (Driver-independent color extensions)
- [indentfirst](https://www.ctan.org/pkg/indentfirst) (Indent first paragraph after section header)
- [physics](https://www.ctan.org/pkg/physics) (Macros supporting the Mathematics of Physics)
- [amsmath](https://www.ctan.org/pkg/amsmath) (AMS mathematical facilities)
- [subfiles](https://www.ctan.org/pkg/subfiles) (Individual typesetting of subfiles of a “main” document)
- [hyperref](https://www.ctan.org/pkg/hyperref) (Extensive support for hypertext)
- [graphicx](https://www.ctan.org/pkg/graphicx) (Enhanced support for graphics)
- [fancypar](https://www.ctan.org/pkg/fancypar) (Decoration of individual paragraphs)
- [minted](https://www.ctan.org/pkg/minted) (Highlighted source code)
- [tcolorbox](https://www.ctan.org/pkg/tcolorbox) (Coloured boxes, for LATEX examples and theorems)


### Project structure
This `Cookiecutter` template provides the following project structure.

**main.tex**  
Main project file that contains settings and project structure.

**sections**  
Folder with project sections or subsections (see [subfiles](https://www.ctan.org/pkg/subfiles)).

**sections/*.tex**  
Sections or subsections of the project.

**sections/title.tex**  
Title page of the project.

**sections/annotation.tex**  
Annotation of the project with an important data such as author, document name, date, publisher and etc.

**images**  
Folder with project images.


### Compilation instructions
You can compile project with the following command:  
```sh
lualatex main.tex
```

**NOTE:**  
If you are using LaTeX [minted](https://www.ctan.org/pkg/minted) package, you must compile project inside the [Python](https://www.python.org/) environment with installed [Pygments](https://pygments.org/) and with `-shell-escape` flag:  

```sh
lualatex -shell-escape main.tex
```

---


## Author
GitHub: [deverte](https://github.com/deverte)  
e-mail: [deverte@ya.ru](mailto:deverte@ya.ru)


---


## License

[MIT](/LICENSE)