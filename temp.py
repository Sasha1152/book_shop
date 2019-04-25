def foo(*args):
	if args:
		print(args)
	else:
		print('nothing')

foo()
foo(2, 3, 4)