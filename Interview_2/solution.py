class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def nth_to_last(head: Node, k: int) -> Node:
    count = 0
    atual = head

    # Contando o tamanho da lista
    while atual is not None:
        count += 1
        atual = atual.next

    if k > count:
        return None
    
    atual = head
    for _ in range(count - k):
        atual = atual.next

    return atual