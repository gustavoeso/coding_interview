class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        start = 0
        parts = []

        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            # Quando encontramos uma substring especial
            if count == 0:
                # Recursivamente processa a parte interna (sem os extremos)
                inner = self.makeLargestSpecial(s[start + 1:i])
                # Adiciona a parte completa (com 1 e 0 nas extremidades)
                parts.append('1' + inner + '0')
                start = i + 1

        # Ordena as partes em ordem lexicográfica decrescente
        parts.sort(reverse=True)
        return ''.join(parts)
