def graduationCeremony(N):
    dp = [[0 for _ in range(4)] for _ in range(N+1)]
    dp[0][0] = 1  

    for i in range(1, N+1):
        dp[i][0] = sum(dp[i-1])  # Attending today
        for j in range(1, 4):
            dp[i][j] = dp[i-1][j-1]  # Absent today

    total_ways = sum(dp[N])
    attended_last_day = sum(dp[N-1])  
    missing_ceremony = total_ways - attended_last_day

    return f"{missing_ceremony}/{total_ways}"

print(graduationCeremony(5))  
print(graduationCeremony(10))