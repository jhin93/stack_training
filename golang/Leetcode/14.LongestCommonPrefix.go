package Leetcode

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	if len(strs) == 1 {
		return strs[0]
	}
	firstWord := strs[0]
	for i := 0; i < len(firstWord); i++ {
		firstPrefix := firstWord[i]
		for j := 1; j < len(strs); j++ {
			if i >= len(strs[j]) || strs[j][i] != firstPrefix {
				return firstWord[:i]
			}
		}
	}
	return firstWord
}
