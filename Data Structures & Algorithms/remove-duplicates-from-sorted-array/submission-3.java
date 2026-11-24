class Solution {
    public int removeDuplicates(int[] nums) {
        // To remove duplicates in a non descending sorted array, we can just compare curent with previous
        // if same, we remove
        // The problem will be to do it in place (O(1) space complexity)
        // We can swap in place to the nums[uniqueCount] if we find out that our current is unique

        int last = nums[0];
        int uniqueCount = 1;
        
        for (int i = 1; i < nums.length; i++){
            if (last < nums[i]){
                last = nums[i];
                
                // We should also swap nums[uniqueCount] to current, to ensure the right order
                nums[uniqueCount] = last;
                uniqueCount+=1;
            }
        }
        
        return uniqueCount;
    }
}