import random

class Tile:
    def __init__(self, id, up=None, down=None):
        self.id = id
        self.up = up
        self.down = down


    def info(self):
        print(self.id, end=" ")
        if self.up:
            print(self.up.id, end=" ")
        else:
            print("--", end = " ")
        if self.down:
            print(self.down.id)
        else:
            print("--")


class Board:
    def __init__(self, up_downs):
        self.max = 25
        self.board = [Tile(id) for id in range(1, 26)]

        for item in up_downs:
                if item[1] < 0:
                    self.board[item[0]-1].down = self.board[abs(item[1])-1]
                else:
                    self.board[item[0]-1].up = self.board[item[1]-1]

        # for tile in self.board:
        #     tile.info()


class Player:

    def __init__(self, name):
        self.throws = 0
        self.moves = 0
        self.name = name
        self.position = b1.board[0]


    def throw_dice(self):
        self.throws += 1
        return random.randint(1,6)


    def play(self):

        move_by = self.throw_dice()

        if self.position.id + move_by > b1.max:
            print(f"{self.name} || Dice: {move_by:02} || No Move")
            return

        old_position = self.position
        self.position = b1.board[int(self.position.id) + move_by - 1]

        if self.position.down:
            temp_position = self.position
            self.position = self.position.down
            unluck = temp_position.id - self.position.id
            print(f"{self.name} || Dice: {move_by:02} || From: {old_position.id:02} || To: {self.position.id:02} || Unluck Value: {unluck:02}")

        elif self.position.up:
            temp_position = self.position
            self.position = self.position.up
            luck = self.position.id - temp_position.id
            print(f"{self.name} || Dice: {move_by:02} || From: {old_position.id:02} || To: {self.position.id:02} || Luck Value: {luck:02}")

        else:
            print(f"{self.name} || Dice: {move_by:02} || From: {old_position.id:02} || To: {self.position.id:02}")

        self.moves += 1
        if self.position.id == b1.max:
            print(f"You Win!! \nMoves: {self.moves} \nThrows: {self.throws}")
            exit

up_downs = [(7,14),(8,-4),(10,18),(16,23),(17,-15),(22,-12)]
b1 = Board(up_downs)
p1 = Player("P1")

# for tile in b1.board:
#     tile.info()

while p1.position.id != b1.max:
    p1.play()
