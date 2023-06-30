## Start a New Django Project

5. To start a new Django project, we'll use the Django administration utility, `django-admin`. Run the following command:

    ```bash
    django-admin startproject bmocrm .
    ```
    This will create a new Django project named 'bmocrm' in your current directory.

## Running the Server

6. Next, we need to start our Django development server. Use the following command to start the server:

    ```bash
    python manage.py runserver
    ```
    Upon running this command, you should see the following output, which means your server is up and running:
    ```bash
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    June 30, 2023 - 03:09:58
    Django version 4.2.2, using settings 'bmocrm.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

7. Access the server at `http://127.0.0.1:8000/` via a web browser. You will see the Django welcome page and some logging information in the terminal:

    ```bash
    [30/Jun/2023 03:10:28] "GET / HTTP/1.1" 200 10664
    Not Found: /favicon.ico
    [30/Jun/2023 03:10:28] "GET /favicon.ico HTTP/1.1" 404 2110
    ```

Note: If you see a message about unapplied migrations, don't worry. Django creates a database and some default tables for you, but we haven't applied those changes yet. This will be done later when we run `python manage.py migrate`.
