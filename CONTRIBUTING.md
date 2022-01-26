# Contributing to Pglet for Python

Thank you for your interest in contributing to Pglet!

## Clone repo

TBD

## Install PDM

## Windows

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -
```

Enable PEP 582:

```
pdm --pep582
```

> Run `refreshenv` after installing PDM on Windows or restart terminal.

## macOS

```
brew install pdm
```

Enable PEP 582:

```
pdm --pep582 >> ~/.zprofile
```

Restart the terminal session to take effect.

## Install dependencies

To install all Pglet dependencies and enable the project as editable package run:

```
pdm install
```

## Check the installation

Run "counter" example:

```
python3 examples/counter.py
```

During the first run Pglet Server will be downloaded from GitHub releases to `$HOME/.pglet/bin` directory and started from there. The version of Pglet Server to download is taken from `PGLET_VERSION` variable in `appveyor.yml` in the root of repository.

You should get a new browser window opened with "counter" web app running.