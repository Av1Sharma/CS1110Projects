"""
Test script for Assignment A4

This test script is different from previous test scripts, because the output of 
the functions in A4 is graphical. We cannot use assert_equals to verify that the 
turtle is drawing correctly. Instead, we have to let the Turtle draw, look at 
the result, and manually verify that they are correct. Hence the test procedures 
for A4 are procedures that draw one or more pictures using the function being 
tested.

However, there are some things that we can test automatically. Many of the 
functions in A4 require that we restore the state of a turtle when we are done. 
We can use assert_equals to verify that these values are properly restored. We 
can also use the function assert_error to verify that a precondition is being 
enforced (e.g. an error is raised if the precondition is violated). There are 
examples of both of these in this file.

This is an EXTREMELY incomplete test script. We do not guarantee that we have 
tested all possibilities for all functions (and in some cases have intentionally 
avoided doing so). Passing this script is not a guarantee that you will get a 
perfect on the assignment. It is up to you add more tests to ensure that your 
A4 functions are complete and correct.

With that said, you will not be submitting this file as part of the assignment.
We have provided it simply as a convenience.

Author: Walker M. White (wmw2)
Date: Oct 13, 2026
"""
import a4
import introcs
from introcs.turtle import Window, Turtle, Pen


#################### DEMO: Two lines ####################

def test_draw_two_lines(w,sp):
    """
    Tests the procedure draw_two_lines
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing draw_two_lines')
    
    # First verify that the preconditions are enforced
    introcs.assert_error(a4.draw_two_lines,'window',sp)
    introcs.assert_error(a4.draw_two_lines,w,-1)
    introcs.assert_error(a4.draw_two_lines,w,str(sp))
    
    a4.draw_two_lines(w,sp)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### TASK 1: Triangle ####################

def test_draw_triangle(w,sp):
    """
    Tests the procedure draw_triangle
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing draw_triangle')
    w.clear()
    turt = Turtle(w)
    turt.speed = sp
    
    # First verify that the preconditions are enforced
    turt.drawmode = False
    introcs.assert_error(a4.draw_triangle,turt,50,'orange')
    turt.drawmode = True
    introcs.assert_error(a4.draw_triangle,turt,'50','orange')
    introcs.assert_error(a4.draw_triangle,turt,-50,'orange')
    introcs.assert_error(a4.draw_triangle,turt,-50,'orangy')
    
    # Store original values (These are all of the important ones)
    oldx = turt.x
    oldy = turt.y
    oldang  = turt.heading % 360
    oldcol  = turt.color
    oldmode = turt.drawmode
    
    # Now draw
    a4.draw_triangle(turt,50,'orange')
    
    # Verify value restored
    introcs.assert_floats_equal(oldx,turt.x)
    introcs.assert_floats_equal(oldy,turt.y)
    introcs.assert_floats_equal(oldang,turt.heading  % 360) # Okay if 360 was added
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### TASK 2: Hexagon ####################

