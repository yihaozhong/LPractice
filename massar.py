import statistics

def MovingMedian(arr):

  WindowSize = arr[0]
  Data = arr[1:]
  N = len(Data)
  retArr = []

  for i in range(N):
    if (i < WindowSize):
      window = Data[0:i+1]
      
    else:
      window = Data[(i-WindowSize)+1:i+1]

    window.sort()
    retArr.append(str(round(statistics.median(window))))