int hammingWeight(uint32_t n) {
    int ones = 0;
    for (int i = 0; i < 32; i++) {
        ones += (n >> i) & 0x0001;
    }
    return ones;
}
