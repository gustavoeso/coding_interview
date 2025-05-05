from typing import List

def compute_pond_sizes(land: List[List[int]]) -> List[int]:
    if not land:
        return []

    rows, cols = len(land), len(land[0])
    visited = [[False] * cols for _ in range(rows)]
    sizes: List[int] = []

    def explore(r: int, c: int) -> int:
        # Fora da matriz → nada a contar
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        # Já visitado ou não‑água → ignora
        if visited[r][c] or land[r][c] != 0:
            return 0

        visited[r][c] = True        # marca a célula
        size = 1                    # conta a própria célula

        # percorre as 8 direções ao redor
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:              # pula a direção (0,0)
                    size += explore(r + dr, c + dc) # soma o que achar
        return size

    # percorre toda a grade
    for i in range(rows):
        for j in range(cols):
            if land[i][j] == 0 and not visited[i][j]:
                sizes.append(explore(i, j))

    return sizes
