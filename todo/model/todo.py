class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id : int = code_id
        self.title: str = title
        self.description = description
        self.completed: bool = False
        self.tags: (list[str]) = []

    def mark_completed(self):
        self.completed = True
        return

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return str(f"{self.code_id} - {self.title}")

    class TodoBook:

        def __init__(self):
            self.todos: dict[int, Todo] = {}

        def add_todo(self, title: str, description: str):
            id: int = len(self.todos) + 1
            valor = Todo(id, title, description)
            self.todos[id] = valor
            return id

        def pending_todos(self):
            return [todo for todo in self.todos.values() if not todo.completed]

        def completed_todos(self):
            return [todo for todo in self.todos.values() if todo.completed]

        def tags_todo_count(self):
            tag_count: dict = {}















