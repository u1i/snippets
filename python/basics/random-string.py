import random, string

# random string: uppercase, lowercase and digits

len=16
res=""

for _ in range(len):
	res += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

print res
