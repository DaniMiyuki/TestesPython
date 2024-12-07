from lista_de_tarefas import ListaDeTarefas

def teste_lista_de_tarefas_criar_tarefas():
    # Arrange
    ldt = ListaDeTarefas()
    nome = 'test'

    # Act
    t = ldt.cria_tarefa(nome)

    # Assert
    assert ldt.recuperar_tarefa(t.id)
    assert t.nome == nome
    assert t.status == 'a fazer'

def teste_lista_de_tarefas_recuperar_tarefa():
    ldt = ListaDeTarefas()

    # garante q veio None
    assert not ldt.recuperar_tarefa(10)

from tarefa import Tarefa  # Classe importada
from lista_de_tarefas import ListaDeTarefas  # Supondo que o código acima está neste arquivo

def teste_lista_de_tarefas_deletar_tarefa():
    # Arrange: Configura os objetos iniciais
    lista = ListaDeTarefas()
    tarefa1 = lista.cria_tarefa("Tarefa 1")
    tarefa2 = lista.cria_tarefa("Tarefa 2")
    
    assert len(lista.tarefas) == 2  # Garantir que temos duas tarefas inicialmente
    
    # Act: Executa o método a ser testado
    lista.deletar_tarefa(tarefa1.id)
    
    # Assert: Verifica os resultados
    assert len(lista.tarefas) == 1  # Deve sobrar apenas uma tarefa
    assert lista.recuperar_tarefa(tarefa1.id) is None  # A tarefa deletada não deve existir
    assert lista.recuperar_tarefa(tarefa2.id) is not None  # A tarefa restante deve existir


from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas

def test_atualiza_tarefa():
    # Arrange: Configuração inicial
    lista = ListaDeTarefas()
    tarefa1 = lista.cria_tarefa("Tarefa Inicial", "a fazer")

    # Garantir que a tarefa foi criada corretamente
    assert tarefa1.nome == "Tarefa Inicial"
    assert tarefa1.status == "a fazer"

    # Act: Atualizar o nome e status da tarefa
    lista.atualiza_tarefa(tarefa1.id, nome="Tarefa Atualizada", status="concluído")

    # Assert: Verificar se a tarefa foi atualizada
    tarefa_atualizada = lista.recuperar_tarefa(tarefa1.id)
    assert tarefa_atualizada is not None
    assert tarefa_atualizada.nome == "Tarefa Atualizada"
    assert tarefa_atualizada.status == "concluído"
