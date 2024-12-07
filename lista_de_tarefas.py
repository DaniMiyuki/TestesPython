from tarefa import Tarefa
# Lista de tarefas 

class ListaDeTarefas:
    """
    (Teste de DOC - Depende de outro componente para ser testado, 
    no caso ele depende do Tarefa)

    """
    def __init__(self) -> None:
        self.tarefas: list[Tarefa] = []
        self.contador_de_id = 1 # inicia sempre em 1

    def cria_tarefa(self, nome, status='a fazer') -> None:
        t = Tarefa(self.contador_de_id, nome, status) # cada tarefa criada, armazena na variavel t
        self.tarefas.append(t)  # a lista terefas adiciona cada t(tarefa)
        self.contador_de_id += 1

        return t
    def atualiza_tarefa(
            self,
            identificador: int,
            nome: str | None = None,
            status: str | None = None
    ) -> None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                if nome:
                    tarefa.nome = nome
                if status:
                    tarefa.status = status
                break

    def deletar_tarefa(self, identificador: int) -> None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                self.tarefas.remove(tarefa)
            break
    
    def recuperar_tarefa(self, identificador: int) -> Tarefa | None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                return tarefa
        return None