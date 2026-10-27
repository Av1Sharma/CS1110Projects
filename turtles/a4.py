"""
A module to draw cool shapes with the introcs Turtle.

Use a4test.py to show and test the drawing functions.

Avi Sharma (as4632)
October 21, 2026
Implementation assistance: OpenAI Codex.
"""
from introcs.turtle import Window, Turtle, Pen
import introcs  # For the RGB (color) objects
import math     # For the math computations


################# Helpers for Precondition Verification #################

def is_number(x):
    """
    Returns: True if value x is a number; False otherwise.

    Parameter x: the value to check
    Precondition: NONE (x can be any value)
    """
    return type(x) in [float, int]


def is_window(w):
    """
    Returns: True if w is a introcs Window; False otherwise.

    Parameter w: the value to check
    Precondition: NONE (w can be any value)
    """
    return type(w) == Window


def is_valid_color(c):
    """
    Returns: True c is a valid turtle color; False otherwise

    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    if type(c) == str:
        return introcs.is_tkcolor(c) or introcs.is_webcolor(c)
    # else
    return type(c) == introcs.RGB or type(c) == introcs.HSL


def is_valid_speed(sp):
    """
    Returns: True if sp is an int in range 0..10; False otherwise.

    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)
    """
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """
    Returns: True if side is a number >= 0; False otherwise.

    Parameter side: the value to check
    Precondition: NONE (side can be any value)
    """
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """
    Returns: True if n is an int >= 1; False otherwise.

    Parameter n: the value to check
    Precondition: NONE (n can be any value)
    """
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """
    Returns: True if d is an int >= 0; False otherwise.

    Parameter d: the value to check
    Precondition: NONE (d can be any value)
    """
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """
    Returns: True t is a Turtle with drawmode True; False otherwise.

    Parameter t: the value to check
    Precondition: NONE (t can be any value)
    """
    return (type(t) == Turtle and t.drawmode)


def is_valid_penmode(p):
    """
    Returns: True t is a Pen with solid False; False otherwise.

    Parameter p: the value to check
    Precondition: NONE (p can be any value)
    """
    return (type(p) == Pen and not p.solid)


def report_error(message, value):
    """
    Returns: An error message about the given value.

    This is a function for constructing error messages to be used in assert
    statements. We find that students often introduce bugs into their assert
    statement messages, and do not find them because they are in the habit of
    not writing tests that violate preconditions.

    The purpose of this function is to give you an easy way of making error
    messages without having to worry about introducing such bugs. Look at  the
    function draw_two_lines for the proper way to use it.

    Parameter message: The error message to display
    Precondition: message is a string

    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)
    """
    return message+': '+repr(value)




#################### DEMO: Two lines ####################

def draw_two_lines(w,sp):
    """
    Draws two lines on to window w.

    This function clears w of any previous drawings. Then, in the middle of the
    window w, this function draws a green line 100 pixels to the east, and then
    a blue line 200 pixels to the north. It uses a new turtle that moves at
    speed sp, 0 <= sp <= 10, with 1 being slowest and 10 fastest (and 0 being
    "instant").

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)

    # Clear the window first!
    w.clear()

    # Create a turtle and draw
    t = Turtle(w)
    t.speed = sp
    t.color = 'green'
    t.forward(100) # draw a line 100 pixels in the current direction
    t.left(90)     # add 90 degrees to the angle
    t.color = 'blue'
    t.forward(200)

    # This is necessary if speed is 0!
    t.flush()




#################### TASK 1: Triangle ####################

def draw_triangle(t, s, c):
    """
    Draws an equilateral triangle of side s and color c at current position.

    The direction of the triangle depends on the current facing of the turtle.
    If the turtle is facing west, the triangle points up and the turtle starts
    and ends at the east end of the base line.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)

    Parameter c: The triangle color
    Precondition: c is a valid turtle color (see the helper function above)
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)
    assert is_valid_color(c), report_error('Invalid color', c)

    color = t.color
    dash = t.dash
    t.color = c
    t.dash = None
    for _ in range(3):
        t.forward(s)
        t.right(120)
    t.color = color
    t.dash = dash
    t.flush()




#################### TASK 2: Hexagon ####################

def draw_hex(t, s):
    """
    Draws six triangles using the color 'cyan' to make a hexagon.

    The triangles are equilateral triangles, using draw_triangle as a helper.
    The drawing starts at the turtle's current position and heading. The middle
    of the hexagon is the turtle's starting position.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    for _ in range(6):
        draw_triangle(t, s, 'cyan')
        t.left(60)
    t.flush()



#################### Task 3: Radiating Shapes ####################

