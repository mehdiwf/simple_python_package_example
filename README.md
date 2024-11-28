# example package

my example (mehdi fawaz)

# what to modify
If you want to make your own package, you have to:

in `pyproject.toml`: modify the variables `name`, `version`,
`authors`, `description` in the table `[project]`. Make sure that your
python requirement is indeed version > 3.7 (for instance, if you use
`match`, you need at least python 3.10)

in the folder `src`, modify the name of the folder and replace it with
the name you put in `pyproject.toml`.

# installation
## to install globally

## to install with pyenv:
make sure to use the right python version to install your stuff:
for me, `pyenv` puts the python version designed as global in the executable `python`.

then, install the package with (in your shell, in the same directory
as the "pyproject.toml" file):

```
YOUR_PYTHON_EXEC -m pip install -e .
```
make sure to replace `YOUR_PYTHON_EXEC` by the right thing, which is usually something like `python3`

-e is to make sure that it is in dev mode

## to uninstall:

type (in your shell):
```
YOUR_PYTHON_EXEC -m pip uninstall YOUR_PACKAGE_NAME
```

make sure to replace `YOUR_PYTHON_EXEC` and `YOUR_PACKAGE_NAME` by the right thing

# notes

When you modify a source file in the directory where you installed
your package, then you don't need to re-install it for python to
consider the change. But this doesn't work for version: if you change
the version, re-install your package.

You don't need to uninstall and then reinstall your package for it to
be updated, just do as the installation says
