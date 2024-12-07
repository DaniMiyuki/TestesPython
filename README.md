# FizzBuzz  

### Param:
###    val: int (numero)

### Se val for multiplo de 3 -> 'Queijo'
### Se val for multiplo de 5 -> 'Goiabada'
### Se val for multiplo de 3 e 5 -> 'Romeu e Julieta'
### Se val NAO for multiplo de 3 e 5 -> val

## Metodologia TDD  

O que é TDD?
TDD (Test-Driven Development) é uma metodologia de desenvolvimento que segue um ciclo rigoroso:

- RED: Escreva um teste que falha: Comece escrevendo um teste unitário baseado no requisito esperado (mas o código ainda não existe).
- GREEN: Implemente o código: Escreva o mínimo de código necessário para fazer o teste passar.
- REFACTOR: Melhore o código sem alterar o comportamento.


## Taxionomia dos testes  

O que é AAA?
AAA é um padrão amplamente usado para estruturar testes unitários. Ele divide um teste em três fases claras:

- ARRANGE (Preparar)
Configure o cenário de teste. Inicialize objetos, defina dependências, e prepare os dados necessários.  
    valor_de_input = 3  
    esperado = 'Queijo'

- ACT (Agir)
Execute o comportamento ou ação que está sendo testada.  
    resultado = romeu_e_julieta(valor_de_input)

- ASSERT (Verificar)
Verifique se os resultados obtidos estão de acordo com o esperado.  
    assert resutado == esperado

- TEARDOWN
Quando usar o Teardown?
Você só precisa da quarta fase (Teardown) quando o teste pode:

    - Criar efeitos colaterais que afetam outros testes.  
    - Consumir recursos externos, como arquivos, conexões de banco de dados, ou APIs.  
    - Usar mocks ou spies que devem ser limpos após o teste.  

## Conexão entre AAA e TDD  

AAA é usado dentro do ciclo TDD para estruturar os testes.
Quando você escreve testes no TDD, o padrão AAA ajuda a organizá-los de forma clara e compreensível.

TDD depende de bons testes, e AAA fornece uma base sólida para isso.
Com AAA, os testes ficam mais legíveis e intuitivos, o que é crucial para a prática de TDD.

### Instalacoes 

Use o comando `python -m venv venv` para criar um ambiente virtual.
Intale as ferramentas para teste e covered: `pip install pytest pytest-cov`
Atualize o pip, caso necessario: `python.exe -m pip install --upgrade pip`
