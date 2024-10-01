def selection_sort(li):
    n = len(li);
    for i in range(n):
        for j in range(i+1,n):
            if li[j] < li[i]:
                li[i],li[j] = li[j],li[i];
                break;
    return li;

print(selection_sort([11, 13, 12, 16, 12]));