MAX_TIME = 10**7

def distance(x_1, y_1, x_2, y_2):
    return ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5


def speed(d, t):
    return float(d) / t

def interpolate_time_at_distance_x(x, idx, cum_dist, cum_time):
    d1, d2 = cum_dist[idx], cum_dist[idx + 1]
    t1, t2 = cum_time[idx], cum_time[idx + 1]
    seg_speed = (d2 - d1) / (t2 - t1)
    return t1 + (x - d1) / seg_speed


def best_100m_start_at_reading(cum_dist, cum_time):
    right = 0
    best = MAX_TIME
    length = len(cum_dist)

    for left in range(length):
        if right < left:
            right = left

        target = cum_dist[left] + 100

        while right < length and cum_dist[right] < target:
            right += 1

        if right == length:
            break

        time_at_target = interpolate_time_at_distance_x(target, right - 1, cum_dist, cum_time)
        window_time = time_at_target - cum_time[left]
        best = min(window_time, best)

    return best


def best_100m_end_at_reading(cum_dist, cum_time):
    left = 0
    best = MAX_TIME
    length = len(cum_dist)

    for right in range(length):
        target = cum_dist[right] - 100
        if target < 0:
            continue
        while cum_dist[left] < target:
            left += 1

        if target == cum_dist[left]:
            time_at_target = cum_time[left]
        else:
            time_at_target = interpolate_time_at_distance_x(target, left - 1 , cum_dist, cum_time)
        window_time = cum_time[right] - time_at_target
        best = min(window_time, best)

    return best


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

    print(min(best_100m_start_at_reading(cum_dist, cum_time), best_100m_end_at_reading(cum_dist, cum_time)))


if __name__ == "__main__":
    main()