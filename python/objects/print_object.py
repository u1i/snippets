# print an object in Python

for key in dir(my_obj):
	print('{}: {}'.format(key, getattr(my_obj, key)))
