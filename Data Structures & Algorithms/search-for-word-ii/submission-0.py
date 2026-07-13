class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):

            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols
            ):
                return

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            node = node.children[ch]

            if node.word:
                ans.append(node.word)
                node.word = None

            board[r][c] = "#"

            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            board[r][c] = ch

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return ans