def print_indices_and_elements(elements) -> None:
    for i, element in enumerate(elements):
        print(i, element)


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [num for num in range(start, end + 1) if num % 2 == 0]


def get_char_set_from(s: str) -> set[str]:
    return {char for char in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {num: int(num ** 0.5) for num in range(start, end + 1) if (num ** 0.5).is_integer()}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1

def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [num if num % 2 == 0 else -1 for num in numbers if num % 5 == 0]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(s) for s in strings]


def get_fibonacci_type(version: int) -> str:
    return "generator" if version == 1 else "list"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return ("fibonacci1 é um generator porque usa yield, gerando os valores sob demanda e economizando memória. "
            "Já fibonacci2 retorna uma lista, armazenando todos os valores de uma vez, o que ocupa mais memória, "
            "mas permite acessar os elementos diretamente e reutilizar a sequência.")


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.elements):
            raise StopIteration
        value = self.elements[self.index]
        self.index += 2
        return value


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return (e1 + e2 + sum(others)) / (2 + len(others))


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    
    # Criando c com **a, **b (mantém os valores de b quando há conflito)
    c1 = {**a, **b}
    
    # Criando c com **b, **a (mantém os valores de a quando há conflito)
    c2 = {**b, **a}
    
    # Encontrando as chaves que têm valores diferentes nas duas versões de c
    return sorted([k for k in c1 if k in c2 and c1[k] != c2[k]])


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        first, *middle, last = numbers
        print(first, last)
        numbers = middle
    if numbers:
        print(numbers[0])


def append_range(start: int, end: int, step: int=1, to: list[int]=None):
    # You may add code here
    if to is None:
        to = []
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None
