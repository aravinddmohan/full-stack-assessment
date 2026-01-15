# Full Stack Assessment – Employee Management System

## Overview
This project is a simple Employee Management System built as part of a full stack assessment.  
It demonstrates core CRUD operations and basic business logic handling using a backend-driven approach.

---

## Features
- Add new employees
- View all active employees
- Fetch employee details by ID
- Update employee information
- Soft delete employees (mark as INACTIVE)
- Unique email validation

---

## Tech Stack
- Backend: Python (Django)
- Database: SQLite (default Django DB)
- Frontend: HTML (Django Templates)
- Version Control: Git & GitHub

---

## Project Structure
- `employees/` – Employee app containing models, views, and templates
- `templates/` – HTML templates for UI rendering
- `models.py` – Employee model with status-based soft delete
- `views.py` – CRUD logic implementation
- Notes

Deleted employees are marked as INACTIVE instead of being removed from the database

Only ACTIVE employees appear in the employee list view

Section B logical problems are included as part of the assessment solutions

---

## How to Run Locally
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies
4. Run migrations
5. Start the development server

```bash
python manage.py migrate
python manage.py runserver
