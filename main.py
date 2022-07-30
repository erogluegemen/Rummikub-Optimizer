total = 0
total_per = [[3, 4, 5], [2, 2, 2]]

# kullanıcı elinin çift mi normal mi gittiği inputunu girmeli mi?


def check_per(per: list):
    min_len_per = 3

    # 1st way: (same-colored tiles, in sequential order)
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
    min_len_per = 3

    # 2nd way: (same-value tiles in distinct colors)
    if len(per) < min_len_per:
        return False

    if len(set(per)) != 1:  # set cannot have duplicates. so len must be equal to 1.
        return False
    return True


per = [4, 5, 6]
per_2 = [5, 5, 5]

if not check_per(per):  # if not sequential per try other one
    if not check_double_per(per):  # if not per return false
        per_count = 5  # koşul olarak bunu ekle
        print(False)
    else:
        total_per.append(per)  # else append per to per list
        print(total_per)
else:
    total_per.append(per)  # else append per to per list
    print(total_per)


def calculate():
    global total
    for idx, per in enumerate(total_per):
        total = total + (sum(total_per[idx]))
    if total >= 101:
        print(f'El açar.\nGüncel puan: {total}')

    else:
        print(f'El açmaz.\nGüncel puan: {total}\nAçmak için gerekli olan puan: {101-total}')


calculate()
