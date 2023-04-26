from emp.models import Emp

def get_all_emps():
    emps = Emp.objects.all()
    return emps
