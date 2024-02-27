dict_to_write = {}
list_list = []
# сюда будут зап-ся промежут. списки перед сортировкой

class FileToList():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf-8')
        self.to_list = []
        for line in self.file:
            line = line.strip('\n ')
            self.to_list.append(line)
        self.to_list.insert(0, self.filename)
        self.to_list.insert(1, len(self.to_list))
        return self.to_list # теперь файл возвращается не объектом, а списком со служ. инфой

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileToList('1.txt', 'r') as file1:
    list_list.append(file1)

with FileToList('2.txt', 'r') as file2:
    list_list.append(file2)

with FileToList('3.txt', 'r') as file3:
    list_list.append(file3)

print(list_list)

def sort_by_length(list_to_sort):
    dict_to_sort = {}
    for list in list_to_sort:
        dict_to_sort[len(list)] = list
    outp_dict = dict(sorted(dict_to_sort.items()))
    return outp_dict

dict_to_write = sort_by_length(list_list)


with open('output.txt', 'a', encoding='utf-8') as output:
    for item in dict_to_write.values():
        for line in item:
            input_text = str(line)
            output.write(input_text + '\n')
