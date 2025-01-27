# Pill Tracker Application

A Flask-based web application for tracking medications and pill schedules.

## Features

- User authentication system
- Add and manage medications
- Track dosage and timing
- Responsive dashboard interface
- Secure data storage

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
pill_tracker/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
└── templates/         # HTML templates
    ├── base.html      # Base template
    ├── index.html     # Home page
    ├── dashboard.html # User dashboard
    └── add_pill.html  # Add medication form
```

## Technologies Used

- Flask
- SQLAlchemy
- Flask-Login
- Bootstrap 5
- SQLite
