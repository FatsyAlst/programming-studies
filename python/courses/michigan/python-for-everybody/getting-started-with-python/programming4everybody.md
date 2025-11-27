> The Open Michigan materials are available at [www.py4e.com](https://www.py4e.com/)

# Hardware overview 

## Definitions
- **CPU** (*Central Processing Unit*): Runs the program - the CPU is always wondering "what to do next" 
- **Input devices**
- **Output devices**
- **Main memory**:Fast small temporary storage - los on reboot
- **Secondary memory**: Slower large permanent storage - lasts until deleted

# Elements of Python

![](/media/2025-10-26-19-09-05.png)

![](/media/2025-10-26-19-10-13.png)

![](/media/2025-10-26-19-12-42.png)

![](/media/2025-10-26-19-12-55.png)


# Module 4

> Parâmetros da função `print()` em Python

A função `print()` é mais poderosa do que parece! Ela aceita vários parâmetros opcionais que controlam como a saída é formatada.

>> Sintaxe completa da função `print()`

```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

Vamos focar nos parâmetros mais comuns: `sep` e `end`.

1. Comportamento padrão do `print()`

Por padrão, `print()` faz duas coisas:
- Adiciona um **espaço** entre múltiplos argumentos (controlado por `sep`)
- Adiciona uma **quebra de linha** no final (controlado por `end`)

Exemplo:
```
print("Hello")
print("World")
```
Saída:
```
Hello
World
```
Cada `print()` está em uma linha diferente porque `end` por padrão é `'\n'` (newline).

2. Parâmetro `end` - Controla o final da linha

O parâmetro `end` define o que é impresso no final. Por padrão, é `'\n'` (quebra de linha).

Exemplo 1: Usando `end=""` para imprimir na mesma linha
```
for i in range(1, 6):
    print(i, end="")
```
Saída:
```
12345
```
Todos os números são impressos lado a lado, sem quebras de linha.

Exemplo 2: Usando `end=" "` para separar com espaço
```
for i in range(1, 6):
    print(i, end=" ")
```

Saída:
```
1 2 3 4 5 
```

Exemplo 3: Usando `end=", "` para separar com vírgula
```
print("Maçã", end=", ")
print("Banana", end=", ")
print("Laranja")
```

Saída:
```
Maçã, Banana, Laranja
```

3. Parâmetro `sep` - Controla o separador entre múltiplos argumentos

O parâmetro `sep` define o que é impresso entre os argumentos. Por padrão, é `' '` (espaço).

Exemplo 1: Comportamento padrão (`sep=' '`)
```
print("Python", "é", "incrível")
```

Saída:
```
Python é incrível
```

Exemplo 2: Usando `sep="-"`
```
print("2025", "11", "11", sep="-")
```

Saída:
```
2025-11-11
```

Exemplo 3: Usando `sep=""` (sem separador)
```
print("1", "2", "3", "4", "5", sep="")
```
Saída:
```
12345
```

4. Combinando `sep` e `end`

Você pode usar ambos os parâmetros juntos:
```
for i in range(1, 4):
    print("Item", i, sep=": ", end=" | ")
```

Saída:
```
Item: 1 | Item: 2 | Item: 3 | 
```

![](/media/2025-10-26-19-33-18.png)

![](/media/2025-10-26-19-35-28.png)

![](/media/2025-10-26-19-37-21.png)

![](/media/2025-10-26-19-44-58.png)

![](/media/2025-10-26-21-12-05.png)

![](/media/2025-10-26-21-15-02.png)

![](/media/2025-10-26-21-15-17.png)

![](/media/2025-10-27-11-53-07.png)

![](/media/2025-10-27-11-53-58.png)

![](/media/2025-10-27-11-58-44.png)

![](/media/2025-10-27-12-00-33.png)

![](/media/2025-10-27-12-01-47.png)

![](/media/2025-10-27-12-04-09.png)

![](/media/2025-10-27-12-06-26.png)

![](/media/2025-10-27-12-08-42.png)

![](/media/2025-10-27-12-13-50.png)

# Module 5

![](/media/2025-10-27-19-18-36.png)

Entendo a diferença entre if, elif e múltiplos if em Python

> Conceito Fundamental

Quando você escreve código com condições, o comportamento é diferente dependendo de como estrutura seus testes:

>> 1. Múltiplos `if` (sem return ou break)

Quando você usa vários `if` independentes, todas as condições são testadas, e múltiplos blocos podem ser executados:

```
def test_multiple_if(valor):
    if valor > 5:
        print("Primeira condicao: maior que 5")
    if valor > 0:
        print("Segunda condicao: maior que 0")
    if valor < 10:
        print("Terceira condicao: menor que 10")
    print("Fim da funcao")

# Se chamarmos com 7:
test_multiple_if(7)
# Saida:
# Primeira condicao: maior que 5
# Segunda condicao: maior que 0
# Terceira condicao: menor que 10
# Fim da funcao
```

**Observe**: As três mensagens foram impressas porque nenhuma condição "bloqueia" as próximas.

>> 2. Usando `if/elif/else` (cadeia mutuamente exclusiva)

Quando você usa `elif`, **apenas o primeiro bloco com condição verdadeira é executado**. Os demais não são sequer testados:

```
def test_if_elif(valor):
    if valor > 10:
        print("Categoria A: maior que 10")
    elif valor > 5:
        print("Categoria B: entre 5 e 10")
    elif valor > 0:
        print("Categoria C: entre 0 e 5")
    else:
        print("Categoria D: 0 ou negativo")
    print("Fim da funcao")

# Se chamarmos com 7:
test_if_elif(7)
# Saida:
# Categoria B: entre 5 e 10
# Fim da funcao
```

**Observe**: Apenas a condição elif valor > 5 foi executada, mesmo que elif valor > 0 também fosse verdadeira

>> 3. Usando `if` com `return`

Quando você usa `return` dentro de um bloco `if`, a função termina ali e nada depois é executado:

```
def test_if_return(valor):
    if valor > 10:
        print("Maior que 10")
        return "A"
    if valor > 5:
        print("Entre 5 e 10")
        return "B"
    if valor > 0:
        print("Entre 0 e 5")
        return "C"
    print("0 ou negativo
```

![](/media/2025-10-27-19-21-16.png)

![](/media/2025-10-27-19-33-58.png)

![](/media/2025-10-29-17-46-49.png)

![](/media/2025-10-29-17-49-43.png)

![](/media/2025-10-31-15-41-56.png)

![](/media/2025-10-31-15-44-26.png)

# Module 6

![](/media/2025-11-01-13-17-43.png)

![](/media/2025-11-01-13-17-46.png)

![](/media/2025-11-01-13-18-59.png)

![](/media/2025-11-01-13-23-00.png)

![](/media/2025-11-01-15-51-29.png)

![](/media/2025-11-01-15-53-25.png)

![](/media/2025-11-01-15-57-13.png)

![](/media/2025-11-01-15-58-42.png)

![](/media/2025-11-01-16-01-00.png)

![](/media/2025-11-01-16-02-38.png)

> Ao criar funções que verificam condições e retornam `True` ou `False`, você pode usar expressões lógicas diretamente para tornar o código mais limpo e legível.

```
# Forma tradicional

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

```

> Exemplo simplificado

```
# Forma pythonica e simples

def is_adult(age):
    return age >= 18
```

# Module 7

![](/media/2025-11-01-17-05-15.png)

![](/media/2025-11-01-17-14-11.png)

![](/media/2025-11-01-17-16-31.png)

![](/media/2025-11-02-19-25-11.png)

![](/media/2025-11-02-19-28-10.png)

![](/media/2025-11-02-19-29-11.png)

![](/media/2025-11-02-21-10-12.png)

![](/media/2025-11-02-21-15-03.png)

![](/media/2025-11-02-21-18-26.png)

![](/media/2025-11-02-21-20-47.png)

![](/media/2025-11-02-21-22-43.png)

![](/media/2025-11-02-21-24-37.png)

![](/media/2025-11-02-21-25-45.png)

![](/media/2025-11-02-21-37-11.png)

![](/media/2025-11-02-21-39-18.png)

