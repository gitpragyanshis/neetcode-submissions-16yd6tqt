public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        var minHeap = new PriorityQueue<int[], double>();
        var result = new int[k][];
        foreach(int[] point in points)
        {
            var distance = CalculateDistance(point[0], point[1]);
            minHeap.Enqueue(point, distance);
        }

        while(k > 0)
        {
            result[k -1] = minHeap.Dequeue();
            k--;
        }

        return result;

    }

    static double CalculateDistance(int x2, int y2)
    {
        return Math.Sqrt(Math.Pow(x2 - 0, 2) + Math.Pow(y2 - 0, 2));
    }
}
