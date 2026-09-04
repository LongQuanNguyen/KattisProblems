UNALLOCATED = 0
REQUESTED = 1
CONTESTED = 2

def inspect_matrix(matrix):
    for row in matrix:
        print(row)


def area(x_sw, y_sw, x_ne, y_ne):
    return abs((x_ne-x_sw)*(y_ne-y_sw))


def employee_guarantee_area(contested_matrix, employee_rect):
    x_sw, y_sw, x_ne, y_ne = employee_rect
    requested_area = area(x_sw, y_sw, x_ne, y_ne)

    for x in range(x_sw, x_ne):
        for y in range(y_sw, y_ne):
            if contested_matrix[x][y] == CONTESTED:
                requested_area -= 1
    return requested_area


def set_contested_area(matrix, contested_coords):
    x_sw, y_sw, x_ne, y_ne = contested_coords
    for x in range(x_sw, x_ne):
        for y in range(y_sw, y_ne):
            if matrix[x][y] == REQUESTED:
                matrix[x][y] = CONTESTED


def set_requested_area(matrix, requested_coord):
    x_sw, y_sw, x_ne, y_ne = requested_coord
    for x in range(x_sw, x_ne):
        for y in range(y_sw, y_ne):
            if matrix[x][y] == UNALLOCATED:
                matrix[x][y] = REQUESTED


def get_contested_coords(rect1, rect2):
    x1_sw, y1_sw, x1_ne, y1_ne = rect1
    x2_sw, y2_sw, x2_ne, y2_ne = rect2

    sw_overlap = max(x1_sw, x2_sw), max(y1_sw, y2_sw)
    ne_overlap = min(x1_ne, x2_ne), min(y1_ne, y2_ne)

    if sw_overlap[0] >= ne_overlap[0] and sw_overlap[1] >= ne_overlap[1]:
        return None
    return sw_overlap[0], sw_overlap[1], ne_overlap[0], ne_overlap[1]


def unallocated_contested_area(matrix, w, h):
    unallocated, contested = 0, 0
    for x in range(w):
        for y in range(h):
            if matrix[x][y] == UNALLOCATED:
                unallocated += 1
            if matrix[x][y] == CONTESTED:
                contested += 1
    return unallocated, contested


def main():
    while True:
        try:
            w, h = map(int, input().split())
            n = int(input())

            floor_matrix = [[ UNALLOCATED for _ in range(h) ] for _ in range(w)]
            requested_area = {}

            for _ in range(n):
                request = input().split()
                employee = request[0]
                x1, y1, x2, y2 = map(int, request[1::])
                requested_area[employee] = x1, y1, x2, y2
                set_requested_area(floor_matrix, (x1, y1, x2, y2))

            keys = list(requested_area)
            for i in range(n):
                for j in range(i + 1, n):
                    employee1 = keys[i]
                    employee2 = keys[j]

                    e1_e2_contested_coords = get_contested_coords(requested_area[employee1], requested_area[employee2])
                    if e1_e2_contested_coords is None:
                        continue
                    else:
                        set_contested_area(floor_matrix, e1_e2_contested_coords)

            #inspect_matrix(floor_matrix)

            print("Total", area(0, 0, w, h))
            unallocated_area, contested_area = unallocated_contested_area(floor_matrix, w, h)
            print("Unallocated", unallocated_area)
            print("Contested", contested_area)
            for employee in keys:
                print(employee, employee_guarantee_area(floor_matrix, requested_area[employee]))
            print()

        except EOFError:
            break
    return None

if __name__ == "__main__":
    main()