from typing import List

class Merge: 
  def solve(self, intervals:List[List[int]]) -> List[List[int]]:
    if not intervals: 
      return []
    
    intervals.sort(key=lambda x: x[0])

    output = [intervals[0]]

    for i in range(1, len(intervals)):
      current_start, current_end = intervals[i]
      last_start, last_end = output[-1]

      if current_start <= last_end: 
        output[-1][1] = max(current_end, last_end)
      else:
        output.append(intervals[i])
    return output
  
# Example usage / quick test
if __name__ == "__main__":
    solver = Merge()
    test_intervals = [[1,3],[2,6],[8,10],[15,18]]
    merged_intervals = solver.solve(test_intervals)
    print("Merged Intervals:", merged_intervals)
    # Expected Output: [[1, 6], [8, 10], [15, 18]]