#!/usr/bin/env python

import yaml
import geoloc

#Instantiate trilaterator class
locator = geoloc.Trilaterate()

#Old fixed points
a = (-30.060202, -51.173660)
b = (-30.060226, -51.173664)
c = (-30.060276, -51.173556)
locator.set_fixed_points( (a, b, c) )

#Trilaterate new fixed points
a1, a2, a3 = 7.33/1000, 7.157/1000, 18.582/1000
b1, b2, b3 = 11.804/1000, 12.731/1000, 24.304/1000
c1, c2, c3 = 12.810/1000, 11.256/1000, 20.016/1000

A = locator.get_point((a1, a2, a3))
B = locator.get_point((b1, b2, b3))
C = locator.get_point((c1, c2, c3))

#Set new fixed points
locator.set_fixed_points((A, B, C))

#Virtual arena delimiters
p1a, p1b, p1c = 6.249/1000, 1.886/1000, 10.874/1000
p2a, p2b, p2c = 26.746/1000, 22.888/1000, 26.013/1000 
p3a, p3b, p3c = 26.362/1000, 23.620/1000, 24.446/1000
p4a, p4b, p4c = 20.643/1000, 18.149/1000, 19.097/1000
p5a, p5b, p5c = 17.114/1000, 15.204/1000, 15.321/1000
p6a, p6b, p6c = 10.213/1000, 9.853/1000, 8.811/1000
p7a, p7b, p7c = 5.553/1000, 7.757/1000, 5.150/1000

#Obstacles
wellA, wellB, wellC = 5.553/1000, 7.757/1000, 5.150/1000
postA, postB, postC = 9.883/1000, 9.349/1000, 9.201/1000
treeA, treeB, treeC = 17.613/1000, 15.384/1000, 16.352/1000

#Write it all in a text file
f = open("virtual_arena/virtual_arena.txt", "w")

#Trilaterations
#Virtual arena
p1 = locator.get_point((p1a, p1b, p1c))
p2 = locator.get_point((p2a, p2b, p2c))
p3 = locator.get_point((p3a, p3b, p3c))
p4 = locator.get_point((p4a, p4b, p4c))
p5 = locator.get_point((p5a, p5b, p5c))
p6 = locator.get_point((p6a, p6b, p6c))
p7 = locator.get_point((p7a, p7b, p7c))

f.write("\nVirtual Arena:")
f.write("\n\tGlobal Coordinates:")
f.write("\n\t\tP0:\t-30.0602102056,-51.1738922207")
f.write("\n\t\tP1:\t" + str(p1[0]) + "," + str(p1[1]))
f.write("\n\t\tP2:\t" + str(p2[0]) + "," + str(p2[1]))
f.write("\n\t\tP3:\t" + str(p3[0]) + "," + str(p3[1]))
f.write("\n\t\tP4:\t" + str(p4[0]) + "," + str(p4[1]))
f.write("\n\t\tP5:\t" + str(p5[0]) + "," + str(p5[1]))
f.write("\n\t\tP6:\t" + str(p6[0]) + "," + str(p6[1]))
f.write("\n\t\tP7:\t" + str(p7[0]) + "," + str(p7[1]))

f.write("\n\tLocal Coordinates (relative to P0):")
f.write("\n\t\tP0:\t0.0,\t\t0.0")
with open("../../settings/minefield.yaml", "r") as stream:
		yaml_minefield = yaml.load(stream)
		mf_corners = yaml_minefield['minefield']
		for i in range(1, len(mf_corners)+1):
			corner_name = "corner{}".format(i)
			f.write("\n\t\tP{}:\t{},\t{}".format(i, mf_corners[corner_name]['latitude'], mf_corners[corner_name]['longitude']))

#Obstacles
well = locator.get_point((wellA, wellB, wellC))
post = locator.get_point((postA, postB, postC))
tree = locator.get_point((treeA, treeB, treeC))

f.write("\n\nObstacles:")
f.write("\n\tGlobal Coordinates:")
f.write("\n\t\tWell: " + str(well[0]) + "," + str(well[1]))
f.write("\n\t\tPost: " + str(post[0]) + "," + str(post[1]))
f.write("\n\t\tTree: " + str(tree[0]) + "," + str(tree[1]))
f.write("\n\tLocal Coordinates (relative to P0):")
f.write("\n\t\tWell: 10.8414412908,-2.0325296335")
f.write("\n\t\tPost: 6.6759533706,\t-1.1691806717")
f.write("\n\t\tTree: -1.1745529239,-0.6197298011")

f.write("\n\nNOTE: P7 = Well")
f.write("\nNOTE: P0 = Center")

f.close()
