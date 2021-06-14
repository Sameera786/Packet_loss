class file_class:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)

    def fun(self):
        lines = self.file.readlines()
        for line in lines:
            print(line)

file_class1 = file_class('prgm.txt', 'r')
file_class2 = file_class('file1.txt', 'r')
file_class1.fun()
file_class2.fun()