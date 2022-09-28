def kSimilarity (s1: str, s2: str) -> int:
    def adjacent(z):
        i = 0
        while z[i] == s2[i]:           # 找到第一个与 s2 中对应位置不想等的字母 的位置 i
            i += 1

        res = []
        for j in range(i+1, len(z)):         # 用 i 之后的字母与其交换
            if z[j] == s2[i] and z[j] != s2[j]:     # z[j] 是 i 后面的字母，如果 z[j] 等于 s2[i] 意味着可以交换过来
                                                    # 注意还要判断下 z[j] != s2[j]，防止交换过来反而扰乱了原来交换好的
                res.append(z[:i] + z[j] + z[i+1:j] + z[i] + z[j+1:] )
        return res


    q = [s1]
    vis = {s1}
    level = 0
    while q:
        for k in range(len(q)):        # BFS 对每层作处理
            tmp = q.pop(0)
            if tmp == s2: 
                return level
            for nex in adjacent(tmp):       # 求相邻的结点
                if nex not in vis:
                    vis.add(nex)
                    q.append(nex)
        level += 1

l=kSimilarity("bccaba","abacbc")
print(l)