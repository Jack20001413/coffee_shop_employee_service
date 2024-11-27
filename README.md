# coffee_shop_employee_service

This is the service for managing employees in a coffee shop

## Project Structure

Since this project is a microservice included in a larger project, file-type based structuring approach is prefered to use for this project.

Ref: [FastAPI Project Structuring Practices](https://medium.com/@amirm.lavasani/how-to-structure-your-fastapi-projects-0219a6600a8f)

## ERD

```mermaid
---
title: Employee Managment System
---
erDiagram
    Employee ||--|{ EmployeePosition: is
    Position ||--|{ EmployeePosition: assigned
    Store ||--|{ Employee: "works at"
    Employee ||--|{ Leave: leaves
    Job ||--|| Position: describes
    Employee ||--|{ Payroll: receives
    Salary ||--|{ Payroll: includes
    Employee ||--|{ JobApplicationHistory: applies
    Job ||--|{ JobApplicationHistory: records
    Payroll ||--|{ Leave: includes
    Payroll ||--|{ Job: includes
    Employee {
        int id PK
        string name
        string gender
        date_time date_of_birth
        string contact_address
        string phone_number
        int age
        int workplaceId FK
        date_time created_at
        date_time updated_at
    }
    Store {
        int id
        string name
        string address
        date_time created_at
        date_time updated_at
    }
    EmployeePosition {
        int employee_id PK,FK
        int position_id PK,FK
        date_time start_date
        date_time end_date
    }
    Position {
        int id PK
        string name
        date_time created_at
        date_time updated_at
    }
    Leave {
        int id PK
        date_time leave_date
        string reason
        int employee_id FK
        int payroll_id FK
        date_time created_at
        date_time updated_at
    }
    Job {
        int id PK
        string name
        string description
        tuple salary_range
        int position_id FK
        date_time created_at
        date_time updated_at
    }
    Salary {
        int id PK
        float amount
        float bonus
        date_time created_at
        date_time updated_at
    }
    Payroll {
        int id PK
        uuid payroll_uuid
        int employee_id FK
        int salary_id FK
        int job_id FK
        date_time payday
        float total_amount
    }
    JobApplicationHistory {
        int id PK
        date_time join_date
        int job_id FK
        int employee_id FK
        date_time created_at
        date_time updated_at
    }
```

## Best Practices

Ref: [Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
