# Q-1 Implement Binary tree

from binarytree import build

nodes =[3, 6, 8, 2, 11, None, 13]

binary_tree = build(nodes)
print('Binary tree from list :\n',
	binary_tree)

print('\nList from binary tree :',
	binary_tree.values)

# Q-2 Find height of a given tree

# Python3 program to find the maximum depth of tree

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def maxDepth(node):
	if node is None:
		return 0

	else:
     
		lDepth = maxDepth(node.left)
		rDepth = maxDepth(node.right)

		if (lDepth > rDepth):
			return lDepth+1
		else:
			return rDepth+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of tree is %d" % (maxDepth(root)))

# Q-3 Perform Pre-order, Post-order, In-order traversal

# In-order Traversal
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printInorder(root):

	if root:

		printInorder(root.left)
	
		print(root.val),

		printInorder(root.right)

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print("\nInorder traversal of binary tree is")
	printInorder(root)

# Preroder

# Python3 program to for tree traversals

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printPreorder(root):

	if root:

		print(root.val),

		printPreorder(root.left)

		printPreorder(root.right)

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

print("Preorder traversal of binary tree is")
printPreorder(root)

# Post Order

# Python3 program to for tree traversals

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printPostorder(root):

	if root:

		printPostorder(root.left)

		printPostorder(root.right)

		print(root.val),

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

print("\nPostorder traversal of binary tree is")
printPostorder(root)

# Q-4 Function to print all the leaves in a given binary tree

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def printLeafNodes(root: Node) -> None:

	if (not root):
		return

	if (not root.left and
		not root.right):
		print(root.data,
			end = " ")
		return

	if root.left:
		printLeafNodes(root.left)

	if root.right:
		printLeafNodes(root.right)

# Driver Code
if __name__ == "__main__":

	# Let us create binary tree shown in
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(8)
	root.right.left.left = Node(6)
	root.right.left.right = Node(7)
	root.right.right.left = Node(9)
	root.right.right.right = Node(10)

	printLeafNodes(root)

# Q-5 Implement BFS (Breath First Search) and DFS (Depth First Search)

# BFS (Breath First Search)

from collections import defaultdict

class Graph:

	# Constructor
	def __init__(self):

		self.graph = defaultdict(list)
  
	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):

		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		queue.append(s)
		visited[s] = True

		while queue:
      
			s = queue.pop(0)
			print(s, end=" ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

if __name__ == '__main__':

	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)

# DFS (Depth First Search)

from collections import defaultdict

class Graph:

	def __init__(self):

		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):

		visited.add(v)
		print(v, end=' ')

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	def DFS(self, v):

		visited = set()

		self.DFSUtil(v, visited)

if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is DFS from (starting from vertex 2)")
	# Function call
	g.DFS(2)

