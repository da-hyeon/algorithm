class Base:
    file = None
    input_list = None

    def initialize(self, file_name=None, input=None):
        if file_name is not None:
            self.file = open(file_name, 'r')
        if input is not None:
            self.input_list = input.split('\n')

        return self

    def readline(self):
        if self.file is not None:
            return self.file.readline()
        if self.input_list is not None:
            return self.input_list.pop(0)
        import sys
        return sys.stdin.readline()

    def read_num_list(self, delimit=' ', is_integer=True):
        num_list = self.readline().strip().split(delimit)
        if is_integer is True:
            for index in range(len(num_list)):
                num_list[index] = int(num_list[index])
        return num_list


class _2231(Base):
    constructor = 0

    def run(self):
        constructor = int(self.readline())

        x = 0
        if constructor > 1000:
            x = int(constructor - (9*len(str(constructor))))

        while True:
            x += 1
            num_list = [int(i) for i in str(x)]

            num = x + sum(num_list)

            if num == constructor:
                print(x)
                break

            if x > constructor:
                print(0)
                break


text = '256'

obj = _2231().initialize(input=text)
obj.run()