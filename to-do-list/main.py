import sys
from tabulate import tabulate
from datetime import date


def main():
    tasks = []
    code = 0
    while True:
        print(menu())
        choice = int(input("Enter the key: "))
        try:
            if choice == 1:
                code += 1
                x = create_task()
                x["code"] = code
                tasks.append(x)
            
            elif choice == 2:
                print("TASKS")
                print(view_tasks(tasks))
            
            elif choice == 3:
                print(view_tasks(tasks))
                tasks = update(tasks)
                print(view_tasks(tasks))

            elif choice == 5:
                sys.exit()

        except ValueError:
            print("Code does not exit")
            pass

def delete():
    return ''


def view_tasks(tasks):
    header = tasks[0].keys()
    rows = [i.values() for i in tasks]
    return tabulate(rows, header, tablefmt="rounded_outline")

def create_task():
    date_created = date.today()
    task = input("Enter the task: ")
    date_due = input("Enter due date: ")
    status = "unfinished"
    code = ''
    return {'code': code, 'date created': date_created, 'date due': date_due, 'task': task, 'status': status}

def update(tasks):
    while True:
        try: 
            enter_code = input("Enter code: ")
            x = input("what do you want edit: ")
            for i in tasks:
                if int(enter_code) == i['code']:
                    if x in ["code", "date created", "date due", "task", "status"]:
                        i[x] = input("Enter new value: ")
                        break
            break
        except ValueError:
            pass
    return tasks
            
def menu():
    table = [
        {"code": "1", "option": "Create Task"},
        {"code": "2", "option": "View Tasks"}, 
        {"code": "3", "option": "Update"},
        {"code": "4", "option": "Delete"},
        {"code": "5", "option": "Save as csv"},
        {"code": "6", "option": "Exit"}
    ]
    header = table[0].keys()
    rows = [x.values() for x in table]
    return f"Main Menu\n{tabulate(rows, header, tablefmt='rounded_outline')}"

if __name__ == "__main__":
    main()