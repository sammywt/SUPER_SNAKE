# SNAKE PLUS

Using pygame (built on top of python3) to create a working recreation of the retro fan-favorite with some bonus features to make the game more interesting and difficult

On load, the viewer will be met with the game board in the center of the screen, with a few simple instructions to the side: press x to pause, press any arrow key to begin

With future versions, a small key will be added to indicate what shapes/colors indicate bombs/spikes/null spaces

## VERSION 1

The standard snake game- A single block or pixel group that can be navigated around a board to collect pieces and grow the length of the tail. If the snake runs its own tail, the game is over. If the snake hits the edge of the board, the snake will then move to the otherside of the board. 

My best estimate is that the game will be created by utilizing lists or by importing numPy to add support for array data type. Description is based on array data type functionality

An array of arrays will be used to represent the game board, with each index of a subarray representing a spot on the board. 

```python
let game_board = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]
```

The above variable game_board should create a 5x5 board, where up and down movement is done by accessing the array itself, and left to right movement is done by accessing the index of the given array. for example:

```python
game_start_position = game_board[3][3]
```
Above code would set the starting position of the board to the center

Movement around the board would look for a specific arrow pad key signal and move the index accordingly, for example:

```python
for i of game_board:
    for j of game_board[i]:
        # if j (position on board) is greater or less than the width of the board, move to the other side of the board
        if (j > game_board[i].len()):
            j = 0
        elif (j < 0):
            j = game_board[i].len()
        # if the key pressed is the left key, shift to the left on the game board by moving left in the array
        elif (arrow_pad_left = True):
            j -= 1
        # if the key pressed is the right key, shift to the right on the game board by moving right in the array
        elif (arrow_pad_right = True):
            j += 1
        else:
            pass
    if (i > game_board.len()):
        i = 0
    elif i < 0:
        i = game_board.len()
    elif (arrow_pad_up = True):
        i -= 1
    elif (arrow_pad_down = True):
        i += 1
    else:
        pass
```

The above code would only work to move the snake one space at a time. To have the snake move continuously, I believe some form of infinite loop needs to be intentionally invoked, calling upon the (i+=1) on every iteration. To do so, calling the function at the end of each if/elif/else statement shouild solve this issue, as so:

```python
def function_name():
    ...
    elif (arrow_pad_up = True):
        i -= 1
        function_name()
```


## VERSION 2

Adding spikes to the playing field- If the snake runs in to a spike, it will shed one unit length of tail. If the snake has no units of tail to shed (is just the head, what the user begins the game with), the game is over. Spikes will be represented by a specific color, if the game ends, the board will reset with spikes in new locations

A recursive function could be used to ensure the proper number of spikes is added to a game board, E.G. if a game board has less than 10% of spaces covered in spikes, run the function again (call on itself to create and place another spike randomly using Math.random and Math.floor set) until the base case of 10% of spaces having a spike is reached.

## VERSION 3

Adding bombs to the playing field- If the snake runs in to a bomb, it is an instant game over regardless of length. Bombs will be added to the playing field using a similar function to the spike implementation, but using a smaller percentage so less spaces contain bombs (around 2% of spaces as opposed to 10%). If the game ends and restarts, bombs will be randomly placed into new positions.

## VERSION 4

Dead spaces will be added to the board where the snake must travel around the dead space. I believe this can be achieved by creating a specific instance in the game board randomly (math.random math.floor) then setting the random spaces to something like "." as opposed to " ". Then using an if else statement, if the index of the array is equivalent to ".", the position is reset to just prior to the dead space

## VERSION 5

Increasing difficulty- levels will be created to increase the difficulty by raising the percentage of spaces containing spikes, bombs, and dead spaces depending on the level number

## VERSION 6

A functional backend with user authentication that stores a users highest level achieved, and allows a user to return to easier levels. Can also store a global "highest level achieved" value and return it to all users with a username, so the player who has achieved the highest level will be displayed on all users screen.