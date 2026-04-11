/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    public bool CanAttendMeetings(List<Interval> intervals) {
        intervals.Sort((a,b) => a.start.CompareTo(b.start));

        for(int i = 1; i < intervals.Count; i++ )
        {
            Interval i1 = intervals[i -1];
            Interval i2 = intervals[i];

            if(i1.end > i2.start)
            {
                return false;
            }
        }

        return true;
    }
}
