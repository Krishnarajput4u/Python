import json
import os
from datetime import date, datetime
from getpass import getpass

# ---------------- File Handling ----------------
USERS_FILE = "users.json"
TASKS_FILE = "tasks.json"
PROGRESS_FILE = "progress.json"


# Clear the terminal window for a fresh screen-based UI flow.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Return a horizontal separator line with a configurable width.
def line(width=70):
    return "-" * width


# Truncate long text to fit a fixed-width table column.
def trim(value, width):
    if len(value) <= width:
        return value
    return value[: width - 3] + "..."


# Render a standard page header with title, user, and current date.
def draw_screen(title, user=None):
    clear_screen()
    print(line())
    print(f"{title:^70}")
    print(line())
    if user:
        print(f"User: {user['username']}    Date: {date.today().isoformat()}")
    else:
        print(f"Date: {date.today().isoformat()}")
    print(line())


# Show a result/feedback page and pause until the user continues.
def show_result(message, user=None):
    draw_screen("Result", user)
    print(message)
    print(line())
    input("Press Enter to continue...")


# Print a simple numbered menu from a list of (key, label) tuples.
def render_menu(title, options):
    print(f"{title}")
    print(line())
    for key, label in options:
        print(f"{key}. {label}")
    print(line())


# Parse a YYYY-MM-DD string into a date object, or None if invalid.
def parse_deadline(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


# Return task timing status and day delta based on today's date.
def task_status(deadline_value):
    deadline_date = parse_deadline(deadline_value)
    if deadline_date is None:
        return "Invalid", "-"

    days_left = (deadline_date - date.today()).days
    if days_left < 0:
        return "Overdue", str(days_left)
    if days_left <= 2:
        return "Due Soon", str(days_left)
    return "On Track", str(days_left)


# Generate the next task ID without reusing deleted IDs.
def next_task_id(tasks):
    return max((t.get("id", 0) for t in tasks), default=0) + 1


# Create a plain-text progress bar for completion percentage.
def render_progress_bar(completed, total, width=28):
    if total <= 0:
        return "No tasks yet"

    ratio = completed / total
    filled = int(ratio * width)
    empty = width - filled
    return f"{'#' * filled}{'.' * empty} {int(ratio * 100)}%"


# Keep prompting until the user enters one of the valid menu choices.
def prompt_choice(prompt_text, valid_choices):
    while True:
        choice = input(f"{prompt_text}: ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Try again.")


# Prompt for yes/no input with a default value when left blank.
def prompt_yes_no(prompt_text, default=True):
    suffix = "[Y/n]" if default else "[y/N]"
    while True:
        value = input(f"{prompt_text} {suffix}: ").strip().lower()
        if not value:
            return default
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False
        print("Please enter y or n.")


# Load JSON data from disk and return an empty list if missing/invalid.
def load_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


# Persist Python data as pretty-printed JSON to disk.
def save_file(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- Auth Functions ----------------
# Register a new user account and store credentials in users.json.
def register():
    draw_screen("Create Account")
    username = input("Username: ").strip()
    password = getpass("Password: ")

    if not username or not password:
        show_result("Username and password cannot be empty.")
        return

    users = load_file(USERS_FILE)
    if any(u["username"] == username for u in users):
        show_result("Username already exists.")
        return

    user = {"id": len(users) + 1, "username": username, "password": password}
    users.append(user)
    save_file(USERS_FILE, users)
    show_result("Registration successful.")


# Authenticate a user by username/password and return the matched user.
def login():
    draw_screen("Login")
    username = input("Username: ").strip()
    password = getpass("Password: ")

    users = load_file(USERS_FILE)
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)
    if user:
        show_result(f"Welcome {username}.")
        return user
    else:
        show_result("Invalid credentials.")
        return None

# ---------------- Task Functions ----------------
    # Display all tasks for a specific user in a compact table layout.
def show_tasks(user_id):
    tasks = load_file(TASKS_FILE)
    user_tasks = [t for t in tasks if t["user_id"] == user_id]

    if not user_tasks:
        print("No tasks found.")
        print("Use option 2 to add your first task.")
        return

    print("ID  Title                    Deadline     Priority  Status    Days")
    print(line())

    for task in user_tasks:
        status_text, days_left = task_status(task["deadline"])
        print(
            f"{str(task['id']):<3} "
            f"{trim(task['title'], 24):<24} "
            f"{task['deadline']:<12} "
            f"{task['priority']:<8} "
            f"{status_text:<9} "
            f"{days_left:>4}"
        )
    print(line())


# Collect task details, validate them, and add a new task for the user.
def add_task(user_id, user=None):
    draw_screen("Add Task", user)
    title = input("Task Title: ").strip()

    if not title:
        show_result("Task title cannot be empty.", user)
        return

    deadline = input("Deadline (YYYY-MM-DD): ").strip()
    while parse_deadline(deadline) is None:
        print("Invalid date format. Use YYYY-MM-DD.")
        deadline = input("Deadline (YYYY-MM-DD): ").strip()

    print("Priority options: Low, Medium, High")
    priority = input("Priority: ").strip().title()
    while priority not in {"Low", "Medium", "High"}:
        print("Priority must be Low, Medium, or High.")
        priority = input("Priority: ").strip().title()

    tasks = load_file(TASKS_FILE)
    task_id = next_task_id(tasks)
    task = {"id": task_id, "title": title, "deadline": deadline, "priority": priority, "user_id": user_id}
    tasks.append(task)
    save_file(TASKS_FILE, tasks)
    show_result(f"Task added: {title}", user)


# Mark a chosen task as complete and log completion in progress.json.
def complete_task(user_id, user=None):
    tasks = load_file(TASKS_FILE)
    user_tasks = [t for t in tasks if t["user_id"] == user_id]

    if not user_tasks:
        show_result("No tasks to complete.", user)
        return

    draw_screen("Complete Task", user)
    show_tasks(user_id)

    task_id_text = input("Enter Task ID to complete: ").strip()
    if not task_id_text.isdigit():
        show_result("Task ID must be a number.", user)
        return

    task_id = int(task_id_text)

    task = next((t for t in tasks if t["id"] == task_id and t["user_id"] == user_id), None)
    if not task:
        show_result("Task not found.", user)
        return

    if not prompt_yes_no(f"Mark '{task['title']}' as complete?", default=True):
        show_result("Completion canceled.", user)
        return

    tasks.remove(task)
    save_file(TASKS_FILE, tasks)

    progress = load_file(PROGRESS_FILE)
    progress.append({"user_id": user_id, "status": "completed"})
    save_file(PROGRESS_FILE, progress)

    show_result(f"Task completed: {task['title']}", user)


# Show completed-vs-total progress summary for the current user.
def show_progress(user_id, user=None):
    draw_screen("Your Progress", user)
    progress = load_file(PROGRESS_FILE)
    completed_count = sum(1 for p in progress if p["user_id"] == user_id and p["status"] == "completed")
    tasks = load_file(TASKS_FILE)
    # Total includes active tasks plus the ones already completed.
    total_tasks = len([t for t in tasks if t["user_id"] == user_id]) + completed_count

    bar = render_progress_bar(completed_count, total_tasks)
    print(f"Completed: {completed_count}")
    print(f"Total:     {total_tasks}")
    print(f"Progress:  {bar}")
    print(line())
    input("Press Enter to continue...")

# ---------------- Dashboard ----------------
# Run the logged-in user dashboard loop until logout.
def student_dashboard(user):
    options = [
        ("1", "Show Tasks"),
        ("2", "Add Task"),
        ("3", "Complete Task"),
        ("4", "Show Progress"),
        ("5", "Logout"),
    ]

    while True:
        draw_screen("Student Dashboard", user)
        render_menu("Select an action", options)
        choice = prompt_choice("Choose an option", {"1", "2", "3", "4", "5"})

        if choice == "1":
            draw_screen("Your Tasks", user)
            show_tasks(user["id"])
            input("Press Enter to continue...")
        elif choice == "2":
            add_task(user["id"], user)
        elif choice == "3":
            complete_task(user["id"], user)
        elif choice == "4":
            show_progress(user["id"], user)
        elif choice == "5":
            break

# ---------------- Main Loop ----------------
# Run the main application loop for login, registration, and exit.
def main():
    options = [
        ("1", "Login"),
        ("2", "Register"),
        ("3", "Exit"),
    ]

    while True:
        draw_screen("GoalSync Task Manager")
        render_menu("Main Menu", options)
        choice = prompt_choice("Choose an option", {"1", "2", "3"})
        if choice == "1":
            user = login()
            if user:
                student_dashboard(user)
        elif choice == "2":
            register()
        elif choice == "3":
            draw_screen("Goodbye")
            print("Thanks for using GoalSync.")
            print(line())
            break

# Entry point when running this file directly.
if __name__ == "__main__":
    main()

