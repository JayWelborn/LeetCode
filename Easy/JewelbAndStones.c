int numJewelsInStones(char* J, char* S) {
    int count = 0;
    while (*S != '\0') {
        char *j = J;
        while (*j != 0) {
            if (*j == *S) {
                count++;
            }
            j++;
        }
        S++;
    }
    return count;
}

