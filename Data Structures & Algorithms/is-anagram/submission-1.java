class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> freqS = calculateFreq(s);
        Map<Character, Integer> freqT = calculateFreq(t);
        return (freqS.equals(freqT));
        

    }

    private Map<Character, Integer> calculateFreq(String aus) {
        Map<Character, Integer> freq = new HashMap<>();

        for (int i=0; i<aus.length(); i++) {
            Character c = aus.charAt(i);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        System.out.println(freq);
        return freq;
    }
}
