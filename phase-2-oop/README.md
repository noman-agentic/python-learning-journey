# Phase 2 — Object-Oriented Programming (OOP)

## Topics Learned
- **Step 16:** Classes and objects
- **Step 17:** Attributes, methods, and `__init__`
- **Step 18:** Inheritance and polymorphism
- **Step 19:** Dunder methods (`__str__`, `__repr__`)
- **Step 20:** Decorators (basic concept and custom decorators)

## Why This Matters
Modern AI agent frameworks (LangChain, LangGraph) are built heavily on OOP. Understanding classes, inheritance, and decorators makes framework code readable instead of "magic".

## Mini-Project: Task Manager with OOP
A small task management system demonstrating core OOP concepts:
- `Task` base class with attributes and methods
- `UrgentTask` subclass using inheritance
- Overridden `__str__` for readable object output
- Custom `@log_action` decorator that logs method calls

### How to Run
```bash
cd phase-2-oop/mini-project
python phase2_mini_project.py
```

See `sample_output.txt` for example output.