def count_balanced_combinations(s):
    """
    括弧文字列から最小限の削除でバランスの取れた組み合わせの数を計算
    """
    n = len(s)
    
    # dp[i][j] = i番目までの文字で、開き括弧がj個多い状態での組み合わせ数
    # jは開き括弧の数 - 閉じ括弧の数
    dp = {}
    
    def solve(i, balance):
        # メモ化
        if (i, balance) in dp:
            return dp[(i, balance)]
        
        # ベースケース
        if i == n:
            return 1 if balance == 0 else 0
        
        result = 0
        
        if s[i] == '(':
            # 開き括弧を使う場合
            result += solve(i + 1, balance + 1)
            # 開き括弧を削除する場合
            result += solve(i + 1, balance)
        else:  # s[i] == ')'
            # 閉じ括弧を使う場合（balanceが正の時のみ）
            if balance > 0:
                result += solve(i + 1, balance - 1)
            # 閉じ括弧を削除する場合
            result += solve(i + 1, balance)
        
        dp[(i, balance)] = result
        return result
    
    return solve(0, 0)

def find_minimum_removals(s):
    """
    最小削除数を計算（参考用）
    """
    open_count = 0
    close_needed = 0
    
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                close_needed += 1
    
    return open_count + close_needed