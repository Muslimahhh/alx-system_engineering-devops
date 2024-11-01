#!/usr/bin/python3
"""
Use the requests module to make a request to an employee REST API
    The request takes in an integer that serves as the employee ID
"""
import requests
import sys


def main():
    """
    This is the main function for the program
    """
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit("Not enough information")
    employee_id = sys.argv[1]

    # Make the GET request
    url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    response = requests.get(url)
    employee_details = response.json()

    url = url + "/todos"
    response = requests.get(url)
    employee_todos = response.json()

    # Display formatted details
    name = employee_details["name"]
    no_todos = len(employee_todos)
    done_todos = [todo for todo in employee_todos if todo['completed']]
    no_done_todos = len(done_todos)

    print(f"Employee {name} is done with tasks({no_done_todos}/{no_todos}):")
    for todo in done_todos:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    main()
