#!/usr/bin/env python3

import eventlet
eventlet.monkey_patch()

import web

def main():
	web.app.main()

if __name__ == '__main__':
	main()
