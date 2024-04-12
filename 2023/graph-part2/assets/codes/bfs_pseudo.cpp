BFS(v)
  initialize a queue Q
  mark v as visited and push it to Q
  while Q is not empty:
    take the front element of Q and call it w
    for each edge w → u:
      if u is not visited
        mark it as visited and push it to Q
    END
END