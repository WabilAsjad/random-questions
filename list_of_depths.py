from collections import deque

def lists_of_depths(root):
  
  result = {}
  
  if root == None:
    return result
    
  depth = 0
  queue = deque()
  queue.append(root)
  

  while queue:
    
    size = len(queue)
    nodes = LinkedList()
    
    for i in range(size):
      curr = queue.popleft
      nodes.add(curr)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    
    result[depth] = nodes
    depth+=1
  
  return result 

