# bounce.py

height = 100
for bounce in range(1, 11):
    height *= 3/5
    print(bounce, round(height, 4))
