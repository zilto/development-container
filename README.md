# Development container

## Dependencies
- Docker Desktop
- hydra Python package `pip install hydra-core` to handle config files (TODO remove dependency)

## How to use:
1. Setup `environment.yml` to create the virtual environment within the container
2. Setup `scripts/config/docker.yaml` to define your docker environment
3. Add your secrets to the `/.devcontainer` directory (then add to `.gitignore`); they won't be accessed by Docker build
4. Start Docker Desktop
5. Run `python scripts/create_container.py` to create your dev-container
6. Run `python scripts/launch_script.py` or `python scripts/launch_jupyter.py`

## Features
The development container allows to run script and run Jupyter notebooks from a Linux environment on a Windows machine. The container will be in sync with your code found in `/src` which allows for quick testing iterations. With a few tweaks, the current approach could enable code to be executed on remote containers. 

## Motivation
Being primarily a Windows user, I wanted to be able to fully use Python projects with Linux dependencies (Metaflow, research repos, etc). I considered Windows Subsystem for Linux (WSL), but I wanted access to my usual IDE (Dataspell by Jetbrains) and data located on the Windows system. 

PyCharm has a feature to run/debug code within a container, but Dataspell doesn't. However, I can setup the IDE `Run` command to launch a script in the container. VSCode has devcontainer extensions, but it relies on a domain specific config and the images created a quite heavy (~5 Gb) 
