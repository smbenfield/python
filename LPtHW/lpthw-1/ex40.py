#!/usr/bin/python

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

smoke = Song(["Let's get covered in flames,",
			  "And play some games with the smoke"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

smoke.sing_me_a_song()