# TaskKing - Task Management Application

A Django-based task management application designed to help users organize and track their daily tasks efficiently.

## Features
- User Authentication (Login/Register)
- Task Creation and Management
- Responsive Design
- Secure Data Handling
- Mobile-Friendly Interface

## Tech Stack
- Python 3.12.6
- Django 5.1.3
- SQLite3 Database
- WhiteNoise for Static Files
- Gunicorn Server

## Project Structure
TaskKing/ ├── TaskKing/ │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── todolist/ │ ├── templates/ │ │ └── todolist/ │ │ ├── login.html │ │ ├── register.html │ │ └── task_list.html │ ├── static/ │ │ ├── css/ │ │ └── js/ │ ├── models.py │ └── views.py ├── staticfiles/ ├── manage.py ├── Procfile └── requirements.txt

## Local Development Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/TooTechnical/TaskKing.git
    cd TaskKing
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Deployment
The application is configured for deployment on Heroku:
1. Set up environment variables:
    - SECRET_KEY
    - DEBUG
    - ALLOWED_HOSTS
    - DATABASE_URL

2. Deploy using Heroku CLI:
    ```bash
    git push heroku main
    ```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Dillon Malone - dillonsmalone.94@gmail.com  
[Project Link](https://github.com/TooTechnical/TaskKing)

## Acknowledgments
- Django Documentation
- Heroku Platform
- Code Institute

