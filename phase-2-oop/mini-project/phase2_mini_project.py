def log_action(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__ + "()...")
        return func(*args, **kwargs)
    return wrapper

class Task:
    def __init__(self, title, status="pending"):
        self.title = title
        self.status = status

    @log_action
    def mark_done(self):
        self.status = "done"

    def __str__(self):
        return f"[{self.status}] {self.title}"


class UrgentTask(Task):
    def __init__(self, title, deadline, status="pending"):
        super().__init__(title, status)
        self.deadline = deadline

    def __str__(self):
        return f"[{self.status}] {self.title} - {self.deadline}"
প

task1 = Task("Complete mini project")
task1.mark_done()
print(task1)
task2 = UrgentTask("AI Agent Mastery Course", "November 30, 2026")
print(task2)


