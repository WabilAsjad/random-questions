

#Given a directed graph, design an algorithm to find out whether there is a node between two nodes.
#simple bfs or dfs


def find_route_dfs(start, target):
  
  visited = set()
  stack = []
  stack.append(start)
  
  while stack:
    curr = stack.pop()
    if curr == target:
       return True
    if curr not in visited:
      visited.add(curr)
    for neighbor in curr.adjacent_nodes:
        if neighbor not in visited:
          visited.add(neighbor)
          stack.append(neighbor)
        if neighbor == target:
          return True
          
   return False 
 
 
 def dfs_recurse(visited, graph, root):
     visited = set()
     if root not in visited:
        visited.add(root)
        for neighbor in root.adjacent_nodes:
            dfs(visited, graph, neighbor)
            
        
    
          
    
 from collections import dequeue
 def find_route_bfs(start, target):
  
  visited = set()
  queue = deque()
  queue.append(start)
  
  while queue:
    curr = queue.popleft()
    if curr == target:
       return True
    if curr not in visited:
      visited.add(curr)
    for neighbor in curr.adjacent_nodes:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)
        if neighbor == target:
          return True
          
   return False
  
