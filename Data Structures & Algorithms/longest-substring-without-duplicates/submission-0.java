class Solution {
    public int lengthOfLongestSubstring(String s) {
        String[] str = s.split("");
        String longest = "";
        String temp = "";
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < s.length(); ) {
            if (set.contains(str[i])) {
                set.clear();
                if (temp.length() > longest.length()) {
                    longest = temp;
                }
                i -= temp.length() - 1;
                temp = "";
            } else {
                temp += str[i];
                set.add(str[i]);
                i++;
            }
        }
        
        return Math.max(longest.length(), temp.length());
    }
}