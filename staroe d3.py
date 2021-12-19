from datetime import datetime
from decorator import file_path

my_file_path = file_path("D:\decorator\logs.txt")

@my_file_path
def flat_generator(list):
        for search in list:
            for search_2 in search:
                part = search_2
                yield part

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
if __name__ == '__main__':
    for item in  flat_generator(nested_list):
        print(item)
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)