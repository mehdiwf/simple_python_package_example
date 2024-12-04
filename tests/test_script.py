import example_package_mifz as e

# this should print "hello!"
e.printmod.say_hello()

two = e.mymath.addone.add_one(1)
# this should print "2"
print(two)

v = e.my2Dvec.My2DVector(2, 0)
# should print "vector: x= 2 , y= 0"
v.show()

v.normalize()
# should print "vector: x= 1.0 , y= 0.0"
v.show()
