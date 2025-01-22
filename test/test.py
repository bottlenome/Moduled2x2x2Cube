from cube import coord
from cube import cubie
from cube import defs
from cube import enums
from cube import face
from cube import misc

def move_test(state, move):
    cc = coord.CoordCube.from_string(state)
    cc.move(move)
    return cc.to_string()

if __name__ == '__main__':
    print(int(enums.Facelet.U1))
    print(move_test("UUUURRRRFFFFDDDDLLLLBBBB", enums.Move.U1))