def test_draw_hex(w,sp):
    """
    Tests the procedure draw_hex
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing draw_hex')
    w.clear()
    turt = Turtle(w)
    turt.speed = sp
    
    # First verify that the preconditions are enforced
    turt.drawmode = False
    introcs.assert_error(a4.draw_hex,turt,50)
    turt.drawmode = True
    introcs.assert_error(a4.draw_hex,turt,'50')
    introcs.assert_error(a4.draw_hex,turt,-50)
    
    # Store original values (These are all of the important ones)
    oldx = turt.x
    oldy = turt.y
    oldang  = turt.heading % 360
    oldcol  = turt.color
    oldmode = turt.drawmode
    
    # Now draw
    a4.draw_hex(turt,50)
    
    # Verify value restored
    introcs.assert_floats_equal(oldx,turt.x)
    introcs.assert_floats_equal(oldy,turt.y)
    introcs.assert_floats_equal(oldang,turt.heading % 360) # Okay if 360 was added
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### Task 3A: Spirals ####################

def test_draw_spiral(w,sp):
    """
    Tests the procedure draw_spiral AND draw_spiral_helper
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing draw_spiral')
    # This is only ONE TEST. Feel free to change the values for different tests.
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    introcs.assert_error(a4.draw_spiral,'window',1,24,64,sp)
    introcs.assert_error(a4.draw_spiral,w,'1',24,64,sp)
    introcs.assert_error(a4.draw_spiral,w,-1,24,64,sp)
    introcs.assert_error(a4.draw_spiral,w,1,24,64.3,sp)
    introcs.assert_error(a4.draw_spiral,w,1,24,0,sp)
    introcs.assert_error(a4.draw_spiral,w,1,24,64,str(sp))
    introcs.assert_error(a4.draw_spiral,w,1,24,64,-1)
    
    # Now draw
    a4.draw_spiral(w, 1, 24, 64, sp)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')
    
    print('Testing draw_spiral_helper')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    turt = Turtle(w)
    turt.color = 'blue'
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    turt.drawmode = False
    introcs.assert_error(a4.draw_spiral_helper,turt,20,90,6,sp)
    turt.drawmode = True
    introcs.assert_error(a4.draw_spiral_helper,turt,'20',90,6,sp)
    introcs.assert_error(a4.draw_spiral_helper,turt,-1,90,6,sp)
    introcs.assert_error(a4.draw_spiral_helper,turt,20,90,6.3,sp)
    introcs.assert_error(a4.draw_spiral_helper,turt,20,90,0,sp)
    introcs.assert_error(a4.draw_spiral_helper,turt,20,90,6,str(sp))
    introcs.assert_error(a4.draw_spiral_helper,turt,20,90,6,-1)
    
    # Store original values (These are all of the important ones)
    oldcol  = turt.color
    oldvis  = turt.visible
    oldspd  = turt.speed
    oldmode = turt.drawmode
    
    # Now draw
    a4.draw_spiral_helper(turt, 20, 90, 6, sp)
    
    # Verify value restored
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldvis,turt.visible)
    introcs.assert_equals(oldspd,turt.speed)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### TASK 3B: Polygon Vortex ####################

