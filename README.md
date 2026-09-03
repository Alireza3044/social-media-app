# Social Media App

A simple text-based social media app with a complete authentication system.

This app is powered by Django as it's main framework in addition to TailwindCSS, HTMX, and Alpine.js.

# Getting Started

1. Clone the repository into your machine by:

   `git clone https://github.com/Alireza3044/social-media-app.git`

2. Install the required packages from requirements.py by running the following command:

   `pip install -r requirements.txt`

3. Create a .env file with variables DJANGO_DEBUG and DJANGO_SECRET_KEY. If you want to deploy the project, set the DJANGO_DEBUG to False, otherwise to True. For DJANGO_SECRET_KEY you can generate one by first entering to the Django shell via `python manage.py shell` and then importing and running the function `get_random_secret_key` from `django.core.management.utils`.

4. Migrate the models by:

   `python manage.py migrate`

5. Now you can run the Django dev server alongside TailwindCSS by following command:

   `python manage.py tailwind runserver`

6. After first run it would try to download the TailwindCSS's binary file. After installation, you can explore the project!
