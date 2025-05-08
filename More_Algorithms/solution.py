from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Grafo: curso → lista de cursos dependentes
        graph = defaultdict(list)
        # In-degree: número de pré-requisitos de cada curso
        in_degree = [0] * numCourses

        # Constrói o grafo e in-degree
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Inicializa fila com cursos sem pré-requisitos
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Se a ordem contém todos os cursos, é válida
        return order if len(order) == numCourses else []
