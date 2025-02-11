def one_edit_away(first: str, second: str) -> bool:
    found_dif = False
    i, j = 0, 0

    if len(first) == len(second):
        while i < len(first):
            if first[i] != second[i]:
                if found_dif:
                    return False
                found_dif = True
            i += 1
        return True
    
    elif abs(len(first) - len(second)) == 1:
        while i < len(first) and j < len(second):
            if first[i] != second[j]:
                if found_dif:
                    return False
                found_dif = True

                if len(first) > len(second):
                    i += 1
                else:
                    j += 1
            else:
                i += 1
                j += 1
        return True

    else:
        return False

print(one_edit_away("pale", "ple"))