class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = max_left_index = 0
        right = max_right_index = len(height) - 1
        max_left_value = height[left]
        max_right_value = height[-1]
        biggest_area = right*min(max_left_value, max_right_value)
        for i in range(len(height) - 2):
            if max_left_value <= max_right_value:
                left += 1
                if height[left] > max_left_value:
                    max_left_value = height[left]
                    max_left_index = left
            else:
                right -= 1
                if height[right] > max_right_value:
                    max_right_value = height[right]
                    max_right_index = right
            area = (max_right_index - max_left_index)*min(max_left_value, max_right_value)
            if area > biggest_area:
                biggest_area = area
        return biggest_area