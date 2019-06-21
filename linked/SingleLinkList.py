from linked.SingleNode import SingleNode

class SingleLinkList:
    """单链表"""
    def __init__(self):
        # _私有变量
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.item,end="->")
            cur = cur.next
        print("None",end="\n")

    def add(self,item):
        """头部添加元素"""
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        """尾部添加元素"""
        node =SingleNode(item)
        # 判断链表是否为空，如果为空，则将_head指向新节点
        if self.is_empty():
            self._head = node
            return
        cur = self._head
        # 寻找尾节点
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos<=0:
            self.add(item)
        # 若指定位置超过尾结点，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 中间位置插入
        else:
            node = SingleNode(item)
            pre = self._head
            count = 0
            # 查找要添加位置的节点的前一个结点，因为位置默认为从0开始
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self._head
        # 要删除节点的前一个节点
        pre = None
        while cur is not None:
            if cur.item == item:
                # 找到了指定元素
                if not pre:
                    # 要删除的是头节点
                    self._head = cur.next
                else:
                    # 要删除的不是头节点
                    pre.next = cur.next
                break
            else:
                # 未找到指定元素，继续向后寻找
                pre = cur
                cur = cur.next

    def search(self,item):
        """查找节点是否存在，存在返回True，否则返回False"""
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    """测试单向链表"""
    list = SingleLinkList();
    list.add(1)
    list.add(3)
    list.add(5)
    list.add(8)
    list.append(9)
    list.append(10)
    list.travel()
    list.insert(2,4)
    list.travel()
    list.remove(9)
    list.travel()
    list.remove(8)
    list.travel()