class Solution {
    public int removeElement(int[] nums, int val) {
        // Edge cases where nums.length = 1 and nums[i] == val
        if (nums.length == 1 && nums[0] == val){
            return 0;
        }

        // Edge cases where nums is empty
        if (nums.length == 0) {
            return 0;
        }

        // We shoul always push the val items to the end.
        // But we need to also track which right pointer that still valid to be swapped with
        // So lets do two pointer
        // L always moves to the right
        // R only moves to the left if its invalid to be swapped
        // Loop ends when l touch r

        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            // Check if l is val, then swap with r if r is valid
            if (nums[l] == val){

                // If r valid
                if (nums[r] != val) {
                    int temp = nums[l];
                    nums[l] = nums[r];
                    nums[r] = temp;

                    // We move r since r current cannot be valid
                    r--;
                } 
                // If r is invalid we move r down but dont increment l
                else {
                    r--;
                    continue;
                }
            }

            l++;
        }

        return r+1;
    }
}