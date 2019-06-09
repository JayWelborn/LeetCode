/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let possibilities = new Array(nums.length).fill(false);
    possibilities[0] = true;
    for (let i = 0; i < nums.length; i++) {
        if (possibilities[i]) {
            for (let j = 1; j <= nums[i]; j++) {
                if (i + j < nums.length) {
                    possibilities[i + j] = true
                }
            }
        }
    }
    return possibilities[possibilities.length - 1]
};
