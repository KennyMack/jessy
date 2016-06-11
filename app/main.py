#!/usr/bin/python3
from core import app as a

def main():
	app = a.Application('app.json')
	app.loadEnv()
	print('hello')

if __name__ == '__main__':
	main()
