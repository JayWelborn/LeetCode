void inPlaceRecursiveReverse(char *s, int start, int end) {
    if (end <= start)
        return;
    s[start] = s[start] ^ s[end];
    s[end] = s[start] ^ s[end];
    s[start] = s[start] ^ s[end];
    inPlaceRecursiveReverse(s, start + 1, end - 1);
}

char* reverseString(char* s, int sSize) {
    inPlaceRecursiveReverse(s, 0, sSize - 1);
    return s;
}
