import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
public class RandomWord {
    public static void main(String[] args) {
        String w = "";
        String c = "";
        int i = 1;
        while (!StdIn.isEmpty()) {
            w = StdIn.readString();
            if (StdRandom.bernoulli(1.0/i)) {
                c = w;
            }
            i += 1;
        }
        StdOut.println(c);
    }
}