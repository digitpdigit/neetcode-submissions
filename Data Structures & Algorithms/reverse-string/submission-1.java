class Solution {
    public void reverseString(char[] s) {
        // We can use two pointers starting from right and left
        // And when pointer match or surpass each other we break
        int l = 0;
        int r = s.length - 1;

        while (l < r) {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;

            l++;
            r--;
        }
        
    }
}