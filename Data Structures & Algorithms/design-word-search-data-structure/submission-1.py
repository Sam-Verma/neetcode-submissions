class TrieNode:
    def __init__(self):
        self.children=dict()
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True
        
    def search(self, word: str) -> bool:
        
        def dfs(node,i):

            if len(word)==i:
                return node.is_end
            
            ch=word[i]

            if ch!='.':
                if ch not in node.children:
                    return False
                node=node.children[ch]
                return dfs(node,i+1)
            
            for child in node.children.values():
                if dfs(child,i+1):
                    return True
            return False
                
        return dfs(self.root,0)
