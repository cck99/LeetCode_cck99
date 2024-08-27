class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 第一步：拷贝每个节点并插入到原节点后面
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next, None)
            cur.next = new_node
            cur = new_node.next
        
        # 第二步：设置拷贝节点的 random 指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # 第三步：将两个链表分离
        cur = head
        copy_head = head.next
        copy_cur = copy_head
        
        while cur:
            cur.next = cur.next.next  # 修正：将原链表的 next 指针指向下一个原节点
            if copy_cur.next:
                copy_cur.next = copy_cur.next.next  # 修正：将拷贝链表的 next 指针指向下一个拷贝节点
            cur = cur.next
            copy_cur = copy_cur.next
        
        return copy_head
