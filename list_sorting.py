def bubble_sort(lis_):
    n = len(lis_);
    for i in range(n-1):
        for j in range(n-i-1):
            if lis_[j] > lis_[j+1]:
                lis_[j],lis_[j+1] = lis_[j+1],lis_[j];
    return lis_;
