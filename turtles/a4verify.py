"""Additional specification checks for A4 using a real graphics window."""
import math
import unittest
from unittest.mock import patch

import introcs
from introcs.turtle import Window, Turtle, Pen
import a4


class DrawingTests(unittest.TestCase):
    """Check geometry, state restoration, and invalid inputs."""

    @classmethod
    def setUpClass(cls):
        cls.window = Window()

    @classmethod
    def tearDownClass(cls):
        cls.window.dispose()

    def setUp(self):
        self.window.clear()

    def turtle(self):
        t = Turtle(self.window)
        t.speed = 0
        t.move(13, -27)
        t.heading = 37
        t.color = 'purple'
        t.dash = (7, 2)
        t.visible = False
        return t

    def state(self, t):
        return (t.color, t.speed, t.dash, t.visible, t.drawmode)

    def assert_position(self, t, x, y, heading):
        self.assertAlmostEqual(t.x, x, places=7)
        self.assertAlmostEqual(t.y, y, places=7)
        difference = (t.heading - heading + 180) % 360 - 180
        self.assertAlmostEqual(difference, 0, places=7)

    def record(self, lines):
        forward = Turtle.forward

        def draw(t, length):
            if t.drawmode:
                lines.append((t.x, t.y, length, t.heading, t.color,
                              t.dash, t.stroke))
            return forward(t, length)

        return patch.object(Turtle, 'forward', draw)

    def test_triangles_and_hexagons(self):
        for function, count in ((a4.draw_triangle, 3), (a4.draw_hex, 18)):
            t = self.turtle()
            before = self.state(t)
            lines = []
            args = (t, 51, 'green') if count == 3 else (t, 51)
            with self.record(lines):
                function(*args)
            self.assertEqual(len(lines), count)
            self.assertTrue(all(line[5] is None for line in lines))
            self.assertEqual(self.state(t), before)
            self.assert_position(t, 13, -27, 37)

    def test_spiral_patterns(self):
        t = self.turtle()
        before = self.state(t)
        lines = []
        with self.record(lines), patch.object(Turtle, 'flush') as flush:
            a4.draw_spiral_helper(t, 2.5, -75, 5, 0)
            flush.assert_not_called()
        self.assertEqual([line[2] for line in lines],
                         [2.5, 5, 7.5, 10, 12.5])
        self.assertEqual([line[4] for line in lines],
                         ['orange', 'cyan', 'red', 'blue', 'orange'])
        self.assertEqual([line[5] for line in lines],
                         [None, (1, 1, 1, 1, 1), (1, 1, 1, 1, 3),
                          (2, 2, 2, 2, 2), (2, 2, 2, 2, 4)])
        self.assertEqual(self.state(t), before)

    def test_vortex_radii_and_state(self):
        t = self.turtle()
        before = self.state(t)
        with patch.object(a4, 'draw_polygon',
                          wraps=a4.draw_polygon) as polygon:
            with patch.object(Turtle, 'flush') as flush:
                a4.draw_vortex_helper(t, 0, 90, 5, 4, 0)
                flush.assert_not_called()
            self.assertEqual([call.args[1] for call in polygon.call_args_list],
                             [0, 30, 60, 90])
        self.assertEqual(self.state(t), before)
        self.assert_position(t, 13, -27, 37)

    def test_radiate_patterns_and_colors(self):
        for side in (0, 2.5, 3, 10.5):
            t = self.turtle()
            before = self.state(t)
            lines = []
            with self.record(lines), patch.object(Turtle, 'flush') as flush:
                a4.radiate_helper(t, side, 4, 0)
                flush.assert_not_called()
            self.assertEqual(len(lines), 4)
            for i, line in enumerate(lines):
                self.assertAlmostEqual(line[0], 13)
                self.assertAlmostEqual(line[1], -27)
                self.assertEqual(line[4], introcs.HSL((37 + i * 90) % 360,
                                                    1.0, 0.5))
                self.assertEqual(line[6], 2.0)
                if side < 3:
                    self.assertIsNone(line[5])
                else:
                    self.assertEqual(sum(line[5]), int(side))
            self.assertEqual(self.state(t), before)
            self.assert_position(t, 13, -27, 37)

    def test_fractal_counts_and_centers(self):
        p = Pen(self.window)
        p.speed = 0
        p.visible = False
        for helper, fill, count in ((a4.vicsek_helper, 'fill_rect', 5),
                                    (a4.hexaflake_helper, 'fill_hex', 7)):
            for depth in range(4):
                with patch.object(a4, fill, wraps=getattr(a4, fill)) as draw:
                    with patch.object(Pen, 'flush') as flush:
                        helper(p, 10, -20, 81, depth)
                        flush.assert_not_called()
                    self.assertEqual(draw.call_count, count ** depth)
                    centers = [call.args[1:3] for call in draw.call_args_list]
                    self.assertAlmostEqual(sum(x for x, y in centers) /
                                           len(centers), 10)
                    self.assertAlmostEqual(sum(y for x, y in centers) /
                                           len(centers), -20)
                    for call in draw.call_args_list:
                        self.assertAlmostEqual(call.args[3], 81 / 3 ** depth)
                self.assertFalse(p.visible)
                self.assertFalse(p.solid)

    def test_koch_geometry(self):
        for depth in range(5):
            t = self.turtle()
            before = self.state(t)
            lines = []
            with self.record(lines), patch.object(Turtle, 'flush') as flush:
                a4.kochflake_edge(t, 81, depth)
                flush.assert_not_called()
            self.assertEqual(len(lines), 4 ** depth)
            self.assertTrue(all(math.isclose(line[2], 81 / 3 ** depth)
                                for line in lines))
            self.assert_position(t, 13 + 81 * math.cos(math.radians(37)),
                                 -27 + 81 * math.sin(math.radians(37)), 37)
            self.assertEqual(self.state(t), before)
        t = self.turtle()
        t.move(0, 0)
        t.heading = 0
        lines = []
        with self.record(lines):
            a4.kochflake_edge(t, 90, 1)
        self.assertLess(lines[2][1], 0)

    def test_main_functions(self):
        cases = ((a4.draw_spiral, (5, 90, 4), 90),
                 (a4.draw_vortex, (0, 30, 3, 2), 270),
                 (a4.radiate, (15, 4), 180),
                 (a4.vicsek, (27, 1), None),
                 (a4.hexaflake, (27, 1), None),
                 (a4.kochflake, (27, 1), 60))
        for speed in (0, 10):
            for function, args, heading in cases:
                with self.subTest(function=function.__name__, speed=speed):
                    function(self.window, *args, speed)
                    tools = (self.window.pens if heading is None
                             else self.window.turtles)
                    self.assertEqual(len(tools), 1)
                    tool = tools[0]
                    self.assertFalse(tool.visible)
                    self.assertEqual(tool.speed, speed)
                    if function == a4.kochflake:
                        self.assert_position(tool, -13.5,
                                             -27 * math.sqrt(3) / 6, 60)
                    if function == a4.vicsek:
                        self.assertEqual(tool.fillcolor, 'red')
                        self.assertEqual(tool.edgecolor, 'red')
                    if function == a4.hexaflake:
                        self.assertEqual(tool.fillcolor, 'sky blue')
                        self.assertEqual(tool.edgecolor, 'gray')

    def test_all_preconditions(self):
        t = self.turtle()
        p = Pen(self.window)
        p.speed = 0
        w = self.window
        invalid = {'tool': (None, 'tool'), 'length': (-1, True, '5'),
                   'number': (True, '5', None), 'depth': (-1, 1.5, True),
                   'speed': (-1, 11, True, 1.5), 'one': (0, True, 1.5),
                   'two': (1, True, 2.5), 'three': (2, True, 3.5),
                   'color': ('invalid color', None, 12)}
        cases = ((a4.draw_triangle, [t, 5, 'red'],
                  ['tool', 'length', 'color']),
                 (a4.draw_hex, [t, 5], ['tool', 'length']),
                 (a4.draw_spiral, [w, 5, 90, 2, 0],
                  ['tool', 'length', 'number', 'one', 'speed']),
                 (a4.draw_spiral_helper, [t, 5, 90, 2, 0],
                  ['tool', 'length', 'number', 'one', 'speed']),
                 (a4.draw_vortex, [w, 1, 5, 3, 2, 0],
                  ['tool', 'length', 'length', 'three', 'two', 'speed']),
                 (a4.draw_vortex_helper, [t, 1, 5, 3, 2, 0],
                  ['tool', 'length', 'length', 'three', 'two', 'speed']),
                 (a4.radiate, [w, 5, 2, 0],
                  ['tool', 'length', 'two', 'speed']),
                 (a4.radiate_helper, [t, 5, 2, 0],
                  ['tool', 'length', 'two', 'speed']),
                 (a4.vicsek, [w, 5, 0, 0],
                  ['tool', 'length', 'depth', 'speed']),
                 (a4.hexaflake, [w, 5, 0, 0],
                  ['tool', 'length', 'depth', 'speed']),
                 (a4.kochflake, [w, 5, 0, 0],
                  ['tool', 'length', 'depth', 'speed']),
                 (a4.vicsek_helper, [p, 0, 0, 5, 0],
                  ['tool', 'number', 'number', 'length', 'depth']),
                 (a4.hexaflake_helper, [p, 0, 0, 5, 0],
                  ['tool', 'number', 'number', 'length', 'depth']),
                 (a4.kochflake_edge, [t, 5, 0],
                  ['tool', 'length', 'depth']))
        for function, args, kinds in cases:
            for i, kind in enumerate(kinds):
                for value in invalid[kind]:
                    bad = args.copy()
                    bad[i] = value
                    with self.subTest(function=function.__name__,
                                      parameter=i, value=value):
                        with self.assertRaises(AssertionError):
                            function(*bad)
        for function, tool in ((a4.draw_vortex, w),
                               (a4.draw_vortex_helper, t)):
            with self.assertRaises(AssertionError):
                function(tool, 10, 5, 3, 2, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
