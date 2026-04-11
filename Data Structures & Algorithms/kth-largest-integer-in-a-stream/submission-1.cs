public class KthLargest {
    private int l;
    private PriorityQueue<int, int> pQueue;
    public KthLargest(int k, int[] nums) {
        l = k;
        pQueue = new PriorityQueue<int, int>();

        foreach(var num in nums)
        {
            pQueue.Enqueue(num, num);

            if(pQueue.Count > l)
            {
                pQueue.Dequeue();
            }
        }
    }
    
    public int Add(int val) {
        pQueue.Enqueue(val, val);

        if(pQueue.Count > l)
        {
            pQueue.Dequeue();
        }

        return pQueue.Peek();
    }
}
