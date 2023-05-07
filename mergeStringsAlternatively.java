import java.util.Queue;
import java.util.LinkedList;

class mergeStringsAlternatively {
    public String mergeAlternately(String word1, String word2) {

        char[] w = word1.toCharArray();
        Queue<Character> wordOne = new LinkedList<Character>();

        for(int i = 0; i <word1.length(); i++ ){
            wordOne.add(w[i]);
        }

        char[] f = word2.toCharArray();
        Queue<Character> wordTwo = new LinkedList<Character>();

        for(int i = 0; i <word2.length(); i++ ){
            wordTwo.add(f[i]);
        }

        String word = "";

        while(!(wordOne.peek() == null) && !(wordTwo.peek() == null)) {
            word+=wordOne.poll();
            word+=wordTwo.poll();
        }

        while(!(wordOne.peek() == null)) {
            word+=wordOne.poll();
        }

        while(!(wordTwo.peek() == null)) {
            word+=wordTwo.poll();
        }

        return word;
        
    }
}