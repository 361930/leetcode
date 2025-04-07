class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        index = [i for i in range(n)]
        pairs = [(nums[i] + nums[i+1], i) for i in range(n-1)]
        heapq.heapify(pairs)
        remove = set()
        reverse_cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                reverse_cnt += 1
        
        m = n
        while reverse_cnt > 0:
            s, idx = heapq.heappop(pairs)
            if (s, idx) in remove:
                continue
            remove.add((s, idx))
            
            i = bisect.bisect_left(index, idx)
            
            # replace element
            x, y = nums[i], nums[i+1]
            xi, yi = index[i], index[i+1]
            nums.pop(i+1)
            nums[i] = x+y
            index.pop(i+1)
            m -= 1
            if x > y:
                reverse_cnt -= 1
            
            # maintain pre element
            if i-1 >= 0:
                t, ti = nums[i-1], index[i-1]
                remove.add((t+x, ti))
                heapq.heappush(pairs, (t+x+y, ti))
                if (t+x+y, ti) in remove:
                    remove.remove((t+x+y, ti))
                if t > x:
                    reverse_cnt -= 1
                if t > x+y:
                    reverse_cnt += 1
            
            # maintain post element
            if i+1 < m:
                t, ti = nums[i+1], index[i+1]
                remove.add((t+y, yi))
                heapq.heappush(pairs, (t+x+y, xi))
                if (t+x+y, xi) in remove:
                    remove.remove((t+x+y, xi))
                if y > t:
                    reverse_cnt -= 1
                if x+y > t:
                    reverse_cnt += 1

        return n - m
