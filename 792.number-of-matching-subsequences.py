#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 对 s 进行预处理，记录字符 c 的所有出现位置
        index = [[] for _ in range(256)]
        for i in range(len(s)):
            c = ord(s[i]) # 获取s中指定下标的字符及其ascll码值
            if index[c] == None:
                # 如果第一次出现，则初始化一个空列表
                index[c] = []
            index[c].append(i) # 添加位置信息
        
        # 统计符合要求的 words
        res = 0 # 记录符合要求的单词数量
        for word in words: # 遍历单词列表
            i = 0 # 记录已匹配的单词长度
            j = 0 # 指向 s 中当前查找的字符的位置
            for i in range(len(word)): # 遍历单词中的字符
                c = ord(word[i]) # 获取单词当前字符及其ascll码值
                # 如果 s 中不存在单词当前字符，则不可能匹配
                if not index[c]:
                    break
                pos = self.left_bound(index[c], j) # 二分查找 c 第一次出现的位置
                # 如果没找到，则已经匹配失败了
                if pos == len(index[c]):
                    break
                j = index[c][pos] + 1 # pos 是下标，所以要加1，指向下一个位置
            if i == len(word):
                # 如果整个单词匹配结束，说明这是一个符合要求的单词
                res += 1
        
        # 返回符合要求的单词数量
        return res

    def left_bound(self, arr, target) -> int:
        # 查找左侧边界的二分查找
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1 if left == len(arr) or arr[left] != target else left        
    # @lc code=end

