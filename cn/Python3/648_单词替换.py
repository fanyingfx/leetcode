# @algorithm @lc id=648 lang=python3 
# @title replace-words


from cn.Python3.mod.preImport import *
# @test(["cat","bat","rat"],"the cattle was rattled by the battery")="the cat was rat by the bat"
# @test(["a","b","c"],"aadsfasf absbs bbab cadsfafs")="a a b c"
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str: