from fastapi import APIRouter

from app.models.employee import Employee

router = APIRouter()


@router.get("/employees")
def list_employees(limit: int = 10):
    employees = ["Alan", "Mikey"]
    response = {"Employees": employees, "Limit": limit}
    return response


@router.get("/employees/me")
def show_current_employee():
    return {"Employee ID": "The current employee's ID"}


@router.get("/employees/{employee_id}")
def show_employees(employee_id: int):
    return {"Employee ID": employee_id}


@router.post("/employees/")
def create_employee(employee: Employee):
    return {"Message": f"Employee {employee.name} is added successfully"}


@router.patch("/employees/{employee_id}")
def update_employee(employee: Employee):
    pass
