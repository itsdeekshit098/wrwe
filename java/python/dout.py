def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
  else:
    result = 0
  return result

print(tri_recursion(6))

#dout in 2b1 we wnat to assign fact1 as 1 else part  but here if we decalre result as 0 also it is working