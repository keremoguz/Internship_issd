
def rotate(matrix):
    """
    it rotates from the outermost layer to the innermost layer.
    """
    l,r = 0, len(matrix)-1

    while l<r:
        """
        iterates until left and right meet.
        """
        top,bottom = l,r
        for i in range(r-l):
            temp = matrix[top][l+i] # keeps the top left value in temp variable to assign to the top right
            matrix[top][l+i] = matrix[bottom-i][l] # changes bottom left to the top left
            matrix[bottom-i][l] = matrix[bottom][r-i] # changes bottom right to the bottom left
            matrix[bottom][r-i] = matrix[top+i][r] # changes top right to the bottom right
            matrix[top+i][r] = temp # lastly assigns temp to the top right.
        
        l += 1; r-=1 # allows switching to 1 lower layer
