#Knapsack using Both Bottom-Up and Top-Down Approaches

def knapsack_top_down(weights, values, n, capacity, memo):

    
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    
    if weights[n - 1] > capacity:

        memo[n][capacity] = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

    else:

       
        take = values[n - 1] + knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        
        not_take = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

      
        memo[n][capacity] = max(take, not_take)

    return memo[n][capacity]




def knapsack_bottom_up(weights, values, n, capacity):

   
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            
            if weights[i - 1] <= w:

              
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

                
                not_take = dp[i - 1][w]


                dp[i][w] = max(take, not_take)

            else:


                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]




weights = [3, 1, 4, 2]
values = [12, 10, 20, 15]
capacity = 5

n = len(weights)




memo = [[-1] * (capacity + 1) for _ in range(n + 1)]

top_down_result = knapsack_top_down(
    weights,
    values,
    n,
    capacity,
    memo
)



bottom_up_result = knapsack_bottom_up(
    weights,
    values,
    n,
    capacity
)




print("Top-Down Maximum Value:", top_down_result)
print("Bottom-Up Maximum Value:", bottom_up_result)