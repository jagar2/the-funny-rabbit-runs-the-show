# %%

# BEGIN TESTS

# %%

""" # BEGIN TEST CONFIG
points: 1
hidden: false
success_message: "Success: The total pellet count is correctly calculated!"
failure_message: "Failed: The total pellet count is incorrect."
""" # END TEST CONFIG

expected_pellet_count = sum(row.count('.') for row in BOARD_LAYOUT)
assert total_pellets == expected_pellet_count, f"Expected {expected_pellet_count} pellets, but got {total_pellets}."

# %%

""" # BEGIN TEST CONFIG
points: 1
hidden: false
success_message: "Success: Pac-Man's position is correctly identified!"
failure_message: "Failed: Pac-Man's position is not set correctly."
""" # END TEST CONFIG

expected_pacman_pos = None
for j in range(ROWS):
for i in range(COLS):
if BOARD_LAYOUT[j][i] == "P":
expected_pacman_pos = [i, j]
break
if expected_pacman_pos:
break

assert pacman_pos == expected_pacman_pos, f"Expected Pac-Man at {expected_pacman_pos}, but got {pacman_pos}."

# %%

""" # BEGIN TEST CONFIG
points: 1
hidden: false
success_message: "Success: Pac-Man's start position is correctly recorded!"
failure_message: "Failed: Pac-Man's start position is incorrect."
""" # END TEST CONFIG

assert pacman_start == expected_pacman_pos, f"Expected Pac-Man start at {expected_pacman_pos}, but got {pacman_start}."

# %%

""" # BEGIN TEST CONFIG
points: 1
hidden: false
success_message: "Success: Ghost positions are correctly identified!"
failure_message: "Failed: Ghost positions are incorrect."
""" # END TEST CONFIG

expected_ghosts = []
for j in range(ROWS):
for i in range(COLS):
if BOARD_LAYOUT[j][i] == "G":
expected_ghosts.append([i, j])

assert ghosts == expected_ghosts, f"Expected ghosts at {expected_ghosts}, but got {ghosts}."

# %%

""" # BEGIN TEST CONFIG
points: 1
hidden: false
success_message: "Success: Pac-Man and Ghosts were removed from the board correctly!"
failure_message: "Failed: Pac-Man and/or Ghosts were not removed properly from the board."
""" # END TEST CONFIG

board_without_pacman_ghosts = [list(row) for row in BOARD_LAYOUT]
for j in range(ROWS):
for i in range(COLS):
if board_without_pacman_ghosts[j][i] in ["P", "G"]:
board_without_pacman_ghosts[j][i] = " "

assert board == board_without_pacman_ghosts, "The board still contains Pac-Man or Ghosts when they should have been removed."

# %%

# END TESTS
