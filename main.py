import hashlib

def gen(file_name):
  for line in open(file_name, "rb"):
    yield hashlib.md5(line).hexdigest()

t = gen("text.txt")

print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
