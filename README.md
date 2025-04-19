# Employee_Training_Tracker-Rolling_arrays

**Overview**
The Employee Training Tracker is a web application built using Django to manage employee training programs, track enrollment status, and visualize key metrics. It helps HR managers and organizations keep track of their employee training efforts, monitor their progress, and improve their training operations.

**Features**
Employee Management: Add and manage employee data.

Training Management: Add and track training programs.

Enrollment Tracking: Track the enrollment status of employees in training programs.

Data Visualization: Use Chart.js to generate graphical representations of training data (pie charts showing overall statistics and enrollment status).

Responsive Design: The UI is built using Tailwind CSS, making the app mobile-friendly and modern.

**Technologies**
Backend: Django

Frontend: HTML, Tailwind CSS, JavaScript

Database: SQLite (default; can be configured for others like PostgreSQL)

Charting: Chart.js for visualizing data

Deployment: Render for hosting

**Installation**
Prerequisites
Python 3.6+

pip (for managing dependencies)

Steps to Run Locally
-> Clone the repository:
git clone https://github.com/yourusername/employee-training-tracker.git

->Navigate into the project directory:
cd employee-training-tracker

->Create a virtual environment:
python -m venv venv

->Activate the virtual environment:
On Windows:
venv\Scripts\activate
On Mac/Linux:
source venv/bin/activate

->Install the required dependencies:
pip install -r requirements.txt

->Apply the migrations to set up the database:
python manage.py migrate

->Create a superuser to access the admin panel:
python manage.py createsuperuser

->Run the development server:
python manage.py runserver
Access the app: Open your browser and go to http://127.0.0.1:8000/.

Deployment
Employee Training Tracker - https://employee-training-tracker-rollingarrays.onrender.com/
