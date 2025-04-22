import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_40x20(self):
        num_cols = 40
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_20x40(self):
        num_cols = 20
        num_rows = 40
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()

        self.assertFalse(
            m1._cells[0][0].has_top_wall,
        )

        self.assertFalse(
            m1._cells[num_cols - 1][num_rows -1].has_bottom_wall
        )

    def test_maze_break_entrance_exit_20x40(self):
        num_cols = 20
        num_rows = 40
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()

        self.assertFalse(
            m1._cells[0][0].has_top_wall,
        )

        self.assertFalse(
            m1._cells[num_cols - 1][num_rows -1].has_bottom_wall
        )

    def test_maze_visited_cells_reset(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        m1._cells[0][0].visited = True
        m1._cells[0][1].visited = True
        m1._cells[0][2].visited = True
        m1._cells[1][0].visited = True
        m1._cells[1][1].visited = True
        m1._cells[1][2].visited = True
        m1._cells[2][0].visited = True
        m1._cells[2][2].visited = True
        m1._cells[2][2].visited = True
        
        m1._reset_visited_cells()

        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[i])):
                self.assertFalse(m1._cells[i][j].visited,
                    f"Cell at ({i},{j}) should have visited=False")




    

if __name__ == "__main__":
    unittest.main()