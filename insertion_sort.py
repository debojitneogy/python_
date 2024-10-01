def insertion_sort(li):
    n = len(li);

    for i in range(1,n):
        j = i-1;
        key = li[i];
        while (j >= 0) and (li[j] > key):
            li[j+1] = li[j];
            j -= 1;

        li[j+1] = key;
    return li;

print(insertion_sort([11, 13, 12, 16, 12]));