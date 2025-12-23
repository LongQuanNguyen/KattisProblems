def main():
    trophies, properties = list(map(int, input().split()))
    properties_matrix = [[None for _ in range(trophies)] for _ in range(properties)]
    trend_matrix = [[None for _ in range(trophies)] for _ in range(properties)]

    uniqueness = [True] * properties
    for i in range(trophies):
        a_tr_properties = list(map(int, input().split()))
        #print(a_tr_properties)
        for j, property in enumerate(a_tr_properties):
            if property in properties_matrix[j]:
                uniqueness[j] = False
            properties_matrix[j][i] = property

            if i > 0:
                if property > properties_matrix[j][i-1]:
                    trend_matrix[j][i] = True
                if property < properties_matrix[j][i-1]:
                    trend_matrix[j][i] = False

    unique_trend_matrix = []
    for i in range(len(uniqueness)):
        if uniqueness[i]:
            unique_trend_matrix.append(tuple(trend_matrix[i]))

    print(len(set(unique_trend_matrix)))

if __name__ == "__main__":
    main()