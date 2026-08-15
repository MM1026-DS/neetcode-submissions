class Solution:
    def climbStairs(self, n: int) -> int:

        ##
        ## 2 
        ## 1

     ##(dfs(1,2) + dfs(2,2))
     ##  dfs(1,2)
     # / 
     ## dfs(1,1) + dfs(2,1)
    ##  


        def dfs(steps):

         
            if steps<0:
                return 0 
            
            if steps == 0:
                return 1 


            if dp[steps]!=-1:
                return dp[steps]
            


            dp[steps] = dfs(steps-1) + dfs(steps-2)
            
            return dp[steps]
        

        dp = [-1]*(n+1)
    
        dp[n] = dfs(n-1)+dfs(n-2)
        return dp[n]