class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count=[0]*26
        for letter in p:
            p_count[ord(letter)-97]+=1
        _len=len(p)
        current=[0]*26
        result=[]
        for i in range(len(s)):
            current[ord(s[i])-97]+=1
            #去除滑动窗口前面的一个元素
            if i>=_len:
                current[ord(s[i-_len])-97]-=1;
            if current==p_count:
                result.append(i-_len+1)
        return result
