class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Caso base: primeira linha, primeiro símbolo
        if n == 1 and k == 1:
            return 0
        
        # Determina o "pai" do k-ésimo símbolo
        parent = (k + 1) // 2
        
        # Chamada recursiva para descobrir o valor do pai
        parent_val = self.kthGrammar(n - 1, parent)
        
        # Verifica se k é par (filho direito) ou ímpar (filho esquerdo)
        if k % 2 == 1:
            return parent_val
        else:
            return 1 - parent_val
