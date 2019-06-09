/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let furthest = 0;
    let lastIndex = nums.length - 1;
    for (let i = 0; i <= furthest && furthest <= lastIndex; i++) {
        furthest = Math.max(furthest, i + nums[i]);
        if (furthest >= lastIndex) {
            return true;
        }
    }
    return furthest >= lastIndex;
};
