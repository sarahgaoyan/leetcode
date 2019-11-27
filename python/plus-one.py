
'''给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def plusOne(self, digits):
        sum = digits[len(digits) -1] + 1 
        overflow = sum // 10
        digits[len(digits) -1] = sum % 10
        if overflow == 0: return digits
        for i in range(len(digits) - 2, -1, -1):
            sum = digits[i] + overflow
            overflow = sum // 10
            digits[i] = sum % 10
        if overflow == 1:
            digits.insert(0, overflow)
        return digits

'''    def plusOne(self, digits):
        sums = 0
        for i in digits:
            sums = sums * 10 + i #10进制乘以10，进行累和；
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

作者：balconyang
链接：https://leetcode-cn.com/problems/plus-one/solution/python-jie-zhe-dao-ti-hen-jian-dan-by-balconyang/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''

s = Solution()
a = [1,2,3]
b = [4,3,2,1]
c = [9, 9, 9]

print(s.plusOne(a))
print(s.plusOne(b))
print(s.plusOne(c))

        
