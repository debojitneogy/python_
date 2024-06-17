def longest_(*words):
    max_ = max(words);
    max_len = len(max_);
    return max_,max_len;

print(longest_("abc","abcd","ab","a"));