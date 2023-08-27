
def rotate(matrix):
    l,r = 0, len(matrix)-1

    while l<r:
        top,bottom = l,r
        for i in range(r-l):
            temp = matrix[top][l+i]
            matrix[top][l+i] = matrix[bottom-i][l]
            matrix[bottom-i][l] = matrix[bottom][r-i]
            matrix[bottom][r-i] = matrix[top+i][r]
            matrix[top+i][r] = temp
        l += 1
        r -= 1
