from main import delete, view_tasks, update, create_task
from operator import __sub__
from tabulate import tabulate
from datetime import date

def main():
    test_delete()
    test_update()


def test_delete():
    assert delete([{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "40 days",
             'task': 'cleaning', 'status': "In-progress"}], 0) == []
    
    assert delete([{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "40 days",
             'task': 'cleaning', 'status': "In-progress"}], 1) == [{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "40 days",
             'task': 'cleaning', 'status': "In-progress"}]
    

def test_update():
    assert update([{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "40 days",
             'task': 'cleaning', 'status': "In-progress"}], "0", "3", "") == [{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "--------",
             'task': 'cleaning', 'status': "Done"}]
    assert update([{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "40 days",
             'task': 'cleaning', 'status': "In-progress"}], "0", "1", "cooking") == [{'code': 0, 'date created': "2024-09-01", 'date due': '2024-10-10', 'days remaining': "40 days",
             'task': 'cooking', 'status': "In-progress"}]
    
def test_view():
    assert view_tasks([]) == tabulate([], ['code', 'date created', 'date due', 'days remaining', 'task', 'status'], tablefmt="rounded_outline")

def test_create():
    assert create_task("cleaning", "2024-09-02") == {'code': '', 'date created': date.today(), 'date due': '2024-09-02', 'days remaining': "",
             'task': 'cleaning', 'status': "In-progress"}
    
    assert create_task("cooking", "2024-10-10") == {"code": '', "date created": date.today(), "date due": "2024-10-10",
                                                    "days remaining": "", "task": "cooking", "status": "In-progress"}


if __name__ == "__main__":
    main()