def passerRating(attempts,completions,yards,touchdowns,interceptions):
  #Part A
  CPA_one = (int(completions)/int(attempts))
  CPA_two = (CPA_one*100)-20
  CPA = (CPA_two/20)
  PartA = CPA

#Part B
  YPA_one = (int(yards)/int(attempts))
  YPA_two = (YPA_one-3)
  YPA = (YPA_two/4)
  PartB = YPA

  #Part C  
  TDPA_one = (int(touchdowns)/int(attempts))
  TDPA = (TDPA_one*20)
  PartC = TDPA

  #Part D 
  IPA_one = (int(interceptions)/int(attempts))
  IPA_two = (IPA_one*25)
  IPA = (2.375 - IPA_two)
  PartD = IPA

  #Stat adjustment
  if PartA < 0:
    PartA = 0
  elif PartA > 2.375:
    PartA = 2.375

  if PartB < 0:
    PartB = 0
  elif PartB > 2.375:
    PartB = 2.375

  if PartC < 0:
    PartC = 0
  elif PartC > 2.375:
    PartC = 2.375

  if PartD < 0:
    PartD = 0
  elif PartD > 2.375:
    PartD = 2.375
  
  # QBR Calcculations
  Total = (PartA+PartB+PartC+PartD)
  QBR_one = (Total/6)
  QBR_two = (QBR_one*100)
  
  rating = QBR_two
  rating = round(rating,4)
  return rating

def ratingCategory(rating):
  if rating < 85:
    RatingCategory = "Bad"
  elif rating <= 90:
    RatingCategory = "Mediocre"
  elif rating <= 95:
    RatingCategory = "Good"
  else:
    RatingCategory = "Great"
  return RatingCategory

def addColumns(fileIn, fileOut,):
  fin = open(fileIn,"r")
  fout = open(fileOut,"w")
  players = {}
  header = fin.readline()
  
  for line in fin:
    section = line.split(",")
    PlayerName = (section[0]+","+section[1])
    FirstName = section[0]
    LastName = section[1]
    Team = section[2]
    Games = section[3]
    Starts = section[4]
    Compleations = section[5]
    Attempts = section[6]
    Yards = section[7]
    TDS = section[8]
    Interceptions = section[9]
    Sacks = section[10]
    QBR = passerRating(Attempts,Compleations,Yards,TDS,Interceptions,)
    Category = ratingCategory(QBR)
    
    
    
#section[0] is their first name section[1] is there last name
    if PlayerName in players.keys():
      continue
    else:
      players[PlayerName] = [str(FirstName),str(LastName),str(Team),int(Games),int(Starts),int(Compleations),int(Attempts),int(Yards),int(TDS),int(Interceptions),int(Sacks),int(QBR),str(Category)]
  fout.write("First,Last,Team,Games,Starts,Completions,Attempts,Yards,TDs,Interceptions,Sacks,QBR,QBR Category\n")
  for k,v in players.items():
    fout.write(str(v)+"\n")
    
addColumns("2017_QB_data.csv", "results.csv",)