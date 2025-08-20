# Django HTMX SaaS Template

A modern Django SaaS starter template featuring HTMX, Tailwind CSS (via DaisyUI), and best practices for rapid development and deployment.

## Features

### Current Features
- Django project structure with reusable apps
- HTMX for dynamic, modern frontend interactions
- Tailwind CSS + DaisyUI for styling
- Allauth for authentication (login, signup, social, passkey support)
- Docker support for easy deployment
- Railway deployment configuration
- Custom management command for superuser creation
- Example contact form and basic pages

### Planned Features
- Integrate forms with captcha validation

## Project Structure

```
.
├── .env.example
├── Dockerfile
├── railway.json
├── requirements.txt
├── requirements_railway.txt
├── requirements_codespace.txt
└── src/
    ├── manage.py
    ├── arvmain/           # Main Django project
    ├── commando/          # Example Django app
    ├── helpers/           # Helper modules
    ├── staticfiles/       # Compiled static assets
    ├── templates/         # Django templates
    └── .django_tailwind_cli/
```

## Setup

1. **Clone the repository**

2. **Create virtual env and activate it**

   ```
   py -m venv venv
   venv/Scripts/activate or
   . venv/bin/activate
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in the required values.

5. **Download vendors file**
   
   ```
   python manage.py vendor_pull
   ```

6. **Configure Tailwind CLI**
   
   ```
   python manage.py tailwind setup
   ```

7. **Run migrations and create superuser**

   ```
   python manage.py migrate
   python manage.py createsu
   ```

8. **Run the development server and hot reload**

   ```
   python manage.py tailwind runserver
   ```

## Deployment

- Ready for deployment on [Railway](https://railway.app/) (see [`railway.json`](railway.json))
- Uses Gunicorn for production serving

## Custom Management Commands

- [`python manage.py createsu`](src/commando/management/commands/createsu.py): Creates a Django superuser from environment variables.

## Styling

- Tailwind CSS and DaisyUI are used for styling.
- See [`python manage.py tailwind config`](src/.django_tailwind_cli/source.css) for current configuration.

## Authentication

- Allauth is used for authentication.
- Templates for login, signup, and logout are in [`src/templates/account/`](src/templates/account/).

## Contact

- Example contact form at `/contact` using Django forms and HTMX.

---

**License:** MIT
