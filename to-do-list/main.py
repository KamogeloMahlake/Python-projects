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
                tasks.append(create_task())
                for i, task in enumerate(tasks):
                    task['code'] = i
            elif choice == 2:
                print("TASKS")
                print(view_tasks(tasks))
            
            elif choice == 3:
                print(view_tasks(tasks))
                tasks = update(tasks)
                print(view_tasks(tasks))

            elif choice == 4:
                print(view_tasks(tasks))
                tasks = delete(tasks)
                print(view_tasks(tasks))

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

def delete(tasks):
    try:
        enter_code = input("Enter code: ")
        new_tasks = [i for i in tasks if int(enter_code) != i['code']]
        return new_tasks
    except ValueError:
        pass

def view_tasks(tasks):
    header = ['code', 'date created', 'date due', 'days remaining', 'task', 'status']
    rows = [i.values() for i in tasks]
    return tabulate(rows, header, tablefmt="rounded_outline")

def create_task():
    date_created = date.today()
    task = input("Enter the task: ")
    while True:
        try:
            date_due = date.fromisoformat(input("Enter due date(YYYY-MM-DD): "))
            break
        except ValueError:
            pass
    status = "In-progress"
    code = ''
    days_remaining = __sub__(date_due, date_created).days
    return {'code': code, 'date created': date_created, 'date due': date_due, 'days remaining': days_remaining,
             'task': task, 'status': status}

def update(tasks):
    try: 
        enter_code = input("Enter code: ")
        x = input("1. Edit task\n2. Edit date due\n3. Edit status\nChoose an option: ")
        for i in tasks:
            if int(enter_code) == i['code']:
                if x  == '1':
                    i['task'] = input('Input updated task: ')
                elif x == '2':
                    while True:
                        try:
                            i['date due'] = date.fromisoformat(input("Enter new due date(YYYY-MM-DD): "))
                            i['days remaining'] = __sub__(i['date due'], i['date created'])
                            break
                        except ValueError:
                            pass
                elif x == '3':
                    i['status'] = 'Done'
                    i['days remaining'] = '--------'
                return tasks
        return tasks
    except ValueError:
        pass
            
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