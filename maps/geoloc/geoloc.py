#!/usr/bin/env python

import math
import numpy as np

class Trilaterate():
	def __init__(self):
		'''
		Constuctor

		Constants:
		(a, b, c) - Fixed points for trilateration 
		earthR - Radius of the Earth
		'''
		self.a = (-30.060275, -51.173556)
		self.b = (-30.060179, -51.173658)
		self.c = (-30.060258, -51.173651)
		self.earthR = 6371	#assuming elevation = 0

	def set_fixed_points(points):
		'''
		Method for changing the fixed points in trilateration

		Arguments:
		points - Tuple with the (lat, lon) of each point
		'''
		self.a = points[0]
		self.b = points[1]
		self.c = points[2]

	def eucl(self, a,b):
		'''
		Returns the euclidean distance between two points

		Arguments:
		a, b - Points in space (2D)

		Returns:
		Euclidean distance between a and b
		'''
		return np.sqrt(np.abs(a[0]-b[0])**2+np.abs(a[1]-b[1])**2)

	def latlon_to_ecef(self, point):
		'''
		Converts a point from geodesic to ECEF coordinates
		(ECEF - https://en.wikipedia.org/wiki/ECEF)

		Arguments:
		point - Geodesic point to be converted

		Returns:
		Tuple with converted point (in ECEF)
		'''

		#using authalic sphere
		#if using an ellipsoid this step is slightly different
		#Convert geodetic Lat/Long to ECEF xyz
		#   1. Convert Lat/Long to radians
		#   2. Convert Lat/Long(radians) to ECEF
		x = self.earthR *(math.cos(math.radians(point[0])) * math.cos(math.radians(point[1])))
		y = self.earthR *(math.cos(math.radians(point[0])) * math.sin(math.radians(point[1])))
		z = self.earthR *(math.sin(math.radians(point[0])))
		return (x,y,z)

	def get_point(self, dists):
		'''
		Trilaterates a point in (latitude, longitude) coordinates from 3 other known points.
		(http://gis.stackexchange.com/questions/66/trilateration-using-3-latitude-and-longitude-points-and-3-distances)
		(https://en.wikipedia.org/wiki/Trilateration)

		Arguments:
		dists - Tuple of the distances from the points (in km) to the target point

		Returns:
		Tuple of geodesic coordinates for the target point
		'''

		pA, pB, pC = self.a, self.b, self.c
		xA, yA, zA = self.latlon_to_ecef(pA)
		xB, yB, zB = self.latlon_to_ecef(pB)
		xC, yC, zC = self.latlon_to_ecef(pC)

		P1 = np.array([xA, yA, zA])
		P2 = np.array([xB, yB, zB])
		P3 = np.array([xC, yC, zC])

		# from wikipedia
		# transform to get circle 1 at origin
		# transform to get circle 2 on x axis
		ex = (P2 - P1)/(np.linalg.norm(P2 - P1))
		i = np.dot(ex, P3 - P1)
		ey = (P3 - P1 - i*ex)/(np.linalg.norm(P3 - P1 - i*ex))
		ez = np.cross(ex,ey)
		d = np.linalg.norm(P2 - P1)
		j = np.dot(ey, P3 - P1)

		# from wikipedia
		# plug and chug using above values
		x = (pow(dists[0],2) - pow(dists[1],2) + pow(d,2))/(2*d)
		y = ((pow(dists[0],2) - pow(dists[2],2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x)
		
		# triPt is an array with ECEF x,y of trilateration point
		triPt = P1 + x*ex + y*ey

		# convert back to lat/long from ECEF
		# convert to degrees
		lat = math.degrees(math.asin(triPt[2] / self.earthR))
		lon = math.degrees(math.atan2(triPt[1],triPt[0]))

		return (lat, lon)

	def example(self):
		# Distances to target (circle radiuses for trilateration)
		dist_a, dist_b, dist_d = 12.693/1000, 2.285/1000, 5.771/1000

		target = (-30.060202, -51.173660)
		print "\nTarget point is:\n\t", target, " (latitutde, longitude)\n"

		print "Trilaterating from points:"
		print "\ta:", self.a, "\n\tb:", self.b, "\n\tc:", self.c

		trilaterated = self.get_point((dist_a, dist_b, dist_d))
		print "\nTrilaterated coordinates:\n\t", trilaterated

		miss = self.eucl(self.latlon_to_ecef(trilaterated), self.latlon_to_ecef(target))*1000
		print "\nTrilaterated point is off by", miss, "meters"
