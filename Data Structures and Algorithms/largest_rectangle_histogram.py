
def largestRectangleArea(heights):
    stack = []
    maxArea = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1]>h :
            """
            if we cannot extend the rectangle horizontally, we pop the last item in the stack 
            and calculate the area of it, if it is the max thus far,it will be assigned to the maxArea. 
            After that, because we can extend backwards, we reassign start to index.
            """
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i-index)) 
            start = index
        stack.append((start,h))

    for i,h in stack:
        """
        if there are still items in stack, calculate the area of it and if it is the max reassign the maxArea
        """
        maxArea = max(maxArea,(len(heights)-i)*h)
    
    return maxArea
