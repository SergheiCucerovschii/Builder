class Period:
  def __init__(self,start,end):
    self.start = start
    self.end = end
    if self.start > self.end:
      raise ValueError(f"You enter wrong date")


  def  __str__(self):
    return f"From {self.start} to {self.end}"     # e.g. "[01.01.2021 .. 02.01.2021]"

# p = Period("01.01.2021","02.01.2021")
# print(p)