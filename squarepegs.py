def main():
    inp = input()
    num_plot, num_cir_h, num_sq_h = list(map(int, inp.split()))

    plot_r = input().split()
    plot_r = (list(map(int, plot_r)))
    plot_r.sort(reverse=True)
    #print(plot_r)

    cir_h = input().split()
    cir_h = list(map(int, cir_h))

    sq_h = input().split()
    sq_h = list(map(lambda x: x/(2**(1/2)), map(int, sq_h)))

    house = cir_h + sq_h
    house.sort(reverse=True)
    #print(house)

    filled_plot = 0
    h_index = 0
    for plot in plot_r:
        while (h_index < (num_cir_h + num_sq_h)):
            #print(h_index, plot, house[h_index], filled_plot)
            if house[h_index] >= plot:
                h_index += 1
            else:
                filled_plot += 1
                h_index += 1
                break

    print(filled_plot)


if __name__ == '__main__':
    main()