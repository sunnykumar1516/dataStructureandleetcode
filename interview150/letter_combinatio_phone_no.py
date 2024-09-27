#question number 17.

def solve(digits):
    digit_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if not digits:
        return []
    result = []
    
    # Backtracking function to generate all combinations
    def backtrack(index, current_combination):
        if index == len(digits):
            result.append(current_combination)
            return
        
        # Get the possible characters for the current digit
        possible_chars = digit_to_char[digits[index]]
        
        # Loop through the possible characters and recurse
        for char in possible_chars:
            current=current_combination + char
            backtrack(index + 1, current)
            current = ""
    
    # Start backtracking from the first digit
    backtrack(0, "")
    
    return result
            
        
    
digits = "23"
print(solve(digits))