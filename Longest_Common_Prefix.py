class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #optimal_approach
        op=""#output string initialize
        for i in range(len(strs[0])):#string's 0th index val's length iteration
            for s in strs:#String's elemental Iteration 
                if i==len(s) or s[i]!=strs[0][i]:return op#assinging and checking string's length to list element's indx and character value are equal and printing output string 
                    
            op+=strs[0][i]#appending the output string in list's common string 's index val
        return op  #output string return
