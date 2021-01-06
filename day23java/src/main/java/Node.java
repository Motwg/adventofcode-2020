import java.util.Arrays;

public class Node {
    private int that;
    private Node next;

    public Node(int that, Node next) {
        this.that = that;
        this.next = next;
    }

    @Override
    public String toString() {
        return "Node{" +
                "that=" + that +
                ", next=" + next.getThat() +
                '}';
    }

    public int getThat() {
        return that;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}
