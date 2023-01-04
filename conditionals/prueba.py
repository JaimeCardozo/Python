txt = "  casa  .  txt  .pdf  "
print(len(txt))
position = txt.rfind(".")
print(position)
print(txt[position + 1])