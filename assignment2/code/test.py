class a:

    def __init__(self, tall):
        self.tall = tall

    def __eq__(self,other):
        return self.tall == other.tall



a = 1
print(hex(id(a)))


b = 1
print(hex(id(b)))

print(a == b)
print(a is b)
      