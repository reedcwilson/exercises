
def convert(in_grid):
    grids = []
    for i in range(0, len(in_grid), 4):
        grid_str = in_grid[i:i+4]
        c = len(in_grid)

        if c == 0 or c % 4 != 0 or any(len(r) % 3 != 0 for r in grid_str):
            raise ValueError('Invalid grid')

        # extract individual numbers from grid
        num_strs = (
            ''.join([grid_str[i][g:g+3] for i in range(4)])
            for g in
            range(0, len(grid_str[0]), 3)
        )

        # determine which number it is
        grids.append(''.join([str(numbers.index(s)) if s in numbers else '?'
                              for s in num_strs]))

    return ','.join(grids)


numbers = [''.join(s) for s in [
    " _ "
    "| |"
    "|_|"
    "   ",

    "   "
    "  |"
    "  |"
    "   ",

    " _ "
    " _|"
    "|_ "
    "   ",

    " _ "
    " _|"
    " _|"
    "   ",

    "   "
    "|_|"
    "  |"
    "   ",

    " _ "
    "|_ "
    " _|"
    "   ",

    " _ "
    "|_ "
    "|_|"
    "   ",

    " _ "
    "  |"
    "  |"
    "   ",

    " _ "
    "|_|"
    "|_|"
    "   ",

    " _ "
    "|_|"
    " _|"
    "   "
]]
