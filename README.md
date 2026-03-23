# Problem: Enumerating Oriented Gene Orderings

### The Mission
  Given number (n <= 6), we should combine each number to n, after that for each combination we must print them by -1, so if we get n = 2, then combinations would be (1, 2) and (2, 1), so 
  multiplying them by -1, we get another combination (1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1). 

  By this problem we can get combinations of gene orders, by evolution one gene order like (1, 2) could transform to (-1, 2) creating one life
  
### Technical Approach
| Phase | Action | Tool/Method |
| :--- | :--- | :--- |
| **Understand problem condition** | Search, Google it | brain, AI |
| **Create file for large results** | Create simply txt file | file system |
| **Get Data** | File reading | `strip().split()` |
| **Core Processing** | Factorial & Libraries | `itertools` module |
| **Output Mgmt** | Large data handling | `with open() as file` |

### Complexity
**Time complexity:** $O(n! \cdot 2^n)$ - because analyzing each permutation is required 
**Space complexity:** $O(n)$ - writing len(n) list for file in each loop, gives O(n) space complexity. 


### Execution Flow
1. **Initialize, save range(n) to list:** `signs = list(range(1, n+1))`
2. **Compute:** Calculate $n! \times 2^n$ for amount of final combinations by mathematics.
3. **Stream:** Use a generator to write results to `result.txt`.
