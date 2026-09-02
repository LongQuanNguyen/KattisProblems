MAX_TIME = 10**7

def distance(x_1, y_1, x_2, y_2):
    return ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5


def speed(d, t):
    return float(d) / t


def time_at_distance(x, cum_dist, cum_time):
    for i in range(1, len(cum_dist)):
        if x <= cum_dist[i]:
            d1, d2 = cum_dist[i - 1], cum_dist[i]
            t1, t2 = cum_time[i - 1], cum_time[i]

            seg_speed = speed(d2 - d1, t2 - t1)

            return t1 + (x - d1) / seg_speed
    return MAX_TIME


def main():
    n = int(input())
    cum_dist = [0.0]
    cum_time = [0.0]
    prev_x, prev_y, prev_d, = 0, 0, 0
    for _ in range(n):
        x, y, t = map(float, input().split())
        prev_d += distance(x, y, prev_x, prev_y)
        cum_dist.append(prev_d)
        cum_time.append(t)
        prev_x, prev_y = x, y

    best = MAX_TIME
    for d in cum_dist:
        best = min(best, time_at_distance(d + 100, cum_dist, cum_time) - time_at_distance(d, cum_dist, cum_time))
        if d >= 100:
            best = min(best, time_at_distance(d, cum_dist, cum_time) - time_at_distance(d - 100, cum_dist, cum_time))

    print(best)


if __name__ == "__main__":
    main()