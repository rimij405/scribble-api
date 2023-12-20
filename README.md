# Scribble API

Repository containing the API for the Scribble note-taking application example.

## Overview

This is a FastAPI backend server written to serve a REST API for a note-taking application.

## Getting Started

Follow this walkthrough to get started with local development.

1. Activate your virtual environment.

    ```sh
    $ source ./venv/bin/activate
    # No output but your shell should show the activated environment.
    ```

2. Ensure the `pip-tools` development dependency is installed.

    > :memo: This assumes you have installed `pip` in your virtual environment.

    ```sh
    $ pip install pip-tools
    # This will install the pip-compile and pip-sync commands.
    ```

3. Use the helper scripts to install the pinned dependencies.

    > :memo: This uses `pip-sync` under the hood.

    ```sh
    $ bin/install
    # This uses `pip-sync` to install the package dependencies inside of `requirements.txt`.
    ```
