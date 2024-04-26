

class DynamicArray:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.length = 0
    self.arr = [0] * capacity

  
  def get(self, i: int) -> int:
    return self.arr[i]
  
  def set(self, i: int, n: int) -> None:
      self.arr[i] = n

  def pushback(self, n: int) -> None:
      if self.length == self.capacity
      #  Resize()

      self.arr[self.length] = n
      self.length += 1

  def popback(self) -> int:
      self.length = -1

      return self.arr[self.length]
  

  def capacity(self) -> int:
      return self.capacity
  
  def size(self) -> int:
      return self.length


