from tarefa import Tarefa

def teste_Tarefa_deve_conter_os_campos_id_nome_status():
    # arrange
    identificador = 1
    nome = 'Estudar Testes'
    status = 'fazendo'

    # Act
    t = Tarefa(identificador, nome, status)

    # Assert
    assert t.id == identificador
    assert t.nome == nome
    assert t.status == status
