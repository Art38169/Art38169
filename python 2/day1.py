def len_word(x: str) -> list:
  len = 0
  len_list = []
  for char in x:
    if char != " ":
      len += 1
    else:
      len_list.append(len)
      len = 0
  return len_list
print(len_word("A A AA A"))
  