class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        @cache
        def dp(i, flag, rest, odd_even):
            if i == len(t):
                return flag >= 0 and not rest and not odd_even
            
            
            ans = int(0 < i < len(t) and not rest and not odd_even)
            for j in range(int(i == 0), 10):
                # compare the most significant digit with upper limit only when
                # previous comparsion are all equal (flag = 0)
                new_flag = flag
                if flag == 0:
                    # diff determined if current digit not equal with the one of upper limit
                    if j > int(t[i]): new_flag = -1
                    if j < int(t[i]): new_flag = 1
                    
                if j % 2:
                    ans += dp(i+1, new_flag, (rest * 10 + j) % k, odd_even+1)
                else:
                    ans += dp(i+1, new_flag, (rest * 10 + j) % k, odd_even-1)
            return ans
        
        t = str(high)
        h = dp(0, 0, 0, 0)
        dp.cache_clear()
        t = str(low - 1)
        l = dp(0, 0, 0, 0)
        return h - l