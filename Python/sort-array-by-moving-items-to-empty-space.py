# Time:  O(n)
# Space: O(n)

# greedy, sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def min_moves(d):
            def index(x):
                return d*(len(nums)-1) if x == 0 else x-d

            a = nums[:]
            result = 0
            for i in xrange(len(a)):
                l, found = 1, (a[i] == 0)
                while index(a[i]) != i:
                    j = index(a[i])
                    a[i], a[j] = a[j], a[i]
                    l += 1
                    found |= (a[i] == 0)
                if l >= 2:
                    result += l-1 if found else l+1
            return result

        return min(min_moves(0), min_moves(1))
