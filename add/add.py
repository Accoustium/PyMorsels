def add(*matrices):
    # If only one matrix return itself.
    if len(matrices) == 1:
        return matrices[0]

    # Gather the size of first matrix
    size = []
    for col in range(len(matrices[0])):
        size.append(len(matrices[0][col]))

    # Cycle through all available matrices adding
    value = []
    for matrix in matrices:
        # Validate matrix is valid size
        test_size = []
        for col in range(len(matrix)):
            test_size.append(len(matrix[col]))
        if test_size != size:
            raise ValueError("Given matrices are not the same size.")

        # If first value
        if value == []:
            for col in range(len(matrix)):
                value.append([x for x in matrix[col]])

        # if not first value
        else:
            for col in range(len(matrix)):
                for row in range(len(matrix[col])):
                    value[col][row] += matrix[col][row]

    return value
