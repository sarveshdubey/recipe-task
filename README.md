# Recipe API Backend

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs

## Prerequisites
* Python :- 3.9.6
* postgres :- 16.2 

## Installation 
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/saharsh-solanki/recipe-app-backend
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd recipe-app-backend
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python -m venv venv
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Rename the .env.dist file to .env and update environment variables
    5. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```
    6. Create a supper user.Enter your email and password
        ```bash
        python manage.py createsuperuser
        ```
    7. Run Server 
       ```bash
       python manage.py runserver
       ```
    8. Admin Dashboard can be accessed at this url
       ```bash
        http://127.0.0.1:8000/admin/login/?next=/admin/
        ```
    9. Swagger UI Can be accessed here 
       ```bash
        http://127.0.0.1:8000/docs/
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the swagger api docs here 
    ```
        http://localhost:8000/docs/
    ```