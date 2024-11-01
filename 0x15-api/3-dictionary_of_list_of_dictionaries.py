#!/usr/bin/python3
"""
Use the requests module to make a request to an employee REST API
    The request takes in an integer that serves as the employee ID
    Exports data as a JSON file
"""
import json
import requests
import sys


def main():
    """
    This is the main function for the program
    """
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url)
    all_employees = response.json()

    # Get all employee IDs
    employee_ids = [employee["id"] for employee in all_employees]

    def individual_employee(employee_id):
        """
        This works on getting the object for each employee
        """
        # Make the GET request
        url = "https://jsonplaceholder.typicode.com/users/" + str(employee_id)
        response = requests.get(url)
        employee_details = response.json()

        url = url + "/todos"
        response = requests.get(url)
        employee_todos = response.json()

        # Display formatted details
        name = employee_details["username"]
        todos_arr = []
        for todo in employee_todos:
            todo_obj = {
                    "username": name,
                    "task": todo["title"],
                    "completed": todo["completed"],
                    }
            todos_arr.append(todo_obj)
        return (todos_arr)

    # Create final object
    final_obj = {}
    for employee in employee_ids:
        final_obj[employee] = individual_employee(employee)
    json_data = json.dumps(final_obj)

    # Save to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w", newline="") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    main()
