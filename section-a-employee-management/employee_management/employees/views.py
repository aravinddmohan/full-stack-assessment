from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee

# CREATE EMPLOYEE
def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            department=request.POST.get('department'),
            salary=request.POST.get('salary')
        )
        return redirect('/list')
    return render(request, 'employees/add_employee.html')

# READ EMPLOYEE (ACTIVE ONES)
def employee_list_view(request):
    employees = Employee.objects.filter(status=Employee.ACTIVE)
    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })

# READ EMPLOYEE VIA ID
def get_employee_by_id(request,emp_id):
    employee = get_object_or_404(
         Employee,
         id=emp_id,
         status=Employee.ACTIVE
    )
    return render(request, 'employees/employee_detail.html', {
        'employee': employee
    })
    
# UPDATE EMPLOYEE
def update_employee(request,emp_id):
    employee=get_object_or_404 (Employee, id=emp_id)
    if request.method=='POST':
            employee.name=request.POST['name']
            employee.department=request.POST['department']
            employee.salary=request.POST['salary']
            employee.save()
            return redirect('/list')
    return render(request, 'employees/update_employee.html', {
        'employee': employee
    })

# DELETE EMPLOYEE
def delete_employee(request,emp_id):
    employee=get_object_or_404 (Employee, id=emp_id)
    if request.method=='POST':
        employee.status=Employee.INACTIVE
        employee.save()
        return redirect('/list')