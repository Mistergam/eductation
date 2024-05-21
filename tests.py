x = input()
y = 'abcdefghijklmnopqrstuvwxyz'
input_text = input().lower()
trl = input_text.maketrans(y, x)
print(input_text.translate(trl))
