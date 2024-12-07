from romeu_e_julieta import romeu_e_julieta

def test_romeu_e_julieta_deve_retornar_queijo():
    """
    AAA = Arrange Act Assert
    4 fases:

    """

    # Arrange
    valor_de_input = 3
    esperado = 'Queijo'

    # Act
    resultado = romeu_e_julieta(valor_de_input)

    # Assert
    assert resultado == esperado

