class Stack:
    def __init__(self):
        # Your subclass must not access this attribute
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


class StackWithMin(Stack):
    def __init__(self):
        super().__init__()
        self._min_stack = []  # Pilha auxiliar para armazenar os mínimos

    def push(self, value):
        # Insere o valor na pilha original
        super().push(value)

        # Insere o valor na pilha auxiliar se for menor ou igual ao topo dela
        if not self._min_stack or value <= self._min_stack[-1]:
            self._min_stack.append(value)

    def pop(self):
        # Remove o valor da pilha original
        value = super().pop()

        # Se o valor removido for igual ao topo da pilha de mínimos, remove de lá também
        if value == self._min_stack[-1]:
            self._min_stack.pop()

        return value

    def minimum(self):
        # Retorna o mínimo atual da pilha em O(1), se a pilha não estiver vazia
        if not self._min_stack:
            return float('inf')
        return self._min_stack[-1]