# Building your own CRM with Django

This guide will show you how to set up a Python virtual environment and install Django, a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Requirements

- Python (Preferably 3.7 and above)
- pip (Python Package Installer)

## Steps

1. First, you need to activate your Python virtual environment. If you have not created one, create it using the `python3 -m venv /path/to/new/virtual/environment` command. Here, we already have a virtual environment named `website_venv`. To activate it, navigate to the directory where it is located and run the following command:

    ```bash
    source website_venv/bin/activate
    ```
    Your terminal prompt should now show the name of your virtual environment, like so:
    ```bash
    (website_venv) teboho@tebo:~/bemore$
    ```

2. Check your active Python package installer (`pip`) location to make sure it corresponds to your virtual environment:

    ```bash
    which pip
    ```
    The output should look something like this:
    ```bash
    /home/teboho/bemore/website_venv/bin/pip
    ```

3. Now, let's install Django using pip:

    ```bash
    pip install django
    ```
    After the installation, your terminal should display something like this:
    ```bash
    Collecting django
    Downloading Django-4.2.2-py3-none-any.whl (8.0 MB)
    ...
    Successfully installed asgiref-3.7.2 django-4.2.2 sqlparse-0.4.4 typing-extensions-4.7.0
    ```

4. Once Django is installed, it's a good practice to save all the dependencies of your project in a `requirements.txt` file. This file can be used later to install all the dependencies at once:

    ```bash
    pip freeze > requirements.txt
    ```

With Django installed in your virtual environment, you are now ready to start building your own CRM!

