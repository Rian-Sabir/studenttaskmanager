# Student Task Manager – User Guide

## 1. Introduction
Student Task Manager is a Python console application designed to help students organize their tasks.

## 2. Starting the Application
Open a terminal in the project directory and execute:

`python task_manager.py`

The main menu will appear.

## 3. Adding a Task
1. Select option 1.
2. Enter a task title.
3. The application assigns the task a unique ID.
4. Empty task titles are rejected.

## 4. Viewing Tasks
Select option 2 to display all tasks, including their IDs, titles, and completion statuses.

Tasks can have two statuses:
- Pending
- Completed

## 5. Completing a Task
1. Select option 3.
2. Enter the ID of the task.
3. The selected task is marked as Completed.

If the ID does not exist, the application displays an error message.

## 6. Deleting a Task
1. Select option 4.
2. Enter the ID of the task.
3. The selected task is removed from the task list.

If the ID does not exist, the application displays an error message.

## 7. Exiting the Application
Select option 5 to close the application.

## 8. Running Unit Tests
To test the application's main functions, execute:

`python -m unittest discover -s tests -v`

The test suite checks adding, completing, and deleting tasks.