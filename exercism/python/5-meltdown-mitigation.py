"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    efficieny = (generated_power / theoretical_max_power) * 100

    if efficieny >= 80:
        return 'green'
    if 60 <= efficieny < 80:
        return 'orange'
    if 30 <= efficieny < 60:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    if temperature * neutrons_produced_per_second < 0.9 * threshold:
        return 'LOW'
    if threshold - 0.1 * threshold <= temperature * neutrons_produced_per_second <= threshold + 0.1 * threshold:
        return 'NORMAL'
    return 'DANGER'


"""
NOTA IMPORTANTE SOBRE IF/ELIF/RETURN:

Neste codigo, usamos if/elif com return. Veja por que isso e importante:

Quando usamos "if" independentes sem return, TODAS as condicoes sao testadas:
    if valor > 5:
        print("teste 1")
    if valor > 0:
        print("teste 2")
    # Ambas sao executadas se ambas forem verdadeiras

Quando usamos "elif", apenas UM bloco e executado (o primeiro verdadeiro):
    if valor > 10:
        return "A"
    elif valor > 5:
        return "B"
    elif valor > 0:
        return "C"
    else:
        return "D"
    # Apenas UM return e alcancado

Por que preferir elif quando ha return?
1. CLAREZA: Deixa explícito que apenas uma categoria sera retornada
2. EFICIENCIA: Python nao testa condicoes desnecessarias apos um return
3. MANUTENCAO: Seu codigo fica mais legivel e facil de debugar

Exemplo do projeto:
    if efficieny >= 80:
        return 'green'
    elif 60 <= efficieny < 80:
        return 'orange'
    elif 30 <= efficieny < 60:
        return 'red'
    return 'black'

Se efficieny = 75, apenas a segunda condicao e executada e 'orange' e retornado.
As outras nao sao sequer testadas!
"""

# ============================================================================
# EXEMPLO PRATICO DE COMO FUNCIONA
# ============================================================================

"""
# Multiplos if (TODAS as condicoes sao testadas):
print("=== Multiplos if ===")


def multiplos_if(x):
    if x > 5:
        print("Passou no primeiro if")
    if x > 0:
        print("Passou no segundo if")
    if x < 10:
        print("Passou no terceiro if")


multiplos_if(7)
# Saida: Todas as tres linhas aparecem porque nenhuma bloqueia as proximas

# if/elif (apenas UM bloco e executado):
print("\n=== If/elif ===")


def if_elif(x):
    if x > 10:
        print("Categoria A")
    elif x > 5:
        print("Categoria B")
    elif x > 0:
        print("Categoria C")
    else:
        print("Categoria D")


if_elif(7)
# Saida: Apenas "Categoria B" apa
"""