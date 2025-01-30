# Shuttle System Project Management

A Django-based project management system for managing shuttle and parking lot operations. This system helps track project initiation, stakeholder management, requirements collection, and risk assessment.

## Features

- Stakeholder Management
- Project Charter Documentation
- Requirements Tracking (MoSCoW Method)
- Risk Assessment and Management
- Full Admin Interface

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the admin interface at `http://localhost:8000/admin`
2. Log in with your superuser credentials
3. Start managing your project by:
   - Adding stakeholders
   - Creating project charter
   - Documenting requirements
   - Tracking risks

## Project Structure

- `project_management/`: Main app containing project management functionality
  - `models.py`: Database models for project entities
  - `admin.py`: Admin interface configurations

## License

MIT License