"""
Program: Surface Area of a Cube
--------------------------------
Analysis:
This program calculates the total surface area of a cube based on
the length of one edge, entered by the user.

A cube has 6 equal square faces, so the surface area formula is:
    Surface Area = 6 * (edge length)^2

How it works:
1. Prompt the user to enter the cube's edge length (Input).
   - input() returns a string, so int() converts it to an integer
     for use in calculations.
2. Calculate the surface area:
   - Square the edge length (Input * Input) to get the area of
     one face.
   - Multiply by 6 (the number of faces on a cube) to get the
     total surface area, stored in Output.
3. Print the result:
   - str() converts the numeric result back to a string so it can
     be combined with the surrounding text.
   - The message is built by joining three pieces: "The surface
     area is ", the value of Output, and " square units".

Example:
    Input:  edge = 4
    Output: The surface area is 96 square units
    (since 4*4 = 16, and 16*6 = 96)
"""
Input= int(input("enter cube's edge: "))
Output= (Input*Input)*6
print("The surface area is "+str(Output)+" square units")