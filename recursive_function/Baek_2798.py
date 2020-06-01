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


class _2798(Base):
    count = 0
    target_number = 0
    card_list = []

    def run(self):
        num_list = self.read_num_list()
        count = int(num_list[0])
        target_number = int(num_list[1])
        max_sum = int(0)

        card_list = self.read_num_list()
        card_len = len(card_list)

        for i in range(card_len):
            x = int(card_list[i])
            if x > target_number:
                continue

            for j in range(i + 1, card_len):
                y = int(card_list[j])
                if y > target_number:
                    continue

                for k in range(j + 1, card_len):
                    z = int(card_list[k])
                    if z > target_number:
                        continue

                    card_sum = x + y + z

                    if max_sum < card_sum <= target_number:
                        max_sum = card_sum

                    if target_number == card_sum:
                        print(target_number)
                        exit()

        print(max_sum)


_2798().run()
