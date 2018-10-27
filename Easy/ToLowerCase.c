char* toLowerCase(char* str) {
    char *curr = str;
    while (*curr != '\0') {
        if (*curr >= 'A' && *curr <= 'Z') {
            *curr += 0x20;
        }
        curr++;
    }
    return str;
}
