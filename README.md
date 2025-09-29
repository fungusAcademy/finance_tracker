# 💰 Finance Tracker - Personal Finance Management System

A full-featured, production-ready web application for personal finance management built with Django. This project demonstrates modern web development practices with a complete user authentication system, real-time analytics, and responsive design.

![Django](https://img.shields.io/badge/Django-5.2.6-092E20?logo=django)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap)
![Chart.js](https://img.shields.io/badge/Chart.js-4-FF6384?logo=chart.js)
![Render](https://img.shields.io/badge/Deployed-Render-46B3E6)

## Project Overview

Finance Tracker is a comprehensive financial management solution that enables users to track income and expenses, set budgets, and analyze spending patterns through interactive dashboards. Built with scalability and user experience in mind, it showcases full-stack development capabilities with a focus on data integrity and security.

### Live Production Deployment

**Experience the application:** [Finance Tracker Live Demo](https://finance-tracker-uvth.onrender.com/)

## Key Features

### Core Financial Management
- **Transaction Tracking** - Comprehensive CRUD operations for income and expenses
- **Category System** - Hierarchical categorization with custom user-defined categories
- **Budget Management** - Period-based budgeting with real-time spending comparisons
- **Multi-User Support** - Secure data isolation between users

### Advanced Analytics & Reporting
- **Interactive Dashboards** - Real-time financial overview with Chart.js visualizations
- **Spending Analysis** - Category-wise expense tracking with trend identification
- **Budget vs Actual** - Visual comparison of planned vs actual spending
- **Financial Health Metrics** - Balance calculations and financial insights

### Security & User Management
- **Django Authentication** - Secure user registration and login system
- **Data Protection** - User-level data isolation and access controls
- **Session Management** - Secure cookie handling and session protection
- **Production Security** - HTTPS enforcement and security headers

### User Experience
- **Responsive Design** - Mobile-first approach with Bootstrap 5
- **Intuitive Interface** - Clean, modern UI with seamless navigation
- **Form Validation** - Client and server-side validation with user feedback
- **Progressive Enhancement** - Graceful degradation for JavaScript-disabled clients

## Technical Architecture

### Backend Stack
- **Framework**: Django 5.2.6 with Class-Based Views
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Authentication**: Django built-in auth with session management
- **API Design**: RESTful architecture with form-based interactions

### Frontend Stack
- **Templating**: Django Templates with template inheritance
- **Styling**: Custom CSS with Bootstrap 5 components
- **Data Visualization**: Chart.js for interactive financial charts
- **JavaScript**: Vanilla JS for dynamic form interactions

### DevOps & Deployment
- **Platform**: Render.com with automated deployments
- **Static Files**: WhiteNoise for efficient static file serving
- **Database**: Managed PostgreSQL with connection pooling
- **Build Process**: Automated build scripts with dependency management

## Project Structure
```
finance_tracker/
├── config/          # Django project settings
│ ├── settings/      # Environment-specific configurations
│ └── wsgi.py        # Production WSGI configuration
├── transactions/    # Main application
│ ├── models.py      # Database models (Category, Transaction, Budget)
│ ├── views.py       # Class-based and function-based views
│ ├── forms.py       # Django forms with custom validation
│ ├── admin.py       # Django admin customization
│ └── management/    # Custom management commands
├── static/          # CSS, JavaScript, images
│ └── css/
│ └── style.css      # Unified stylesheet
├── templates/       # Django templates
│ ├── base.html      # Base template structure
│ └── transactions/  # App-specific templates
├── requirements.txt # Python dependencies
├── build.sh         # Render.com build script
└── render.yaml      # Infrastructure as Code configuration
```

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL (for production) or SQLite (for development)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/fungusAcademy/finance_tracker.git
   cd finance_tracker
   ```

2. **Set up virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment**
    ```bash
    cp .env.example .env
    # Edit .env with your settings
    ```

5. **Run migrations**
    ```bash
    python manage.py migrate
    ```

6. **Start development server**
    ```bash
    python manage.py runserver
    ```

### Production Deployment

The application is configured for seamless deployment on Render.com:

1. **One-Click Deploy**

https://render.com/images/deploy-to-render-button.svg

2. **Environment Variables**

- **DEBUG**=False

- **SECRET_KEY** (auto-generated)

- **DATABASE_URL** (provided by Render)

- **SUPERUSER_*** credentials (for admin access)

## Technical Highlights

### Database Design

- **Normalized Schema** - Optimized relationships between users, categories, and transactions

- **Data Integrity** - Foreign key constraints and validation rules

- **Performance** - Strategic indexing for common query patterns

### Security Implementation

- **CSRF Protection** - Built-in Django CSRF tokens

- **XSS Prevention** - Template auto-escaping and secure form handling

- **SQL Injection Protection** - Django ORM with parameterized queries

- **Password Hashing** - PBKDF2 with SHA256

### Code Quality

- **DRY Principles** - Template inheritance and reusable components

- **Separation of Concerns** - Clear separation between models, views, and templates

- **Error Handling** - Comprehensive form validation and user feedback

- **Accessibility** - Semantic HTML and keyboard navigation support

## Business Value

This project demonstrates capabilities in building:

- **Scalable Web Applications** with proper architecture patterns

- **Data-Intensive Applications** with complex relationships and calculations

- **User-Centric Design** with focus on usability and experience

- **Production-Ready Systems** with security and deployment considerations

## Contributing

This is a portfolio project demonstrating full-stack development skills. While primarily for demonstration purposes, suggestions and feedback are welcome.

## Licence

This project is licensed under the MIT License