import datetime

from utils import add, subtract, multiply

name = "Ahsanur Rahman"
print("My Name:", name)


today = datetime.date.today()
print("Today’s Date:", today)

print("Addition:", add(10, 20))
print("Subtraction:", subtract(10, 20))
print("Multiplication:", multiply(10, 20))