# CookPal - Recipe Application

A Django-based web application for managing and sharing culinary recipes. Users can create, view, edit, and delete recipes, along with an interactive and responsive interface. The app supports image uploads for each recipe and includes a searchable, filterable recipe gallery.

## Features

- **User Authentication:** Secure login and logout system.
- **Recipe Management:** Add, edit, and delete recipes with details like ingredients, directions, and difficulty.
- **AJAX Support:** Interactive and smooth UI interactions without page reloads.
- **Responsive Design:** Optimized for desktop and mobile devices.
- **Dynamic Difficulty Calculation:** Calculates recipe difficulty based on cooking time and number of ingredients.
- **Customizable Recipe Instructions:** Supports basic text formatting for clear recipe steps.

## Technologies Used

- **Django** - Backend framework
- **JavaScript (AJAX)** - For smooth user interactions
- **Bootstrap** - For styling and responsive design
- **SQLite** - Default database for development
- **HTML/CSS** - For user interface

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Django 3.2+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/vdevhub/recipe-app.git
   cd recipe-app
   ```
2. **Create a virtual environment:**
```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**
```
pip install -r requirements.txt
```

4. **Run migrations:**
```
python manage.py migrate
```

5. **Create a superuser (admin user):**
```
python manage.py createsuperuser
```
6. **Start the development server:**
```
python manage.py runserver
```
7. **Open app:**
Open http://127.0.0.1:8000 in your browser to access the app.

## Usage

- **Add Recipe:** Fill out the recipe form with name, ingredients, directions, and upload an image.
- **Edit Recipe:** Modify recipe details, adjust cooking time, and update instructions.
- **Delete Recipe:** Remove a recipe entirely from your account.
- **AJAX Operations:** Supports real-time updates in the recipe list for an enhanced user experience.

## Running Tests

To run tests, use the following command:

```
python manage.py test
```

## Deployment
To deploy this project in a production environment, consider using a WSGI server like Gunicorn and a cloud provider or hosting platform like Heroku or DigitalOcean. Remember to configure static files and set up a production database (e.g., PostgreSQL).
1. **Install gunicorn**
```
pip install gunicorn
```
2. **RUn Gunicorn**
```
gunicorn recipe_app.wsgi:application
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push the changes: `git push origin feature/your-feature-name`
5. Submit a pull request.

## License
This project is licensed under the MIT License