from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = deque(), [0]*len(temperatures)
        
        # We're going to go through our temperature list, and maintain a set of
        # indices in a stack representing decreasing temps
        for i in range(len(temperatures)):
            # If we don't have a stack, or the last temp appended to the stack is warmer than
            # the current one, add the index to the stack
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
                
            else:
                # for each temp in the stack the current temp is warmer than, the current temp
                # is the next warmer temp, so the diff between the stored index and current is
                # the output for the stored index
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    prev = stack.pop()
                    output[prev] = i - prev
                stack.append(i)
            
        return output
