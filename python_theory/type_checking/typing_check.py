from classA import A
from classB import B

# Create an instance of B, initially with no A object
b_instance = B(None)

# Create an instance of A, passing the instance of B
a_instance = A(b_instance)

# Now, set the A object in b_instance
b_instance.A_obj = a_instance

# a_instance and b_instance are now instances of A and B, respectively, and know about each other

