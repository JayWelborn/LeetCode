class Solution:

    @staticmethod
    def brute_force(height: List[int]) ->int:
      max_area = 0
      for index_one, item_one in enumerate(height):
          for index_two, item_two in enumerate(height):
              bucket_height = min(item_one, item_two)
              bucket_width = abs(index_one - index_two)
              max_area = max(max_area, bucket_height * bucket_width)
        
      return max_area

    @staticmethod
    def two_pointer(height: List[int]) -> int:
      left, right = 0, len(height) - 1
      max_area = 0
      while right >= left:
        bucket_width = right - left
        bucket_height = min(height[left], height[right])
        max_area = max(max_area, bucket_width * bucket_height)

        if height[left] > height[right]:
          right -= 1
        else:
          left += 1

      return max_area

    def maxArea(self, height: List[int]) -> int:
      return self.two_pointer(height)