# DO NOT MODIFY (Helper for Task 3B)
def draw_polygon(t, radius, n):
    """
    Draws an n-sided regular polygon with the given radius.
    
    The polygon will centered at the current turtle position. The first vertex 
    of the polygon will be radius units along the current turtle heading.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED: 
    position (x and y, within round-off errors), heading, color, speed, visible, 
    and drawmode. There is no need to restore these.
    
    This procedure asserts all preconditions.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter radius: The polygon radius
    Precondition: radius is a valid side length (number >= 0)
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    """
    # Precondition assertions omitted
    
    # Remember the initial settings
    drawmode = t.drawmode
    heading  = t.heading
    
    # Compute the exterior angle between edges
    ang = 360.0/n
    side = 2*radius*math.sin(math.pi/n)
    
    # Move the turtle to the starting vertex and angle
    t.drawmode = False
    t.forward(radius)
    t.left(90+ang/2)
    t.drawmode = drawmode
    
    # t is in position, so it is time to draw
    for _ in range(n):
        t.forward(side)
        t.left(ang)
    
    # Restore the turtle
    t.drawmode = False
    t.right(90+ang/2)
    t.backward(radius)
    t.drawmode = drawmode


#################### Task 3A: Spirals ####################

def draw_spiral(w, side, ang, n, sp):
    """
    Draws a spiral using draw_spiral_helper(t, side, ang, n, sp)

    This function clears the window and makes a new turtle t. This turtle starts
    in the middle of the canvas facing north (NOT the default east). It then
    calls the function draw_spiral_helper(t, side, ang, n, sp). When it is done,
    the turtle is left hidden (visible is False).

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)

    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number

    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_window(w), report_error('Invalid window', w)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert is_number(ang), report_error('Invalid angle', ang)
    assert is_valid_iteration(n), report_error('Invalid iteration count', n)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 90
    draw_spiral_helper(t, side, ang, n, sp)
    t.visible = False
    t.flush()


def draw_spiral_helper(t, side, ang, n, sp):
    """
    Draws a spiral of n lines at the current position and heading.

    The spiral begins at the current turtle position and heading, turning ang
    degrees to the right after each line. Line 0 is side pixels long. Line 1 is
    2*side pixels long, and so on. Hence each Line i is (i+1)*side pixels long.
    The lines alternate between orange, cyan, red, and blue, in that order,
    with the first one orange.

    In addition, any line of length 5 or more is dashed (smaller lines are
    solid),
    Such lines are dashed by breaking them up into five equal segments, with any
    remainder applied to the last segment. If a line has less than length 5, it
    is solid.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color,
    speed, dash, visible, and drawmode. However, the final position and heading
    may be different. If you changed any of these five in the function, you must
    change them back.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)

    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number

    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert is_number(ang), report_error('Invalid angle', ang)
    assert is_valid_iteration(n), report_error('Invalid iteration count', n)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    color = t.color
    speed = t.speed
    dash = t.dash
    t.speed = sp
    colors = ('orange', 'cyan', 'red', 'blue')
    for i in range(n):
        length = (i + 1) * side
        t.color = colors[i % 4]
        t.dash = None
        if length >= 5:
            part = int(length / 5)
            t.dash = (part, part, part, part, int(length - 4 * part))
        t.forward(length)
        t.right(ang)
    t.color = color
    t.dash = dash
    t.speed = speed


#################### TASK 3B: Polygon Vortex ####################

