
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
    public static void main(String[] args) {
//        int[] testCups = {5,8,6,4,3,9,1,7,2};
//        int[] testCups = {3, 8, 9, 1, 2, 5, 4, 6, 7};
        int[] first = {5,8,6,4,3,9,1,7,2};
        int[] second = new int[1000000-9];
        for (int i=0; i<second.length; ++i)
            second[i] = i + 10;
        int[] testCups = IntStream.concat(Arrays.stream(first), Arrays.stream(second)).toArray();

        System.out.println("Last element: " + testCups[testCups.length-1]);
        System.out.println("Initiated");
        List<Node> nodes = new LinkedList<>();

        Node next = null;
        Node node;
        for (int i=testCups.length-1; i>-1; --i) {
            node = new Node(testCups[i], next);
            nodes.add(node);
            next = node;
        }
        System.out.println("Created Nodes");
        nodes.get(0).setNext(nodes.get(nodes.size() - 1));
        System.out.println("Sorting");
        nodes = nodes.stream()
                .sorted(Comparator.comparingInt(Node::getThat))
                .collect(Collectors.toList());
        System.out.println("Sorted");

        nodes.stream().limit(15).forEach(System.out::println);
        start(testCups[0], nodes, 10000000);
    }

    public static void start(int firstValue, List<Node> nodes, int iterations) {
        Node cur = nodes.get(firstValue - 1);
        Node temp_cur;
        Node pickup;
        Node destination;

        Node t_cur;
        Node t_pickup;
        Node t_destination;

        int[] pickupValues = new int[3];
        for (int i=0; i<iterations; ++i) {
            temp_cur = cur;
            if (i % 10000 == 0)
                System.out.println("iteration: " + i);


            for (int j=0; j<3; ++j) {
                cur = cur.getNext();
                pickupValues[j] = cur.getThat();
                //System.out.print(pickupValues[j]);
            }

            pickup = cur;
            cur = cur.getNext();
            destination = getDest(temp_cur.getThat(), nodes, pickupValues);

            //replacing
            t_cur = temp_cur.getNext();
            t_pickup = pickup.getNext();
            t_destination = destination.getNext();

            temp_cur.setNext(t_pickup);
            pickup.setNext(t_destination);
            destination.setNext(t_cur);


        }

        Node first = nodes.get(0);
        for (int i=0; i<3; ++i) {
            System.out.println(first.getThat());
            first = first.getNext();
        }
    }

    public static Node getDest(int currentValue, List<Node> cups, int[] pickupValues) {
        boolean inPickup;
        do {
            currentValue--;
            if (currentValue < 1)
                currentValue = cups.size();
            inPickup = checkIfInPickup(currentValue, pickupValues);
        } while (inPickup);
        return cups.get(currentValue - 1);
    }

    public static boolean checkIfInPickup(int currentValue, int[] pickupValues) {
        for (int val : pickupValues) {
            if (val == currentValue) {
                return true;
            }
        }
        return false;
    }
}
