class User:
    """
    Класс отвечающий за создание User с его атрибутами
    """
    def __init__(self, user_id, name, level):
        self.id = user_id
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.name} ({self.id}, {self.level})'

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __hash__(self):
        return hash(f'{self.id}')
