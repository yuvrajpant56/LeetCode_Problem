class LongestSubstringSolver:
    def solve(self, s):
        # Dictionary to store the last index of every character seen.
        last_seen = {}
        start = 0  # start index of the current substring window
        max_length = 0  # maximum length of substring found
        
        for i, char in enumerate(s):
            # If the character is found in last_seen and it is within the current window
            if char in last_seen and last_seen[char] >= start:
                # Move the start right after the last occurrence of this character
                start = last_seen[char] + 1
            # Update the last seen index of the current character
            last_seen[char] = i
            # Calculate the length of the current window
            max_length = max(max_length, i - start + 1)
        return max_length

# Example usage:
solver = LongestSubstringSolver()
example_str = "abcabcbb"
print("Longest Substring Length:", solver.solve(example_str))
# Expected Output: 3 (The answer is "abc")