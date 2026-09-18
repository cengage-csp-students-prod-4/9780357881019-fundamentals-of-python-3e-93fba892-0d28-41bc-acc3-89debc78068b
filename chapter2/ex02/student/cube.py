"""
Program: Surface Area of a Cube
--------------------------------
Analysis:
This program calculates the total surface area of a cube based on
the length of one edge, entered by the user.

A cube has 6 equal square faces, so the surface area formula is:
    Surface Area = 6 * (edge length)^2

How it works:
1. Prompt the user to enter the cube's edge length (Length).
   - input() returns a string, so int() converts it to an integer
     for use in calculations.
2. Calculate the surface area:
   - Square the edge length (Length * Length) to get the area of
     one face.
   - Multiply by 6 (the number of faces on a cube) to get the
     total surface area.
3. Print the result:
   - str() converts the numeric result back to a string so it can
     be combined with the empty strings and printed.
   - Note: the empty strings ("" + ... + "") don't change the
     output; print(Surface_Area) alone would do the same thing.

Example:
    Input:  edge = 4
    Output: 96   (since 4*4 = 16, and 16*6 = 96)
"""
Input= int(input("enter cube's edge: "))
Output= (Input*Input)*6
print("The surface area is "+str(Output)+" square units")