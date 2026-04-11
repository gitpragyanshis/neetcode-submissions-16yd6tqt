public class MinStack {
    public Stack<int> stack;
    public Stack<int> minstack;
    public MinStack() {
        stack = new Stack<int>();
        minstack = new Stack<int>();
    }
    
    public void Push(int val) {
        stack.Push(val);
        var minValue = Math.Min(val, minstack.Any() ? minstack.Peek():val);
        minstack.Push(minValue);
    }
    
    public void Pop() {
        stack.Pop();
        minstack.Pop();
    }
    
    public int Top() {
       return stack.Peek();
    }
    
    public int GetMin() {
        return minstack.Peek();
    }
}