def draw_vortex(w, r1, r2, n, k, sp):
    """
    Draws a polygonal vortex of k polygons with initial radius r1 and final
    radius r2

    This function clears the window and makes a new turtle t. This turtle starts
    in the middle of the canvas facing south (NOT the default east). It then
    calls the function draw_vortex_helper(t, r1, r2, n, k, sp). The function
    draws with a visible turtle, but the turtle if left hidden (visible is
    False)
    when it is done.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter r1: The radius of the first polygon in the vortex
    Precondition: r1 is a valid side length (number >= 0) and r1 <= r2

    Parameter r2: The radius of the last polygon in the vortex
    Precondition: r2 is a valid side length (number >= 0) and r1 <= r2

    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3

    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 2

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_window(w), report_error('Invalid window', w)
    assert is_valid_length(r1), report_error('Invalid inner radius', r1)
    assert is_valid_length(r2), report_error('Invalid outer radius', r2)
    assert r1 <= r2, report_error('Inner radius exceeds outer radius', r1)
    assert type(n) == int and n >= 3, report_error('Invalid side count', n)
    assert type(k) == int and k >= 2, report_error('Invalid polygon count', k)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 270
    draw_vortex_helper(t, r1, r2, n, k, sp)
    t.visible = False
    t.flush()


def draw_vortex_helper(t, r1, r2, n, k, sp):
    """
    Draws a polygon vortex of k polygons with initial radius r1 and final
    radius r2

    The polygons are drawn by turtle t, centered at the current position. The
    initial polygon is drawn with radius r1 and the current turtle heading.
    Later polygons are rotated by 360/k degrees to the left, and uniformly
    increase in size so that the final polygon has radius r2. The polygons
    alternate between blue, orange, and red, in that order, with the first one
    blue.

    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the
    beginning (within roundoff errors). If you change any attributes of the
    turtle. then you must restore them. Look at the helper draw_polygon for
    more information on what might be changed.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter r1: The radius of the first polygon in the vortex
    Precondition: r1 is a valid side length (number >= 0) and r1 <= r2

    Parameter r2: The radius of the last polygon in the vortex
    Precondition: r2 is a valid side length (number >= 0) and r1 <= r2

    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3

    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 2

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(r1), report_error('Invalid inner radius', r1)
    assert is_valid_length(r2), report_error('Invalid outer radius', r2)
    assert r1 <= r2, report_error('Inner radius exceeds outer radius', r1)
    assert type(n) == int and n >= 3, report_error('Invalid side count', n)
    assert type(k) == int and k >= 2, report_error('Invalid polygon count', k)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    color = t.color
    speed = t.speed
    dash = t.dash
    heading = t.heading
    t.speed = sp
    t.dash = None
    colors = ('blue', 'orange', 'red')
    for i in range(k):
        t.color = colors[i % 3]
        draw_polygon(t, r1 + i * (r2 - r1) / (k - 1), n)
        t.left(360.0 / k)
    t.heading = heading
    t.color = color
    t.dash = dash
    t.speed = speed



#################### TASK 3C: Radiating lines ####################

def radiate(w, side, n, sp):
    """
    Draws n straight, dashed radiating lines using radiate_helper(t, side, n,
    sp)

    This function clears the window and makes a new turtle t. This turtle starts
    in the middle of the canvas facing west (NOT the default east). It then
    calls
    radiate_helper(t, side, n, sp). When it is done, the turtle is left hidden
    (visible is False).

    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.

    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)

    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_window(w), report_error('Invalid window', w)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert type(n) == int and n >= 2, report_error('Invalid line count', n)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.heading = 180
    radiate_helper(t, side, n, sp)
    t.visible = False
    t.flush()


def radiate_helper(t, side, n, sp):
    """
    Draws n straight. dashed radiating lines of length s at equal angles.

    This lines are drawn using turtle t with the turtle moving at speed sp.
    A line drawn at angle ang, 0 <= ang < 360 has HSL color (ang % 360.0, 1,
    0.5).

    If side is greater than 3, the line is dashed, removing the middle third of
    the line has shown in the instructions. If the side is less than 3, the
    line remains solid. In either case the stroke weight is 2.0.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, dash, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these five in the function,
    you must change them back.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)

    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert type(n) == int and n >= 2, report_error('Invalid line count', n)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    color = t.color
    speed = t.speed
    dash = t.dash
    t.speed = sp
    t.stroke = 2.0
    t.dash = None
    if side >= 3:
        part = int(side / 3)
        t.dash = (part, part, int(side - 2 * part))
    for _ in range(n):
        t.heading = t.heading % 360.0
        t.color = introcs.HSL(t.heading, 1.0, 0.5)
        t.forward(side)
        t.drawmode = False
        t.backward(side)
        t.drawmode = True
        t.left(360.0 / n)
    t.heading = t.heading % 360.0
    t.color = color
    t.dash = dash
    t.speed = speed



############### TASK 4: Recursive Shapes ################

# HELPERS. DO NOT MODIFY
def fill_rect(p, x, y, w, h):
    """
    Fills a rectangle of lengths side, hght with center (x, y) using pen p.
    
    This procedure asserts all preconditions.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with solid attribute False.
    
    Parameter x: The x-coordinate of the rectangle center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the rectangle center
    Precondition: y is a number
    
    Parameter w: The width of the rectangle
    Precondition: w is a valid length (number >= 0)
    
    Parameter h: The height of the rectangle
    Precondition: h is a valid length (number >= 0)
    """
    # Precondition assertions omitted
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('x is not a valid position',y)
    assert is_valid_length(w), report_error('w is not a valid length',side)
    assert is_valid_length(h), report_error('h is not a valid length',hght)
    
    # Move to the center and draw
    p.move(x - w/2.0, y - h/2.0)
    p.solid = True
    p.drawLine(    0,  h)
    p.drawLine( w,     0)
    p.drawLine(    0, -h)
    p.drawLine(-w,     0)
    p.solid = False
    p.move(x - w/2.0, y - w/2.0)


