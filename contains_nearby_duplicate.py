"""
Referente ao problema nesse primeiro caso temos 2 loops e issso gera um
Time Complexxity de O(n^2)
Já o Space Complexity de O(1) pois não estamos utilizando nenhuma estrutura de dados adicional
além das variáveis de controle dos loops.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums[i] == nums[j]
        # abs(i - j) <= k

        for i in range(len(nums)): # O(n)
            for j in range(i +1, len(nums)): # O(n)
                if nums [i] == nums[j] and abs(i -j) <= k:
                    return True
        return False
    
"""
Refente ao problema nesse segundo caso temos 1 loop e isso gera um
Time Complexity de O(n)
Já o Space Complexity de O(n) pois estamos utilizando um dicionário para armazenar os
índices dos números vistos até o momento.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i
        return False
    
    ### [1, 2, 3, 1], k = 3
    ### {1: 0}
    ### {1: 0, 2: 1}
    ### {1: 0, 2: 1, 3: 2}