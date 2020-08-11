import numpy as np
def levenshtein_ratio_and_distance(s, t, ratio_calc = True):
    # Convert both to lowercase
    s = s.lower()
    t = t.lower()

    # Initialize matrix of zeros
    rows = len(s)+1
    columns = len(t)+1
    distance = np.zeros((rows,columns),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,columns):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for column in range(1, columns):
        for row in range(1, rows):
            if s[row-1] == t[column-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][column] = min(distance[row-1][column] + 1,      # Cost of deletions
                                 distance[row][column-1] + 1,          # Cost of insertions
                                 distance[row-1][column-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][column]) / (len(s)+len(t))
        return Ratio
        # A 60% match or above will indicate similarity. Anything below is most likely not a match

    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][column])
# x = input("first string: ")
# y = input("second string: ")
# print(levenshtein_ratio_and_distance(x, y, ratio_calc = True))