import ngejawi

while True:
	text = input('ngejawi > ')
	result, error = ngejawi.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)

