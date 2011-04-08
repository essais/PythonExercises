import string
import re

class Node:
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)
	
	def printBackward(self):
		if self.next != None:
			tail = self.next
			tail.printBackward()
		print self.cargo

class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None
	def printBackward(self):
		if self.next != None:
			tail = self.next
			tail.printBackward()
		print self.cargo

class Queue:
	def __init__(self):
		self.length = 0
		self.head = none

	def isEmpty(self):
		return (self.length == 0)

	def insert(self, cargo):
		node = Node(cargo)
		node.next = None
		if self.head == None:
			self.head = node
		else:
			last = self.head
			while last.next: last = last.next
			last.next = node
		self.length = self.length + 1

class PriorityQueue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def insert(self, item):
		self.items.append(item)

	def remove(self):
		maxi = 0
		for i in range(1, len(self.items)):
			if self.items[i] > self.items[maxi]:
				maxi = i
		item = self.items[maxi]
		self.items[maxi:maxi+1] = []
		return item

class Golfer:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def __str__(self):
		return "%-16s: %d" % (self.name, self.score)

	def __cmp__(self, other):
		if self.score < other.score: return 1 #less is more
		if self.score > other.score: return -1
		return 0

class Tree:
	def __init__(self, cargo, left = None, right = None):
		self.cargo = cargo
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.cargo)

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right
	
	def getCargo(self):
		return str(self.cargo)

	def setLeft(self, tree):
		self.left = tree
	
	def setRight(self, tree):
		self.right = tree
	
	def setCargo(self, cargo):
		self.cargo = cargo

def total(self):
	if self == None:
		return 0
	return total(self.left) + total(self.right) + self.cargo

def printTree(tree):
	if tree == None: return
	print tree.cargo,
	printTree(tree.left)
	printTree(tree.right)

def printTreePostorder(tree):
	if tree == None: return
	printTreePostorder(tree.left)
	printTreePostorder(tree.right)
	print tree.cargo,

def printTreeInorder(tree):
	if tree == None: return
	printTreeInorder(tree.left),
	print tree.cargo,
	printTreeInorder(tree.right)

def printTreeIndented(tree, level = 0):
	if tree == None: return
	printTreeIndented(tree.right, level+1)
	print " " * level + str(tree.cargo)
	printTreeIndented(tree.left, level + 1)

def takeapart(expr):
	tokenList = re.split("([^0-9])", expr)
	print tokenList

def getToken(tokenList, expected):
	if tokenList[0] == expected:
		del tokenList[0]
		return True
	else:
		return False

def getNumber(tokenList):
	if getToken(tokenList, "("):
		x = getSum(tokenList)
		if not getToken(tokenList, ")"):
			raise ValueError, "missing parenthesis"
		return x
	else:
		x = tokenList[0]
		if not isinstance(x, int): return None
		tokenList[0:1] = []
		return Tree (x, None, None)

def getProduct(tokenList):
	a = getNumber(tokenList)
	if getToken(tokenList, "*"):
		b = getProduct(tokenList)
		return Tree ("*", a, b)
	else:
		return a

def getSum(tokenList):
	a = getProduct(tokenList)
	if not getToken(tokenList, "+"):
		raise ValueError, "not addition"
	elif getToken(tokenList, "+"):
		b = getSum(tokenList)
		return Tree("+", a, b)
	#else:
		#return a

def yes(ques):
	from string import lower
	ans = lower(raw_input(ques))
	return (ans[0] == "y")

def animal():
	root = Tree("bird")
	
	while True:
		print
		if not yes("Are you thinking of an animal? "): break

		tree = root
		while tree.getLeft() != None:
			prompt = tree.getCargo() + "? "
			if yes(prompt):
				tree = tree.getRight()
			else:
				tree = tree.getLeft()

		guess = tree.getCargo()
		prompt = "Is it a " + guess + "? "
		if yes(prompt):
			print "I rule!"
			continue
			
		prompt = "What is the animal's name? "
		animal = raw_input(prompt)
		prompt = "What question would distinguish a %s from a %s? "
		question = raw_input(prompt % (animal, guess))

		tree.setCargo(question)
		prompt = "If the animal were %s the answer would be? "
		if yes(prompt % animal):
			tree.setLeft(Tree(guess))
			tree.setRight(Tree(animal))
		else:
			tree.setLeft(Tree(animal))
			tree.setRight(Tree(guess))

