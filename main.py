def colorChange(color):
  if color=="red":
    print("\033[31m", end="")
  elif color=="white":
    print("\033[0m", end="")
  elif color=="blue":
    print("\033[34m", end="")
  elif color=="yellow":
    print("\033[33m", end="")
  elif color == "green":
    print("\033[32m", end="")
  elif color == "purple":
    print("\033[35m", end="")

title = f"{Music App} =="
print(f"{title:^35}")
print()
colorChange("red")
print("🔥▶️")
colorChange("white")
print("Radio Gaga")
print()
colorChange("yellow")
print("Queen")
print()
print()
colorChange("white")
print("PREV")
colorChange("green")
print("NEXT")
colorChange("purple")
print("PAUSE")
print()


    