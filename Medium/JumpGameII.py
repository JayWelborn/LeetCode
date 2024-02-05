class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps_taken = 0
        furthest_reachable = 0
        current_max = 0

        if len(nums) == 1:
            return 0
        
        for index, num in enumerate(nums):
            current_max = max(current_max, index + num)
            if index == furthest_reachable:
                furthest_reachable = current_max
                jumps_taken += 1
                
            if furthest_reachable >= len(nums) - 1:
                return jumps_taken
                

        return jumps_taken

class NaiveOriginalSolution:
  def jump(self, nums: List[int]) -> int:
        step_cache = {0: 0}
        
        for i, num in enumerate(nums):
            steps_to_index = step_cache[i]
            
            for j in range(1, num + 1):
                reachable_index = i + j
                if reachable_index > len(nums):
                    pass
                elif reachable_index in step_cache:
                    step_cache[reachable_index] = min(step_cache[reachable_index], steps_to_index + 1)
                else:
                    step_cache[reachable_index] = steps_to_index + 1
                

        return step_cache[len(nums) - 1]
