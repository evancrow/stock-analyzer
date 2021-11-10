def equalArrayLengths(arrays):
    maximumDataLength = len(arrays[0])

    # find the array with the least amount of data
    for array in arrays:
        if len(array) < maximumDataLength:
            maximumDataLength = len(array)

    # make sure no stocks exceed the maximum length
    for i in range(len(arrays)):
        data = []

        for ii in range(len(arrays[i])):
            if ii < maximumDataLength:
                data.append(arrays[i][ii])

        arrays[i] = data

    return arrays