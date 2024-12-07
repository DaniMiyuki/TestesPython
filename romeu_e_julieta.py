# FizzBuzz

def romeu_e_julieta(val: int):
    """
    Param:
        val: int (numero)
    
    Se val for divisivel por 3 -> 'Queijo'
    Se val for divisivel por 5 -> 'Goiabada'
    Se val for divisivel por 3 e 5 -> 'Romeu e Julieta'
    Se val NAO for divisivel por por 3 ou 5 -> val
    
    """
    match val % 3 == 0, val % 5 == 0:
        case [True, False]:
            return 'Queijo'
        case [False, True]:
            return 'Goiabada'
        case [True, True]:
            return 'Romeu e Julieta'
        case _:
            return val