def fill_hex(p, x, y, side):
    """
    Fills a hexagon of side length s with center at (x, y) using pen p.

    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the hexagon center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the hexagon center
    Precondition: y is a number
    
    Parameter side: The side length of the hexagon
    Precondition: side is a valid length (number >= 0)
    """
    # Precondition assertions omitted
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('x is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    
    # Move to the center and draw
    p.move(x + side, y)
    dx = side*math.cos(math.pi/3.0)
    dy = side*math.sin(math.pi/3.0)
    p.solid = True
    p.drawLine(  -dx,  dy)
    p.drawLine(-side,   0)
    p.drawLine(  -dx, -dy)
    p.drawLine(   dx, -dy)
    p.drawLine( side,   0)
    p.drawLine(   dx,  dy)
    p.solid = False


#################### TASK 4A: Vicsek Fractal ####################

def vicsek(w, size, d, sp):
    """
    Draws a Vicsek fractal of length size and depth d.

    This function clears the window and makes a new graphics pen p. This
    pen starts in the middle of the canvas at (0,0). It draws by calling
    the function vicsek_helper(p, 0, 0, size, d). The pen is visible
    during drawing and should be set to hidden at the end.

    The pen should have both a fill color and an edge color of red.

    REMEMBER: You need to flush the pen if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter size: The width and height of the Vicsek fractal
    Precondition: size is a valid length (number >= 0)

    Parameter d: The recursive depth of the fractal
    Precondition: n is a valid depth (int >= 0)

    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    assert is_window(w), report_error('Invalid window', w)
    assert is_valid_length(size), report_error('Invalid size', size)
    assert is_valid_depth(d), report_error('Invalid depth', d)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    w.clear()
    p = Pen(w)
    p.speed = sp
    p.fillcolor = 'red'
    p.edgecolor = 'red'
    vicsek_helper(p, 0, 0, size, d)
    p.visible = False
    p.flush()


def vicsek_helper(p, x, y, size, d):
    """
    Draws a Vicsek fractal of length size and depth d centered at (x,y)

    The fractal is drawn with the current pen color and visibility attribute.
    Follow the instructions on the course website to recursively draw the
    Vicsek fractal.

    This procedure asserts all preconditions.

    Parameter p: The graphics pen
    Precondition: p is a Pen with solid attribute False.

    Parameter x: The x-coordinate of the fractal center
    Precondition: x is a number

    Parameter y: The y-coordinate of the fractal center
    Precondition: y is a number

    Parameter size: The width and height of the Vicsek fractal
    Precondition: size is a valid length (number >= 0)

    Parameter d: The recursive depth of the fractal
    Precondition: n is a valid depth (int >= 0)
    """
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('Invalid x-coordinate', x)
    assert is_number(y), report_error('Invalid y-coordinate', y)
    assert is_valid_length(size), report_error('Invalid size', size)
    assert is_valid_depth(d), report_error('Invalid depth', d)

    if d == 0:
        fill_rect(p, x, y, size, size)
    else:
        third = size / 3.0
        vicsek_helper(p, x, y, third, d - 1)
        vicsek_helper(p, x - third, y, third, d - 1)
        vicsek_helper(p, x + third, y, third, d - 1)
        vicsek_helper(p, x, y - third, third, d - 1)
        vicsek_helper(p, x, y + third, third, d - 1)



#################### TASK 4B: Hexaflake ####################

def hexaflake(w, side, d, sp):
    """
    Draws a hexaflake of depth d with side length size.

    This function clears the window and makes a new graphics pen p. This pen
    starts in the middle of the canvas at (0,0). It draws by calling the
    function hexaflake_helper(p, 0, 0, size, d). The pen is visible during
    drawing and should be set to hidden at the end.

    The pen should have a fill color of 'sky blue' and a edge color of 'gray'.

    REMEMBER: You need to flush the pen if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter side: The side length of the flake fractal
    Precondition: side is a valid length (number >= 0)

    Parameter d: The recursive depth of the fractal
    Precondition: n is a valid depth (int >= 0)

    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    assert is_window(w), report_error('Invalid window', w)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert is_valid_depth(d), report_error('Invalid depth', d)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    w.clear()
    p = Pen(w)
    p.speed = sp
    p.fillcolor = 'sky blue'
    p.edgecolor = 'gray'
    hexaflake_helper(p, 0, 0, side, d)
    p.visible = False
    p.flush()


def hexaflake_helper(p, x, y, side, d):
    """
    Draws a hexaflake of side length size and depth d centered at (x,y).

    The fractal is drawn with the current pen color and visibility attribute.
    Follow the instructions on the course website to recursively draw the
    hexaflake.  For d > 0, draw a center flake and six surrounding recursive
    flakes.

    This procedure asserts all preconditions.

    Parameter p: The graphics pen
    Precondition: p is a Pen with solid attribute False.

    Parameter x: The x-coordinate of the fractal center
    Precondition: x is a number

    Parameter y: The y-coordinate of the fractal center
    Precondition: y is a number

    Parameter side: The side length of the flake fractal
    Precondition: side is a valid length (number >= 0)

    Parameter d: The recursive depth of the fractal
    Precondition: n is a valid depth (int >= 0)
    """
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('Invalid x-coordinate', x)
    assert is_number(y), report_error('Invalid y-coordinate', y)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert is_valid_depth(d), report_error('Invalid depth', d)

    if d == 0:
        fill_hex(p, x, y, side)
    else:
        third = side / 3.0
        hexaflake_helper(p, x, y, third, d - 1)
        for i in range(6):
            angle = i * math.pi / 3.0
            cx = x + 2 * third * math.cos(angle)
            cy = y + 2 * third * math.sin(angle)
            hexaflake_helper(p, cx, cy, third, d - 1)



#################### TASK 5: Koch Anti-Flake ####################

def kochflake(w, side, d, sp):
    """
    Draws a Koch antiflake with the given side length and depth d.

    This function clears the window and makes a new turtle T. This turtle starts
    with heading 60 degrees in the lower left corner of the equaliteral triangle
    centered at (0,0) with length side. It draws by calling the function
    kochflake_edge(t, side, d) three times, rotating the turtle after each call,
    just as you did in draw_triangle.

    The turtle should be visible while drawing, but hidden at the end. The
    turtle color is 'slate blue'.

    REMEMBER: You need to flush the turtle if the speed is 0.

    Parameter w: The window to draw upon.
    Precondition: w is a Window object.

    Parameter side: The side-length of the snowflake
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the snowflake
    Precondition: n is a valid depth (int >= 0)

    Parameter sp: The drawing speed.
    Precondition: sp is a valid turtle/pen speed.
    """
    assert is_window(w), report_error('Invalid window', w)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert is_valid_depth(d), report_error('Invalid depth', d)
    assert is_valid_speed(sp), report_error('Invalid speed', sp)

    w.clear()
    t = Turtle(w)
    t.speed = sp
    t.color = 'slate blue'
    t.move(-side / 2.0, -side * math.sqrt(3) / 6.0)
    t.heading = 60
    for _ in range(3):
        kochflake_edge(t, side, d)
        t.right(120)
    t.visible = False
    t.flush()


def kochflake_edge(t, side, d):
    """
    Draws a single Koch edge with length side and depth d at current
    position/angle.

    The edge is draw with the current turtle color. You should make no
    assumptions of the current angle of the turtle (e.g. use left and right to
    turn; do not set the heading).

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and heading
    may be different. If you changed any of these four in the function, you must
    change them back.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)

    Parameter d: The recursive depth of the edge
    Precondition: n is a valid depth (int >= 0)
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('Invalid side length', side)
    assert is_valid_depth(d), report_error('Invalid depth', d)

    if d == 0:
        t.forward(side)
    else:
        third = side / 3.0
        kochflake_edge(t, third, d - 1)
        t.right(60)
        kochflake_edge(t, third, d - 1)
        t.left(120)
        kochflake_edge(t, third, d - 1)
        t.right(60)
        kochflake_edge(t, third, d - 1)


################# HSL Color Support (DO NOT TOUCH) #################

def _color_guard(cls,c):
    """
    Returns: True c is a valid turtle color; False otherwise
    
    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    return is_valid_color(c)


def _color_code(cls,c):
    """
    Returns the TKinter representation of a color
    
    This method allows us to support all color formats, while using a single
    color format for the backend.
    
    Parameter c: the color value
    Precondition: _color_guard(c) is True
    """
    if type(c) in [introcs.RGB, introcs.HSV, introcs.HSL]:
        return c.webColor()
    
    if c[0] == '#':
        return c
    
    return introcs.tk_webcolor(c)


# Fix for 2026
Turtle._is_valid_color = _color_guard
Turtle._to_internal_color = _color_code
Pen._is_valid_color = _color_guard
Pen._to_internal_color = _color_code
