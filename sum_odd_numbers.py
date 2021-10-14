def row_sum_odd_numbers(n):
    if n > 1:
        len_s1 = (n * (n+1)) / 2
        len_s2 = ((n-1) * n) / 2
        s1 = ((2 + (len_s1 - 1) * 2) * len_s1) / 2
        s2 = ((2 + (len_s2 - 1) * 2) * len_s2) / 2
        return s1 - s2
    else:
        return 1


print(int(row_sum_odd_numbers(3)))
