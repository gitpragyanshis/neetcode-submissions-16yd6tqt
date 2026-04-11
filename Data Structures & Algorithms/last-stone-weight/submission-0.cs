public class Solution {
    public int LastStoneWeight(int[] stones) {
        var minHeap = new PriorityQueue<int,int>();

        foreach(var stone in stones)
        {
            minHeap.Enqueue(-stone, -stone);
        }

        while(minHeap.Count > 1)
        {
            int first = minHeap.Dequeue();
            int second = minHeap.Dequeue();

            if(second > first)
            {
                minHeap.Enqueue(first - second, first - second);
            }
        }

        minHeap.Enqueue(0,0);
        return Math.Abs(minHeap.Peek());
    }
}
