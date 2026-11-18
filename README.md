# Student Task Manager

## Introduction
Student Task Manager is a simple Python console application that helps students manage their tasks. Users can add, view, complete, and delete tasks.

## Features
- Add tasks with unique IDs.
- Reject empty task titles.
- View all tasks and their status.
- Mark tasks as completed.
- Delete tasks using their IDs.
- Handle invalid task IDs and numeric input.
- Automated unit testing using Python's unittest framework.
- GitHub Actions workflow for automatic testing.

## Requirements
- Python 3.11 or later
- Git (optional, for version control)

## Setup Instructions
1. Clone the repository:

   `git clone https://github.com/YOUR-USERNAME/studenttaskmanager.git`

2. Open the project directory:

   `cd studenttaskmanager`

3. Run the application:

   `python task_manager.py`

## Usage
Select an option from the application menu:

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter the required task title or task ID when prompted.

## Running Tests
Run the following command from the project directory:

`python -m unittest discover -s tests -v`

The tests verify task creation, task completion, and task deletion.

## Continuous Integration
GitHub Actions automatically runs the unit tests when code is pushed to the main branch or when a pull request targets main.

## License
This project is licensed under the MIT License.