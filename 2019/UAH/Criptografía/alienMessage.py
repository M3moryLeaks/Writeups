#!/usr/bin/python3

from PIL import Image
from string import ascii_lowercase


def search(img, start_x, start_y, need_color, fix_x = False, fix_y = False):
	found = False
	for y in range(start_y, img.height) if not fix_y else [start_y]:
		for x in range(start_x, img.width) if not fix_x else [start_x]:
			color = (img.getpixel((x, y)) == 0)
			if (color and need_color) or (not color and not need_color):
				found = True
				break
		if found:
			break

	if found:
		return (x,y)
	else:
		return (None, None)


def bfs(img, start_x, start_y):
	queue = [(start_x, start_y)]
	visited = set(queue)
	for x, y in queue:
		for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
			xx, yy = x + dx, y + dy
			if img.getpixel((xx, yy)) > 0:
				continue
			if (xx, yy) not in visited:
				queue.append((xx, yy))
				visited.add((xx, yy))
	return visited


# search google : python zip(*list)
def bounds(letter):
	x, y = zip(*list(letter))
	min_x, min_y = min(x), min(y)
	max_x, max_y = max(x), max(y)
	return (min_x, min_y), (max_x, max_y)


def normalize(letter):
	(min_x, min_y), (max_x, max_y) = bounds(letter)
	normal = set()
	for x, y in letter:
		xx, yy = x - min_x, y - min_y
		normal.add((xx, yy))
	return frozenset(normal)

def scan(img):
	lines = []
	line_x, line_y = 30, 0
	while True:
		x, y = search(img, line_x, line_y, True, fix_x=True)
		if (x, y)==(None, None): break
		line = []
		while True:
			x, y = search(img, x, y, True, fix_y=True)
			if (x, y)==(None, None): break
			letter = bfs(img, x, y)
			line.append(normalize(letter))
			(min_x, min_y), (max_x, max_y) = bounds(letter)
			x = max_x + 1
			y = (max_y + min_y) // 2
		lines.append(line)
		line_y = max_y + 30
	return lines


def translate(lines):
	alpha = dict()
	index = 0
	text = ''
	for line in lines:
		for letter in line:
			if letter not in alpha:
				alpha[letter] = ascii_lowercase[index]
				index += 1
			text += alpha[letter]
		text += '\n'
	return text


def main():
	img = Image.open('alienMessage.png').convert('1', dither=False)
	lines = scan(img)
	print(translate(lines))

if __name__ == '__main__':
	main()
