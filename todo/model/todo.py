
class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int =  code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True
        return self.completed

    def add_tag(self, tag):
        if tag is not self.tags:
            self.tags.append(tag)

    def __str__(self):
        return str(f"{self.code_id} - {self.title}")


class TodoBook:

    def __init__(self):
        self.todos: dict[int,Todo] = {}

    def add_todo(self, title: str,  description: str):
        id: int = len(self.todos)
        valor = Todo(id, title, description) #Creando objeto
        self.todos[id] = valor

    def pending_todos(self,):
        for todos in self.todos:
            return






        return








