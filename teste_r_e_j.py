from romeu_e_julieta import Romeu_e_julieta

def test_romeu_e_julieta_deve_retornar_queijo():
    """
    AAA = Arrange Act Assert
    4 fases:

    """

    # Arrange
    valor_de_input = 3
    esperado = 'Queijo'

    # Act
    resultado = Romeu_e_julieta(valor_de_input)

    # Assert
    assert resultado == esperado


def test_romeu_e_julieta_deve_retornar_goiabada():
    valor_de_input = 5
    esperado = 'Goiabada'

    resultado = Romeu_e_julieta(valor_de_input)

    assert resultado == esperado


def test_romeu_e_julieta_deve_retornar_ReJ():
    valor_de_input = 15  # este valor e multiplo de 3 e 5 ao mesmo tempo como e esperado na funcao
    esperado = 'Romeu e Julieta'

    resultado = Romeu_e_julieta(valor_de_input)

    assert resultado == esperado


def test_romeu_e_julieta_deve_retornar_val():
    valor_de_input = 1  # este valor nao e multiplo de 3 nem 5 como e esperado na funcao
    esperado = 1

    resultado = Romeu_e_julieta(valor_de_input)

    assert resultado == esperado

