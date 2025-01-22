from .coord import CoordCube
from .enums import Move, Color

int2char_map = {
    int(Color.U): "U",
    int(Color.R): "R",
    int(Color.F): "F",
    int(Color.D): "D",
    int(Color.L): "L",
    int(Color.B): "B"
}

char2int_map = {
    'U': int(Color.U),
    'R': int(Color.R),
    'F': int(Color.F),
    'D': int(Color.D),
    'L': int(Color.L),
    'B': int(Color.B)
}

def list_state_to_string(state):
    str_list = [int2char_map[i] for i in state]
    return "".join(str_list)

def string_state_to_list(state):
    return [char2int_map[i] for i in state]

def move(state, move):
    state_str = list_state_to_string(state)
    enum_move = Move(0)
    cc = CoordCube.from_string(state_str)
    cc.move(enum_move)
    next_state_str = cc.to_string()
    return string_state_to_list(next_state_str)

if __name__ == '__main__':
    print(list_state_to_string([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]))
    print(string_state_to_list("UUUURRRRFFFFDDDDLLLLBBBB"))
    print(move([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5], 0))