def test_draw_vortex(w,sp):
    """
    Tests the procedure draw_vortex AND draw_vortex_helper
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing draw_vortex')
    # This is only ONE TEST. Feel free to change the values for different tests.
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    introcs.assert_error(a4.draw_vortex,'window', 100, 300, 5, 20, sp)
    introcs.assert_error(a4.draw_vortex, w, '100', 300, 5, 20, sp)
    introcs.assert_error(a4.draw_vortex, w, -1, 300, 5, 20, sp)
    introcs.assert_error(a4.draw_vortex, w, 100, '300', 5, 20, sp)
    introcs.assert_error(a4.draw_vortex, w, 100, -1, 5, 20, sp)
    introcs.assert_error(a4.draw_vortex, w, 100, 300, 5, 20, str(sp))
    introcs.assert_error(a4.draw_vortex, w, 100, 300, 5, 20,-1)
    
    # Now draw
    a4.draw_vortex(w, 100, 300, 5, 20, sp)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')
    
    print('Testing draw_vortex_helper')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    turt = Turtle(w)
    turt.color = 'blue'
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    turt.drawmode = False
    introcs.assert_error(a4.draw_vortex_helper, turt, 60, 120, 7, 6, sp)
    turt.drawmode = True
    introcs.assert_error(a4.draw_vortex_helper, turt, '60', 120, 7, 6, sp)
    introcs.assert_error(a4.draw_vortex_helper, turt, -1, 120, 7, 6, sp)
    introcs.assert_error(a4.draw_vortex_helper, turt, 60, '120', 7, 6, sp)
    introcs.assert_error(a4.draw_vortex_helper, turt, 60, -1, 7, 6, sp)
    introcs.assert_error(a4.draw_vortex_helper, turt, 60, 120, 7, 6, str(sp))
    introcs.assert_error(a4.draw_vortex_helper, turt, 60, 120, 7, 6, -1)
    
    # Store original values (These are all of the important ones)
    oldx = turt.x
    oldy = turt.y
    oldang  = turt.heading % 360
    oldcol  = turt.color
    oldvis  = turt.visible
    oldspd  = turt.speed
    oldmode = turt.drawmode
    
    # Now draw
    a4.draw_vortex_helper(turt, 60, 120, 7, 6, sp)
    
    # Verify value restored
    introcs.assert_floats_equal(oldx,turt.x)
    introcs.assert_floats_equal(oldy,turt.y)
    introcs.assert_floats_equal(oldang,turt.heading % 360) # Okay if 360 was added
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldvis,turt.visible)
    introcs.assert_equals(oldspd,turt.speed)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### TASK 3C: Radiating Lines ####################

def test_radiate(w,sp):
    """
    Tests the procedure radiate AND radiate_helper
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the 
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    print('Testing radiate')
    # This is only ONE TEST. Feel free to change the values for different tests.
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    introcs.assert_error(a4.radiate, 'window', 250, 45, sp)
    introcs.assert_error(a4.radiate, w, '250', 45, sp)
    introcs.assert_error(a4.radiate, w, -1, 45, sp)
    introcs.assert_error(a4.radiate, w, 250, 45, str(sp))
    introcs.assert_error(a4.radiate, w, 250, 45, -1)
    
    # Now draw
    a4.radiate(w, 250, 45, sp)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')
    
    print('Testing radiate_helper')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    turt = Turtle(w)
    turt.color = 'red'
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    turt.drawmode = False
    introcs.assert_error(a4.radiate_helper, turt, 150, 4, sp)
    turt.drawmode = True
    introcs.assert_error(a4.radiate_helper, turt, '150', 4, sp)
    introcs.assert_error(a4.radiate_helper, turt, -1, 4, sp)
    introcs.assert_error(a4.radiate_helper, turt, 150, 4, str(sp))
    introcs.assert_error(a4.radiate_helper, turt, 150, 4, -1)
    
    # Store original values (These are all of the important ones)
    oldcol  = turt.color
    oldvis  = turt.visible
    oldspd  = turt.speed
    oldmode = turt.drawmode
    
    # Now draw
    a4.radiate_helper(turt, 150, 4, sp)
    
    # Verify value restored
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldvis,turt.visible)
    introcs.assert_equals(oldspd,turt.speed)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### TASK 4A: Vicsek Fractal ####################

def test_vicsek(w,sp):
    """
    Tests the procedure vicsek AND vicsek_helper
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    # Fractals need a few tests
    print('Testing vicsek (depth 0)')
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    introcs.assert_error(a4.vicsek,'window', 300, 0, sp)
    
    # Now draw (three different depths)
    a4.vicsek(w, 300, 0, sp)
    input('Press [return]')
    
    print('Testing vicsek (depth 1)')
    a4.vicsek(w, 300, 1, sp)
    input('Press [return]')

    print('Testing vicsek (depth 3)')
    a4.vicsek(w, 300, 3, sp)
    input('Press [return]')
    
    print('Testing vicsek_helper')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    pen = Pen(w)
    pen.fillcolor = 'blue'
    pen.edgecolor = 'blue'
    pen.speed = sp
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    pen.solid = True
    introcs.assert_error(a4.vicsek_helper, pen, 0, 0, 243, 4)
    pen.solid = False
    
    # Now draw
    a4.vicsek_helper(pen, 0, 0, 243, 4)
    pen.flush()
    input('Press [return]')


#################### TASK 4B: Hexaflake ####################

def test_hexaflake(w,sp):
    """
    Tests the procedure hexaflake AND hexaflake_helper
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    # Fractals need a few tests
    print('Testing hexaflake (depth 0)')
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    introcs.assert_error(a4.hexaflake,'window', 300, 0, sp)
    
    # Now draw (three different depths)
    a4.hexaflake(w, 300, 0, sp)
    input('Press [return]')
    
    print('Testing hexaflake (depth 1)')
    a4.hexaflake(w, 300, 1, sp)
    input('Press [return]')
    
    print('Testing hexaflake (depth 2)')
    a4.hexaflake(w, 300, 2, sp)
    input('Press [return]')
    
    print('Testing hexaflake (depth 3)')
    a4.hexaflake(w, 300, 3, sp)
    input('Press [return]')
    
    print('Testing hexaflake_helper')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    pen = Pen(w)
    pen.fillcolor = 'sky blue'
    pen.edgecolor = 'grey'
    pen.speed = sp
    pen.visible = False
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    pen.solid = True
    introcs.assert_error(a4.hexaflake_helper, pen, 0, 0, 243, 4)
    pen.solid = False
    
    # Now draw
    a4.hexaflake_helper(pen, 0, 0, 243, 4)
    pen.flush()
    input('Press [return]')


