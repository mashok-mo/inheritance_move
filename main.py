class Field:
    def __init__(self):
        self.matrix = []
    def render(self, border, character):
        self.matrix = [0] * border
        for i in range(border):
            self.matrix[i] = [0] * border
        self.matrix[character.point.x][character.point.y] = 1
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Character:
    def __init__(self, point):
        self.point = point
    def move(self, direction, distance, border):
        if direction == '1':
            if self.point.x - distance < 0:
                print('Игрок выходит за пределы поля')
            else:
                self.point.x -= distance
        elif direction == '2':
            if self.point.y + distance >= border:
                print('Игрок выходит за пределы поля')
            else:
                self.point.y += distance
        elif direction == '3':
            if self.point.x + distance >= border:
                print('Игрок выходит за пределы поля')
            else:
               self.point.x += distance
        elif direction == '4':
            if self.point.y - distance < 0:
                print('Игрок выходит за пределы поля')
            else:
               self.point.y -= distance
        else:
            print('Неверная команда')
def main():
    border = int(input('Введите размер поля: '))
    field = Field()
    print('Введите коордтинаты игрока')
    y = int(input('x: '))
    x = int(input('y: '))
    if x < 0 or y < 0 or x >=border or y >= border:
        print('Неверно введенные координаты')
    else:
        character = Character(Point(x,y))
        field.render(border, character)
        while True:
            stop = input('Хотите передвинуть персонажа? да/нет ')
            if stop == 'да':
                direction = input('Введите направление движения:\n1 - вверх, 2 - вправо, 3 - вниз, 4 - влево\n')
                distance = int(input('Введите расстояние: '))
                character.move(direction, distance, border)
                field.render(border, character)
            elif stop == 'нет':
                break
            else:
                print('Неверная команда')
main()