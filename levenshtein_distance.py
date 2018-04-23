def levenshtein_distance(str1, str2):
	"This function calculates the levenshtein distance between str1 and str2"
	n, m = len(str1), len(str2)
	
	if n == 0:
		return m
	if m == 0:
		return n
	
	tab = [[0] * (m+1) for i in range(n+1)]
	
	for i in range(n+1):
		tab[i][0] = i
	for j in range(m+1):
		tab[0][j] = j
		
	for i in range(1, n+1):
		for j in range(1, m+1):
			tab[i][j] = min(min(tab[i-1][j]+1, tab[i][j-1]+1), tab[i-1][j-1] + (0 if str1[i-1] == str2[j-1] else 1))
			
	return tab[n][m]