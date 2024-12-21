from Node import Node

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        new_node = Node(homepage)
        self.homepage = new_node
        self.current = self.homepage

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_node = Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node
        
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(0, steps):
            if self.current.prev:
                self.current = self.current.prev 
        return self.current.value

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(0, steps):
            if self.current.next:
                self.current = self.current.next
        return self.current.value
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Constraints:

# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= steps <= 100
# homepage and url consist of  '.' or lower case English letters.
# At most 5000 calls will be made to visit, back, and forward.
# 10000 = 10 의 4승 5
