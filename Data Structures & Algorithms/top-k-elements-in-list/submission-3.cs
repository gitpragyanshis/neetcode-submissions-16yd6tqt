public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var freqMap = new Dictionary<int, int>();

        foreach(var num in nums){
            if(!freqMap.ContainsKey(num)){
                freqMap.Add(num, 0);
            }
            freqMap[num]++;
        }

        var resultArray = new List<List<int>>(new List<int>[nums.Length + 1]);

        foreach(var kvp in freqMap){
            if(resultArray[kvp.Value] == null){
                resultArray[kvp.Value] = new List<int>();
            }
            resultArray[kvp.Value].Add(kvp.Key);
        }
        var result = new List<int>();

        for (var i = resultArray.Count() - 1; i >= 0; i--){
            if (resultArray[i] == null) continue;
            for (var j = 0; j < resultArray[i].Count(); j ++){
                result.Add(resultArray[i][j]);

                if (result.Count == k){
                    return result.ToArray();;
                }

            } 
        }

        return null;
    }
}
