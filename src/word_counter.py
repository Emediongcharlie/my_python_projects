from collections import Counter

#def count_words(numbers):
values = [2, 3, 5, 3, 3, 2, 5]
# # Counter = Counter(values.)
#
# counter = Counter()
# for key in values:
#  #   print(counter)
#      counter[key] += 1
#  print(counter[key])
count = {}
# for key in Counter(values):
#     print(f'{key:}')

def number_count():
    for keys in values:
        if keys in count and count[keys]:
            count[keys] = count[keys] + 1
        else:
            count[keys] = 1

        return count;

 print(count)

