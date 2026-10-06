# Employee payroll API

Flask REST API backed by MySQL. The database and the `employees` and `payroll`
tables are created automatically on the first request. The MySQL user needs
permission to create the configured database and tables.

## Start

From this `BACKEND` directory, install dependencies and set your MySQL details:

```powershell
py -m pip install -r requirements.txt
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your-mysql-password"
$env:MYSQL_DATABASE = "employee_payroll"
py APP.py
```

The API listens on `http://127.0.0.1:5000`. Do not commit real database
passwords. Set `FLASK_HOST=0.0.0.0` only when the server should accept traffic
from other machines, and put it behind appropriate network access controls.

## Routes

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/api/health` | Check API and MySQL connection |
| GET | `/api/employees` | List employees |
| POST | `/api/employees` | Add employee |
| GET | `/api/employees/<id>` | Get one employee |
| PUT | `/api/employees/<id>` | Replace employee details |
| DELETE | `/api/employees/<id>` | Delete employee and their payroll rows |
| GET | `/api/payroll` | List payroll rows with employee names |
| POST | `/api/payroll` | Create a payroll row and calculate net salary |

Send JSON with `Content-Type: application/json`. Employee creation/update fields:
`employee_code`, `first_name`, `last_name`, `email`, `department`, `job_title`,
`hire_date` (`YYYY-MM-DD`). Payroll fields: `employee_id`, `pay_period`
(`YYYY-MM`), `basic_salary`, optional `allowances` and `deductions`, optional
`status` (`pending` or `paid`), and optional `payment_date` (`YYYY-MM-DD`). A
single payroll row is allowed per employee per month. Monetary values are
returned as decimal strings to avoid floating-point rounding.
