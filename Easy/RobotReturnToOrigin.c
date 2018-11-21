bool judgeCircle(char* moves) {
    int r= 0, l = 0, u = 0, d = 0;
    char c;
    while(*moves) {
        c = *moves;
        l += (c == 'L');
        r += (c == 'R');
        u += (c == 'U');
        d += (c == 'D');
        moves++;
    }
    return l == r && u == d;
}