#################### TASK 5: Koch Snowflake ####################

def test_kochflake(w,sp):
    """
    Tests the procedure kochflake AND kochflake_edge
    
    Unlike most test procedures, you will notice that this test procedure has 
    parameters. That is because we want all of our test procedures to share the
    same drawing window and same drawing speed. Theses are set in the master 
    procedure test_all.
    
    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.
    
    Parameter sp: The drawing speed.
    Precondition: sp is a valid drawing speed (int 0..10).
    """
    # Fractals need a few tests
    print('Testing snowflake (depth 0)')
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    introcs.assert_error(a4.kochflake, 'snowflake', 300, 0, sp)
    
    # Now draw (three different depths)
    a4.kochflake(w, 300, 0, sp)
    input('Press [return]')
    
    print('Testing snowflake (depth 1)')
    a4.kochflake(w, 300, 1, sp)
    input('Press [return]')
    
    print('Testing snowflake (depth 3)')
    a4.kochflake(w, 300, 3, sp)
    input('Press [return]')
    
    print('Testing snowflake_edge')
    # This is only ONE TEST. Feel free to change the values for different tests.
    w.clear()
    turt = Turtle(w)
    turt.move(-200,0)
    turt.color = 'blue'
    turt.speed = sp
    
    # First verify that the preconditions are enforced
    # WE HAVE NOT ADDED ALL OF THEM. YOU MAY NEED TO ADD SOME
    turt.drawmode = False
    introcs.assert_error(a4.kochflake_edge, turt, 400, 5)
    turt.drawmode = True
    
    # Store original values (These are all of the important ones)
    oldx = turt.x
    oldy = turt.y
    oldang  = turt.heading % 360
    oldcol  = turt.color
    oldvis  = turt.visible
    oldspd  = turt.speed
    oldmode = turt.drawmode
    
    # Now draw
    a4.kochflake_edge(turt, 400, 5)
    turt.flush()
    
    # Verify value restored
    introcs.assert_equals(oldcol, turt.color)
    introcs.assert_equals(oldvis,turt.visible)
    introcs.assert_equals(oldspd,turt.speed)
    introcs.assert_equals(oldmode,turt.drawmode)
    
    # Allow the user to look at the picture before continuing
    input('Press [return]')


#################### Main Test Procedure ####################

def get_speed():
    """
    Returns the answer to a prompt about the speed.
    
    If the anwser is invalid, it returns the value 10
    """
    ans = input('Enter the drawing speed [0..10]: ')
    try:
        return int(ans.strip())
    except:
        print('Answer '+repr(ans)+' is invalid. Using speed 10.')
        return 10


def test_all():
    """
    Tests all of the drawing functions in a4.
    
    This is the master test procedure.  It creates a drawing window and sets the 
    drawing speed for all of the tests.
    
    If you want to disable a test (because the turtle is not very fast, and so 
    you do not want to keep drawing the same things), comment it out in the code 
    below.
    """
    print('Testing module a4')
    w  = Window()
    sp = get_speed()
    
    # # Test procedures. Comment out a test to skip it.
    # test_draw_two_lines(w,sp)
    
    # test_draw_triangle(w,sp)
    # test_draw_hex(w,sp)
    
    test_draw_spiral(w,sp)
    # test_draw_vortex(w,sp)
    # test_radiate(w,sp)
    
    # test_vicsek(w,sp)
    # test_hexaflake(w,sp)
    
    # test_kochflake(w,sp)
    
    print('Testing complete')


if __name__ == '__main__':
    test_all()