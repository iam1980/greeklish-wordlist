#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# pygr2gl - greek text to greeklish converter written in Python.
#
# Author  : George Notaras <George[D.O.T]Notaras[A.T]gmail[D.O.T]com>
# Homepage: http://www.g-loaded.eu/2006/12/18/pygr2gl-greek-to-greeklish-converter/
# Licence : GPLv2
#
#
# Accepts data either from stdin or by reading the specified file.
# Supports UTF-8, ISO8859-7 and probably Windows-1253.
# Two sample text files test_utf-8.txt and test_iso8859-7.txt are included in
# the distribution.
#
# Usage:
# ./pygr2gl test_utf-8.txt
# cat test_iso8859-7.txt | ./pygr2gl
#
# Greeklish text is printed to stdout.
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the:
#
# Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston,
# MA 02111-1307  USA
#

__version__ = "0.1"

import sys, os.path

def get_conversion_pool():
	poolGR = u"αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩςάέήίϊΐόύϋΰώΆΈΉΊΪΌΎΫΏ"
	poolGL =  "abgdezi8hklmn3oprstyfx4oABGDEZH8IKLMN3OPRSTYFX4OsaeiiiioiiioAEHIIOYYO"
	return dict(zip(poolGR, poolGL))

def get_decoded_input(line):
	try:
		line = line.decode("utf-8")
	except UnicodeDecodeError:
		line = line.decode("iso8859-7")
	return line

def convert(datasource):
	pool = get_conversion_pool()
	for line in datasource:
		#line = get_decoded_input(line)

		trans = line.replace(u'αυ', 'au')

		sys.stdout.write(trans)
		sys.stdout.flush()

def usage():
	print "pygr2gl - Converts greek text to greeklish."
	print "Usage: %s [filename]" % sys.argv[0]
	print "If \"filename\" is not specified, data from stdin is expected."
	print "Use the -h or --help switch for this help message."
	sys.exit(1)

def main():
	if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) > 2:
		usage()
	elif len(sys.argv) == 2:
		if os.path.exists(sys.argv[1]):
			datasource = open(sys.argv[1])
		else:
			print "error: cannot read file: %s" % sys.argv[1]
			sys.exit(1)
	else:
		datasource = sys.stdin
	try:
		convert(datasource)
	except KeyboardInterrupt:
		print "Terminated by user."
		sys.exit(1)

if __name__ == '__main__':
	main()

