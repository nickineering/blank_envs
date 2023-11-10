import csv

from dotenv import load_dotenv
from requests import get


def get_employees():
    load_dotenv()

    url = "https://s3.eu-west-2.amazonaws.com/interview.thanskben.com/backend/employees.json"
    response = get(url)
    employees = response.json()
    return employees


def get_name(first_name, last_name):
    result_first = first_name
    length = len(f"{first_name} {last_name}")
    if length > 15:
        result_first = f"{first_name[0]}."
    return f"{result_first} {last_name}"


def main():
    employees = get_employees()

    with open("output.csv", "w", newline="\n") as csvfile:
        output_writer = csv.writer(csvfile, delimiter=";")
        output_writer.writerow(["email", "short full name"])

        for employee in employees:
            name = get_name(employee["first name"], employee["last name"])
            line = [employee["email"], name]
            output_writer.writerow(line)


if __name__ == "__main__":
    main()
