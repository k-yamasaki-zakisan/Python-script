import tkinter as tk


class Shape:

    def __init__(self, x, y, width, height, center=False):
        if center:
            x -= width // 2
            y -= height // 2
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    def intersect(self, target):
        hit_x = max(self.x1, target.x1) <= min(self.x2, target.x2)
        hit_y = max(self.y1, target.y1) <= min(self.y2, target.y2)
        return hit_x and hit_y


class Paddle(Shape):

    def __init__(self, x, y, width=45, height=8, speed=6, color="blue"):
        super().__init__(x, y, width, height, center=True)
        self.speed = speed
        self.color = color
        self.name = "paddle"

    def right(self, event):
        self.x1 += self.speed
        self.x2 += self.speed

    def left(self, event):
        self.x1 -= self.speed
        self.x2 -= self.speed

    def limit(self, area):
        adjust = (max(self.x1, area.x1) - self.x1 or
                  min(self.x2, area.x2) - self.x2)
        self.x1 += adjust
        self.x2 += adjust

    def move(self):
        pass

    def draw(self, canvas):
        canvas.delete(self.name)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                fill=self.color, tag=self.name)

    def delete(self, canvas):
        canvas.delete(self.name)


class Ball(Shape):

    def __init__(self, x, y, size=10, dx=2, dy=2, color="red"):
        super().__init__(x, y, size, size, center=True)
        self.dx = dx
        self.dy = dy
        self.color = color
        self.name = "ball"

    def move(self):
        self.x1 += self.dx
        self.y1 += self.dy
        self.x2 += self.dx
        self.y2 += self.dy

    def limit(self, area):
        if self.x1 <= area.x1 or area.x2 <= self.x2:
            self.dx *= -1
        if self.y1 <= area.y1 or area.y2 <= self.y2:
            self.dy *= -1

    def bound(self, target):
        if not self.intersect(target):
            return False
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        if (self.dx > 0 and center_x <= target.x1 or
            self.dx < 0 and target.x2 <= center_x):
                self.dx *= -1
        if (self.dy > 0 and center_y <= target.y1 or
            self.dy < 0 and target.y2 <= center_y):
                self.dy *= -1
        return True

    def draw(self, canvas):
        canvas.delete(self.name)
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                           fill=self.color, tag=self.name)

    def delete(self, canvas):
        canvas.delete(self.name)


class Block(Shape):

    def __init__(self, x, y, width, height, gap_x=0, gap_y=0, center=False,
                 color="orange", point=1):
        super().__init__(x + gap_x, y + gap_y,
                         width - gap_x * 2, height - gap_y * 2, center=center)
        self.point = point
        self.color = color
        self.name = f"block{x}.{y}"
        self.exists = True

    def break_and_bound(self, target):
        if self.exists and target.bound(self):
            self.exists = False
            return self.point
        else:
            return 0

    def is_broken(self):
        return not self.exists

    def draw(self, canvas):
        canvas.delete(self.name)
        if self.exists:
            canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                    fill=self.color, tag=self.name)


class BlockRow:
    def __init__(self, color, point):
        self.color = color
        self.point = point


class Blocks:
    #ROWS = [BlockRow("orange", 1)] * 3
    ROWS = BlockRow("cyan", 10), BlockRow("yellow", 20), BlockRow("orange", 30)

    def __init__(self, x, y, width, height, columns=12, rows=None):
        rows = (rows or self.ROWS)[::-1]
        w = width // columns
        h = height // len(rows)
        self.blocks = [Block(x + dx, y + dy, w, h, gap_x=6, gap_y=12,
                             color=row.color, point=row.point)
                       for dy, row in zip(range(0, h * len(rows) + 1, h), rows)
                       for dx in range(0, w * columns + 1, w)]

    def break_and_bound(self, target):
        return sum(block.break_and_bound(target) for block in self.blocks)

    def are_wiped(self):
        return all(block.is_broken() for block in self.blocks)

    def draw(self, canvas):
        for block in self.blocks:
            block.draw(canvas)


class Wall(Shape):
    CATCH_LINES = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.catch_line = self.y2 - self.CATCH_LINES

    def catch(self, target):
        return target.y2 >= self.catch_line


class Score:
    FONT = ('FixedSys', 16)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0
        self.name = "score"

    def add(self, point):
        self.score += point

    def draw(self, canvas):
        canvas.delete(self.name)
        canvas.create_text(self.x, self.y, text=f"Score = {self.score}",
                           font=self.FONT, tag=self.name)


class Breakout:
    TICK = 20  # 更新間隔
    FONT = ('FixedSys', 40)

    def __init__(self, width, height):
        self.center = (width // 2, height // 2)
        self.root = tk.Tk()
        self.root.title("ブロック崩し")
        self.root.minsize(width, height)
        self.root.maxsize(width, height)
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.paddle = Paddle(width // 2, height - 30)
        self.ball = Ball(width // 3, height * 2 // 3)
        self.blocks = Blocks(0, 40, width, 120)
        self.wall = Wall(0, 0, width, height)
        self.score = Score(width - 70, 20)
        self.keybind()
        self.draw()

    def keybind(self):
        self.root.bind("q", self.quit)
        self.root.bind("<Right>", self.paddle.right)
        self.root.bind("<Left>", self.paddle.left)

    def start(self):
        self.playing = True
        self.play()
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.quit()

    def end(self, message):
        self.paddle.delete(self.canvas)
        self.ball.delete(self.canvas)
        self.canvas.create_text(*self.center, text=message, font=self.FONT)
        self.canvas.pack()
        self.playing = False 

    def quit(self, *args):
        self.root.quit()

    def play(self):
        try:
            if self.playing:
                self.operate()
                self.draw()
                self.root.after(self.TICK, self.play)
            else:
                input("Hit return key to end")
                self.quit()
        except KeyboardInterrupt:
            self.quit()

    def operate(self):
        self.paddle.move()
        self.paddle.limit(self.wall)
        self.ball.move()
        self.ball.limit(self.wall)
        self.ball.bound(self.paddle)
        point = self.blocks.break_and_bound(self.ball)
        self.score.add(point)
        self.over()
        self.clear()

    def draw(self):
        self.ball.draw(self.canvas)
        self.paddle.draw(self.canvas)
        self.blocks.draw(self.canvas)
        self.score.draw(self.canvas)
        self.canvas.pack()

    def over(self):
        if self.wall.catch(self.ball):
            self.end("GAME OVER(T_T)")
            

    def clear(self):
        if self.blocks.are_wiped():
            self.end("GAME CLEAR(^0^)")

def block_break_main():
    Breakout(width=600, height=480).start()

if __name__ == '__main__':
    block_break_main()