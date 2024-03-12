def get_all_left_top(canvas, h, w):
    all_left_top_coord = []
    for row in range(h-1):
        for col in range(w-1):
            if canvas[row][col] == '+' and canvas[row+1][col] == '+' and canvas[row][col+1] == '+':
                all_left_top_coord.append((row, col))
    return all_left_top_coord


def get_full_coords(canvas, h, w, start_search_row, start_search_col):
    start_row = -1
    start_col = -1
    for row in range(start_search_row, h):
        for col in range(start_search_col, w):
            if canvas[row][col] == '+':
                start_row, start_col = row, col
            break
        if start_row != -1:
            break

    end_row = start_row - 1
    for row in canvas[start_row:]:
        if row[start_col] != '+':
            break
        end_row += 1

    end_col = start_col - 1
    for i in range(start_col, w):
        if canvas[start_row][i] != '+':
            break
        end_col += 1

    return start_row, start_col, end_row, end_col


def has_inner_image(canvas, coord):
    for row in range(coord[0]+2, coord[2]-1):
        for col in range(coord[1]+2, coord[3]-1):
            if canvas[row][col] == '+':
                return True
    return False


def has_ads(canvas, coord, allow_list):
    for row in range(coord[0] + 1, coord[2]):
        for col in range(coord[1] + 1, coord[3]):
            if ord(canvas[row][col]) not in allow_list:
                return True
    return False


def blank_replace(canvas, coord):
    for row in range(coord[0], coord[2] + 1):
        for col in range(coord[1], coord[3] + 1):
            canvas[row][col] = ' '


def main():
    allow_list = [32, 33, 43, 44, 46, 63]
    allow_list += list(range(48, 58))
    allow_list += list(range(65, 91))
    allow_list += list(range(97, 123))

    height, width = list(map(int, input().split()))
    canvas = []
    for i in range(height):
        canvas.append(list(input()))

    img_coord_list = []

    all_left_top_coords = get_all_left_top(canvas, height, width)
    for i in all_left_top_coords:
        img_coord_list.append(get_full_coords(canvas, height, width, i[0], i[1]))

    for coord in img_coord_list:
        if has_inner_image(canvas, coord):
            img_coord_list.append(get_full_coords(canvas, height, width, coord[0]+2, coord[1]+2))

    img_coord_list.reverse()
    for coords in img_coord_list:
        if has_ads(canvas, coords, allow_list):
            blank_replace(canvas, coords)

    for row in canvas:
        print(''.join(row))


if __name__ == '__main__':
    main()
