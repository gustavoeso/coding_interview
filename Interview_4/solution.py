class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    if node is None:
        return None

    # Caso 1: se tem uma subárvore à direita, desce nela e pega o nó mais à esquerda
    if node.right:
        ref = node.right
        while ref.left:
            ref = ref.left
        return ref

    # Caso 2: Não existe subárvore à direita, então subir na árvore até encontrar um nó que seja filho à esquerda
    atual = node
    pai = node.parent
    while pai and pai.right == atual:
        atual = pai
        pai = pai.parent
    return pai
