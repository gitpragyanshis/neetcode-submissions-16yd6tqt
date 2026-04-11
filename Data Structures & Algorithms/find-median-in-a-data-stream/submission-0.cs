public class MedianFinder {
    private PriorityQueue<int, int> minHeap;
    private PriorityQueue<int, int> maxHeap;

    public MedianFinder() {
        minHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        maxHeap = new PriorityQueue<int, int>();
    }
    
    public void AddNum(int num) {
        if (maxHeap.Count != 0 && maxHeap.Peek() < num) {
            maxHeap.Enqueue(num, num);
        } else {
            minHeap.Enqueue(num, num);
        }

        if (minHeap.Count > maxHeap.Count + 1) {
            int val = minHeap.Dequeue();
            maxHeap.Enqueue(val, val);
        } else if (maxHeap.Count > minHeap.Count + 1) {
            int val = maxHeap.Dequeue();
            minHeap.Enqueue(val, val);
        }
    }
    
    public double FindMedian() {
        if (minHeap.Count > maxHeap.Count) {
            return minHeap.Peek();
        } else if (maxHeap.Count > minHeap.Count) {
            return maxHeap.Peek();
        }

        return (minHeap.Peek() + maxHeap.Peek()) / 2.0;
    }
}