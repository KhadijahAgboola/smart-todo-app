# src/parsers/task_parser.py
from src.parsers.regex_patterns import Tags, Priority, Due, Assigned, Time, Duration
from src.parsers.validator import TaskValidator


def parse_task_input(task_input):
    """
    Parses a raw task input string and returns a dictionary
    with structured components: description, tags, priority, due, assigned, time, duration
    Also validates each using regex-based validator.
    """

    # Extract tags
    tags = Tags.findall(task_input)
    valid_tags = [tag for tag in tags if TaskValidator.is_valid_tag(f"@{tag}")]
    invalid_tags = [tag for tag in tags if not TaskValidator.is_valid_tag(f"@{tag}")]

    # Extract priority
    priority = None
    prio_match = Priority.search(task_input)
    if prio_match:
        pr_value = f"#{prio_match.group(1)}"
        priority = pr_value if TaskValidator.is_valid_priority(pr_value) else None

    # Extract due date
    due = None
    due_match = Due.search(task_input)
    if due_match:
        due_value = due_match.group(1)
        if due_value in ["tomorrow", "next week"] or TaskValidator.is_valid_date(due_value):
            due = due_value

    # Extract assigned email
    assigned = None
    assigned_match = Assigned.search(task_input)
    if assigned_match:
        assigned_value = assigned_match.group(1)
        assigned = assigned_value  # Email already validated by regex

    # Extract time
    time = None
    time_match = Time.search(task_input)
    if time_match:
        time = time_match.group(1)

    # Extract duration
    duration = None
    duration_match = Duration.search(task_input)
    if duration_match:
        duration = duration_match.group(1)

    # Clean description (remove all special patterns from content)
    description = task_input
    for pattern in [Tags, Priority, Due, Assigned, Time, Duration]:
        description = pattern.sub('', description)
    description = description.strip()

    return {
        "description": description,
        "tags": valid_tags,
        "invalid_tags": invalid_tags,   # ✅ Optional: helpful for feedback
        "priority": priority,
        "due": due,
        "assigned": assigned,
        "time": time,
        "duration": duration
    }

