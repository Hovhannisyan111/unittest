def is_sorted(ml):
    if ml == sorted(ml):
        return True
    return False

def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False
    
def merge_sorted_lists(ml1, ml2):
    tmp = []
    i, j = 0, 0
    while i < len(ml1) and j < len(ml2):
        if ml1[i] < ml2[j]:
            tmp.append(ml1[i])
            i += 1
        else:
            tmp.append(ml2[j])
            j += 1
    if i < len(ml1):
        tmp.extend(ml1[i:])
    if j < len(ml2):
        tmp.extend(ml2[j:])
    return tmp

def main():
    ml = [1,2,3,4]
    #print(is_sorted(ml))
    str1 = "tuk"
    str2 = "kut"
    #print(are_anagrams(str1, str2))
    ml1 = [1,3,5,7]
    ml2 = [2,4,6]
    print(merge_sorted_lists(ml1, ml2))


if __name__ == "__main__":
    main()
