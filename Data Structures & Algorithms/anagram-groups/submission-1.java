class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramMap = new HashMap<>();
        for (String s: strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);
            anagramMap.putIfAbsent(sortedS, new ArrayList<>());
            anagramMap.get(sortedS).add(s);
        }
        return new ArrayList<>(anagramMap.values());
    }
}
