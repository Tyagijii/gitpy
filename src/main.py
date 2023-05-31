def average(*args):
  print(args)

  return sum(args) / len(args)

average(*[1, 2, 3]) # 2.0
print(average(1, 2, 3)) # 2.0


print(sum((1,2,3)))

print(eval('4+7*6-5'))