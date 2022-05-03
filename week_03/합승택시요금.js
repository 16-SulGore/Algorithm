function solution(n, s, a, b, fares) {
  const dp = Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i == j ? 0 : Infinity))
  );

  fares.map((fare) => {
    [i, j, distance] = fare;
    dp[i - 1][j - 1] = distance;
    dp[j - 1][i - 1] = distance;
  });

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
      }
    }
  }

  let answer = Infinity;
  for (let i = 0; i < n; i++) {
    answer = Math.min(answer, dp[s - 1][i] + dp[i][a - 1] + dp[i][b - 1]);
  }
  return answer;
}
