def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of n rows."""
    if n <= 0:
        return []
    
    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]
    
    # Generate rows from the 2nd to the nth row
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1
        
        # Fill in the middle values
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    
    return triangle
