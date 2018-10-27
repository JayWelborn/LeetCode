char* reverseString(char* s) {
    char *rev = malloc(sizeof(char) * (strlen(s) + 1));
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        rev[i] = s[len - i - 1];
    }
    rev[len] = '\0';
    return rev;
}
