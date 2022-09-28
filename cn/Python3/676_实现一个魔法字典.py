# @algorithm @lc id=676 lang=python3 
# @title implement-magic-dictionary
from typing import List
class Trie:
    def __init__(self):
        self.children=[None]*26
        self.is_end=False

    def put(self,word):
        curr_node=self
        for c in word:
            index=ord(c)-ord('a')
            c_child=curr_node.children[index]
            if c_child is None:
                curr_node.children[index]=Trie()
            curr_node=curr_node.children[index]
        curr_node.is_end=True

    def search(self,word):
        curr_node=self
        for c in word:
            if curr_node.children[ord(c)-ord('a')] is None:
                return False
            curr_node=curr_node.children[ord(c)-ord('a')]    
        
        return curr_node.is_end
    def search_back(self,word,idx=0,flag=False):
        curr_node=self
        # if flag:
        #     return curr_node.search(word[idx:])
        if idx==len(word):
            return curr_node.is_end and flag
        c=word[idx]
        tmp_flag=flag
        for i in range(26):
            if curr_node.children[i] is  None:
                continue
            if i!=ord(c)-ord('a'):
                if flag:
                    continue
                if curr_node.children[i].search_back(word,idx+1,True):
                    return True
            else:
                if curr_node.children[i].search_back(word,idx+1,tmp_flag):
           
                    return True
                    
        return False
        

        
                
                
    
from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        self.trie=Trie()
        self.len_dict=defaultdict(list)


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.put(word)
            self.len_dict[len(word)].append(ord(word[0])-ord('a'))



    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.len_dict.keys():
            return False
        return self.trie.search_back(searchWord)
        
