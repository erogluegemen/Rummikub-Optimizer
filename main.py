total = 0
total_per = [[3, 4, 5], [2, 2, 2]]  # for testing


def check_per(per: list):
    min_len_per = 3

    # 1st way: (same-colored tiles, in sequential order / Series)
    if len(per) < min_len_per:
        return False

    min_val = min(per)
    max_val = max(per)

    if max_val - min_val + 1 == len(per):
        for tile in range(len(per)):
            diff = per[tile] - min_val
            if per[tile] > 0:
                per[tile] = per[diff]
            else:
                return False
        return True
    return False


def check_double_per(per: list):
    max_len_per = 2

    # 2nd way: (same-value tiles in distinct colors / double)
    if len(per) < max_len_per or len(per) > max_len_per:
        return False

    else:
        if len(set(per)) != 1:  # set cannot have duplicates. so len must be equal to 1.
            return False
        return True


per = [4, 5, 6]
per_2 = [5, 5, 5]

if not check_per(per):  # if not sequential per try double per
    if not check_double_per(per):  # if not per return false
        print(False)

    else:
        total_per.append(per)  # else append per to per list
        print(total_per)

else:
    total_per.append(per)  # else append per to per list
    print(total_per)


def calculate():
    global total, total_per
    for idx, per in enumerate(total_per):
        total = total + (sum(total_per[idx]))

    if total >= 101:
        print(f'El açar.\nGüncel puan: {total}')

    else:
        print(f'El açmaz.\nGüncel puan: {total}\nAçmak için gerekli olan puan: {101 - total}')


calculate()


