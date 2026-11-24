class Solution {
    public String longestCommonPrefix(String[] strs) {
        // It's common prefix, so we can use the shortest word and capture the char
        // Then we use the char to see if every word agree to that

        // Naive solution would be to iterate through every char of the shortest word
        // and then iterate all other words and see if they match, if not match then we stop

        // Other solution would be to combine them all to be one long string 
        // for example dance dag danger becomes dddaaangn
        // everytime we hit char that occur less than count of words, we exit

        // Both need shortest word, so lets find it first
        String shortest = strs[0];
        int shortestInt = shortest.length();
        
        for (var str : strs) {
            if (shortestInt > str.length()){
                shortest = str;
                shortestInt = str.length();
            }
        }

        // Now that we've got the shortest we can iterate once more
        String result = "";

        for (int i = 0; i < shortest.length(); i++){
            char c = shortest.charAt(i);
            for (var str: strs){
                if (str.charAt(i) != c) return result;
            }

            result += c;
        }


        return result;
    }
}