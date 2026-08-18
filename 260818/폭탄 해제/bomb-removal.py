unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

bomb = Bomb(unlock_code, wire_color, seconds)

print("code :", bomb.code)
print("color :", bomb.color)
print("second :", bomb.sec)