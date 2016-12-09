# Geo-Localization

This is a simple python script which implements a class with methods for trilateration of 2D points in the real world, returning their geodetic coordinates.
You must provide (as a list) the real line-of-sight distances from your fixed points to the target point.

## Usage

To use it in your python script, just import the geoloc file and instantiate the Trilateration class.

### Example

```python
from geoloc import Trilateration

dist1 = 1   # First measured distance 
dist2 = 2   # Second measured distance
dist3 = 1   # Third measured distance

trilat = Trilateration()

print "Trilaterated point:", trilat.get_point( (dist1, dist2, dist3) )
```

There is also an example method in the class, which trilaterates the position of a known point.
The euclidean distance between the real an trilaterated points is approximately 20 cm.

To change the fixed points, use the "set_fixed_points" method.

## Explanation

The script performs trilateration by using the methods described in the sources below.
The process can be separated in three steps:

* Convert your fixed points' coordinates from geodetic to ECEF [1].

* Define one of your points as the datum (reference) and offset all other points.

* Align the X axis of the new reference system with a second point.

* Find the (x,y) coordinates of the target point following the equations in [2], ignoring z for a 2D point.

* Offset the point back.

* Convert from ECEF back to geodetic.

## Sources
[1] - http://mathforum.org/library/drmath/view/51832.html
[2] - https://en.wikipedia.org/wiki/Trilateration