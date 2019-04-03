class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        int result = 0;
        while (n != 0) {
            result += (n & 1);
            n >>= 1;
        }
        return (result == 1);
    }
}
