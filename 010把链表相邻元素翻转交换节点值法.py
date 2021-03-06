import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表Head->1->2->3->4->5->7->7->8
反转为链Head->2->1->4->3->7->5->8->7
要求：
方法：建立两个指针slow和fast，fast比slow快一步，步长均为2，两个一组，在pre和next进行交换。
"""
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		#这里与之前不同，先生成一个随机数，作为节点值
		n = random.randint(1, 9)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	return head
def function(head):
	if head.next is None or head.next.next is None:
		return head
	#太简单了不写了
	return head
if __name__ == '__main__':
	head = creatLink(10)
	print("head:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	head = function(head)
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next