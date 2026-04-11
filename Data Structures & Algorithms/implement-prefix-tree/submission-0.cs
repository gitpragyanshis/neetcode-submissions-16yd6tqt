public class PrefixTree {
    private TrieNode trie;
    public PrefixTree() {
        trie  = new TrieNode();
    }
    
    public void Insert(string word) {
        var temp = trie;
        foreach (var c in word) {
            if (!temp.Node.ContainsKey(c)) {
                temp.Node[c] = new TrieNode();
            }
            temp = temp.Node[c];
        }
        temp.IsWord = true;
    }
    
    public bool Search(string word) {
        var temp = trie;
        foreach (var c in word) {
            if (!temp.Node.ContainsKey(c)) {
                return false;
            }
            temp = temp.Node[c];
        }
        
        return temp.IsWord;
    }
    
    public bool StartsWith(string prefix) {        
        var temp = trie;
        foreach (var c in prefix) {
            if (!temp.Node.ContainsKey(c)) {
                return false;
            }
            temp = temp.Node[c];
        }
        
        return true;
    }
}

public class TrieNode {
    public Dictionary<char, TrieNode> Node {get; set;}
    public bool IsWord {get; set;}
    
    public TrieNode()
    {
        Node = new Dictionary<char, TrieNode>();
        IsWord = false;
    }
}
