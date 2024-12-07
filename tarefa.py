# Todo List

from dataclasses import dataclass

@dataclass
class Tarefa:
    id: int
    nome: str
    status: str = 'a fazer'