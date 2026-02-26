#Use filter() to select names with 7 or fewer characters from the list.
#Expected Output: ['olumide', 'josiah', 'omoseun']

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
result = list(filter(lambda name: len(name) <= 7, my_names))

print(result)