class Base:
    file = None
    input_list = None

    def initialize(self, file_name=None, input=None):
        if file_name is not None:
            self.file = open(file_name, 'r')
        if input is not None:
            self.input_list = input.split('\n')

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


def fibonacci(num):
    num = int(num)
    if num == 0:
        return 0
    elif num < 3:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


class _10870(Base):
    def run(self):
        print(fibonacci(self.readline()))


_10870().run()
