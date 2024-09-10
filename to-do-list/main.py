import sys
from tabulate import tabulate
from datetime import date
import csv
from operator import __sub__


def main():
    tasks = []
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a CSV file")
        else:
            try:
                with open(sys.argv[1]) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        tasks.append(row)

            except FileNotFoundError:
                sys.exit("File does not exixt")
    while True:
        print(menu())
        choice = int(input("Enter the code: "))
        try:
            if choice == 1:
                task = input("Enter the task: ")
                while True:
                    try:
                        date_due = date.fromisoformat(input("Enter due date(YYYY-MM-DD): "))
                        break
                    except ValueError:
                        pass
                tasks.append(create_task(task, date_due))

                for i, task in enumerate(tasks):
                    task['code'] = i
                for i in tasks:
                    i['days remaining'] = __sub__(i['date due'], i['date created']).days
            elif choice == 2:
                print("\nTASKS")
                print(view_tasks(tasks))
            
            elif choice == 3:
                print(view_tasks(tasks))
                while True:
                    try:
                        enter_code = input("Enter code: ")
                        x = input("1. Edit task\n2. Edit date due\n3. Edit status\nChoose an option: ")
                        if x == "1":
                            value = input("Enter new task:")
                            tasks = update(tasks, enter_code, x, value)
                        elif x == "2":
                            value = input("Enter new due date(YYYY-MM-DD): ")
                            tasks = update(tasks, enter_code, x, value)

                        elif x == "3":
                            tasks = update(tasks, enter_code, x)
                        break
                    except ValueError:
                        pass
                print(view_tasks(tasks))

            elif choice == 4:
                print(view_tasks(tasks))
                while True:
                    try:
                        enter_code = input("Enter code: ")
                        tasks = delete(tasks, enter_code)
                        break
                    except ValueError:
                        pass

            elif choice == 5:
                name = input('Enter the name of file: ') + '.csv'
                with open(name, 'w') as file:
                    fieldnames = tasks[0].keys()
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerows(tasks)

            elif choice == 6:
                sys.exit()

            else:
                print("Invalid code")

        except ValueError:
            print("Digits only")
            pass

def delete(tasks, code):
    new_tasks = [i for i in tasks if int(code) != i['code']]
    return new_tasks

def view_tasks(tasks):
    header = ['code', 'date created', 'date due', 'days remaining', 'task', 'status']
    rows = [i.values() for i in tasks]
    return tabulate(rows, header, tablefmt="rounded_outline")

def create_task(task, date_due):
    date_created = date.today()
    status = "In-progress"
    code = ''
    days_remaining = ""
    return {'code': code, 'date created': date_created, 'date due': date_due, 'days remaining': days_remaining,
             'task': task, 'status': status}

def update(tasks, code, choice, new_value=""):
    for i in tasks:
        if int(code) == i['code']:
            if choice  == '1':
                i['task'] = new_value
            elif choice == '2':
                while True:
                    try:
                        i['date due'] = date.fromisoformat(new_value)
                        i['days remaining'] = __sub__(i['date due'], i['date created']).days
                        break
                    except ValueError:
                         pass
            elif choice == '3':
                i['status'] = 'Done'
                i['days remaining'] = '--------'
    return tasks
            
def menu():
    table = [
        {"code": "1", "option": "Create Task"},
        {"code": "2", "option": "View Tasks"}, 
        {"code": "3", "option": "Update Task"},
        {"code": "4", "option": "Delete Task"},
        {"code": "5", "option": "Save as csv"},
        {"code": "6", "option": "Exit"}
    ]
    header = table[0].keys()
    rows = [x.values() for x in table]
    return f"\n      Main Menu\n{tabulate(rows, header, tablefmt='rounded_outline')}"

if __name__ == "__main__":
    main()