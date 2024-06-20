class Circle:
  pi = 3.14
  def test1(self):
    pi2 = 22/7
    return pi2
  def area(self, radius):
    pi = 3.14
    area = pi * radius **2
    return area

circle = Circle()
print(circle.test1())

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
print(pizza_area)
print(teaching_table_area)
print(round_room_area)