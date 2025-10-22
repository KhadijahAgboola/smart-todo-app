# **Smart Todo Application**

A command-line Todo app that uses regular expressions to intelligently parse and manage tasks.

---

## **Project Structure**
smart-todo-app/

├── src/
│ ├── main.py
│ ├── models/
│ │ ├── task.py
│ │ └── todo_list.py
│ ├── parsers/
│ │ ├── regex_patterns.py
│ │ ├── task_parser.py
│ │ ├── date_parser.py
│ │ └── validator.py
│ ├── services/
│ │ ├── task_service.py
│ │ └── storage_service.py
│ └── cli/
│ └── interface.py
├── tests/
│ ├── test_task_parser.py
│ ├── test_date_parser.py
│ ├── test_validator.py
│ ├── test_task_service.py
│ └── test_regex_patterns.py
├── data/
│ └── tasks.json
├── README.md
├── pyproject.toml
└── .gitignore



---

## **Core Features**

### Task Management
- Add, update, delete, and list tasks
- Mark tasks as complete/incomplete
- Persistent storage using JSON

### Smart Task Parsing with Regex
- Parse natural language input:
"Buy groceries @shopping #high due:2025-10-20 assigned:alice@example.com"

- Extract components using regex:
- Task description
- Tags (`@shopping`, `@work`, `@personal`)
- Priority (`#high`, `#medium`, `#low`)
- Due dates (`due:YYYY-MM-DD`, `due:tomorrow`, `due:next week`)
- Assigned email (`assigned:alice@example.com`)
- Extract time patterns (`at 3pm`, `by 5:30 PM`)
- Validate email addresses for task assignment

### Search & Filter
- Search tasks by keyword patterns
- Filter by tags using regex
- Find tasks with specific date patterns
- Search by priority levels

### Task Validation
- Use regex to validate:
- Date formats
- Priority levels
- Tag naming conventions
- Task ID formats

---

## **Installation**

1. Clone the repository:
```bash
git clone https://github.com/KhadijahAgboola/smart-todo-app.git

2. Enter the project directory:
cd smart-todo-app

3. Install dependencies using Poetry:
poetry install

4. Run the application:
poetry run python src/main.py


