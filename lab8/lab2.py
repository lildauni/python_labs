from datetime import datetime
from typing import List

class Train:
  def __init__(self, destination: str, trainNum: str, dateStart):
    self.destination = destination
    self.trainNum = trainNum
    self.dateStart = dateStart

trains = []
trains.append(Train('Херсон', '01', datetime(2019, 8, 30, 18)))
trains.append(Train('Житомир', '02', datetime(2019, 8, 30, 17)))
trains.append(Train('Запорожье', '03', datetime(2019, 8, 30, 14)))
trains.append(Train('Киев', '04', datetime(2019, 8, 30, 22)))
trains.append(Train('Тернополь', '05', datetime(2019, 8, 30, 18)))

trains.sort(key = lambda train: train.trainNum)
# for i in range(0, 5):
#   print(trains[i].trainNum)

def sortByDestination(trains: List[Train]) -> List[Train]:
  return sorted(trains, key = lambda train: train.destination)

def getTrainByNum(num: int):
  return trains[num]

