[![Build Status](https://travis-ci.org/kmedian/thermoencoder.svg?branch=master)](https://travis-ci.org/kmedian/thermoencoder)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/thermoencoder/master?urlpath=lab)

# thermoencoder

## DELETE THIS LATER 
Download thermoencoder and rename it

```
git clone git@github.com:kmedian/thermoencoder.git mycoolpkg
cd mycoolpkg
bash rename.sh "kmedian" "mycoolpkg" "Real Name"
```

The git repo is reinitialized without an remote url. 
Therefore

```
git remote add origin git@github.com:kmedian/mycoolpkg.git
```


## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `thermoencoder` [git repo](http://github.com/kmedian/thermoencoder) is available as [PyPi package](https://pypi.org/project/thermoencoder)

```
pip install thermoencoder
```


## Usage
Check the [examples](http://github.com/kmedian/thermoencoder/examples) folder for notebooks.



## Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi: `python setup.py sdist upload -r pypi`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Debugging
* Notebooks to profile python code are in the [profile](profile) folder


## Support
Please [open an issue](https://github.com/kmedian/thermoencoder/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/thermoencoder/compare/).
