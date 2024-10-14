# Task Management API

This project is a simple task management server built with Flask and SQLAlchemy. It allows users to create, retrieve, update, and delete tasks. 
The API accepts and returns JSON data, making it easy to integrate with web applications.

## Features
- Create a new task with a title and completion status.
- List all tasks created.
- Get details of a specific task.
- Edit the title or completion status of a specific task.
- Delete a specified task.

### Database Setup

**SQL Option**: This project uses **SQLite** as a lightweight database for development purposes. The SQLAlchemy ORM is utilized for managing database connections and defining models.

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- SQLAlchemy

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, use:
```bash
python app.py
```
The server will start on `http://localhost:5000`.

### Testing the API

You can use tools like Postman or CURL to test the API endpoints.


![image](https://github.com/user-attachments/assets/9f630e07-7988-4fdd-b63d-551190c0ae27)
