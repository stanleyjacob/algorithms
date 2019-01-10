# returns the largest overlap rectangle
def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(heights)):
            start_index = i
            start_value = heights[i]
            width = 1
            
            currentArea = start_value * width
            if currentArea > maxArea:
                maxArea = currentArea
            
            left_index = i
            left_value = start_value
            right_index = i
            right_value = start_value
            left_done = False
            right_done = False
            while True:
                    
                if left_index > 0:
                    left_index -= 1
                    left_value = heights[left_index]
                else:
                    left_done = True
                    
                if right_index < (len(heights) - 1):
                    right_index += 1
                    right_value = heights[right_index]
                else:
                    right_done = True
                
                if not left_done:
                    if left_value >= start_value:
                        width += 1
                    else:
                        left_done = True
                
                if not right_done:
                    if right_value >= start_value:
                        width += 1
                    else:
                        right_done = True
                
                currentArea = start_value * width
                
                if currentArea > maxArea:
                    maxArea = currentArea
                    #print('{0:3d} {1:3d}'.format(start_value, width))
                
                if left_done and right_done:
                    break
        return maxArea
