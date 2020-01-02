from random import randrange #start with some import functions
import matplotlib.pyplot as plt
import numpy as np
#TO ADD [more teams? Fix names, more graphics?]
shot_count_list1 = []
shot_count_list2 = []
list1 = []
list2 = []
class Ball: #use this class to define the functions shot and three
    shotcount1 = 0 #these act as my score and shot counters
    shotcount2 = 0
    fieldgoalm1 = 0
    fieldgoalm2 = 0
    count_team1 = 0
    count_team2 = 0
    list1 = []
    list2 = []
    def __init__(self, player, team, close, deep):
        self.player = player
        self.team = team
        self.close = close
        self.deep = deep
    def dunk(self): #for the cpu who scores and for how much
            probability1 = (randrange(100))
            if self.team == 'home':
                Ball.shotcount1 += 1
                shot_count_list1.append(Ball.shotcount1)
                if probability1 < int(self.close):
                    Ball.count_team1 += 2
                    Ball.fieldgoalm1 += 1
                    print("Slam dunk by", self.player)
                    list1.append(Ball.count_team1)
                    print("The score is", Ball.count_team1, "to", Ball.count_team2)
                else:
                    list1.append(Ball.count_team1)
                    print("Oh no.", self.player, "missed the dunk.")
                    print("The score is", Ball.count_team1, " to", Ball.count_team2)
            elif self.team == 'away':
                Ball.shotcount2 += 1
                shot_count_list2.append(Ball.shotcount2)
                if probability1 < int(self.close):
                    Ball.count_team2 += 2
                    Ball.fieldgoalm2 += 1
                    print("Slam dunk by", self.player)
                    list2.append(Ball.count_team2)
                    print("The score is", Ball.count_team1, "to", Ball.count_team2)
                else:
                    list2.append(Ball.count_team2)
                    print("Oh no.", self.player, "missed the dunk.")
                    print("The score is", Ball.count_team1, " to", Ball.count_team2)

    def three(self):
        probability1 = (randrange(100))
        if self.team == 'home':
            Ball.shotcount1 += 1
            shot_count_list1.append(Ball.shotcount1)
            if probability1 < int(self.deep):
                Ball.count_team1 += 3
                Ball.fieldgoalm1 += 1
                list1.append(Ball.count_team1)
                print("Three pointer by", self.player)
            else:
                print ("Three pointer missed by", self.player)
                list1.append(Ball.count_team1)
            print("The score is", Ball.count_team1, " to", Ball.count_team2)
        elif self.team == 'away':
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            if probability1 < int(self.deep):
                Ball.count_team2 += 3
                Ball.fieldgoalm2 += 1
                list2.append(Ball.count_team2)
                print("Three pointer by", self.player)
            else:
                list2.append(Ball.count_team2)
                print ("Three pointer missed by", self.player)
            print("The score is", Ball.count_team1, "to", Ball.count_team2)

shot_count1 = int(Ball.shotcount1)
shot_count2 = int(Ball.shotcount2)
score1 = int(Ball.count_team1)
score2 = int(Ball.count_team2)
#here are our objects, need these to get function out of the user inputs
lebron_james = Ball(player='Lebron', team='home', close=92, deep=63)
anthony_davis = Ball(player='Anthony', team='home', close=90, deep=60)
stephen_curry = Ball(player='Steph', team='away', close=82, deep=84)
klay_thompson = Ball(player='Klay', team ='away', close=76, deep=83)
kyrie_irving = Ball(player='Kyrie', team ='home', close=85, deep=65)
kevin_durant = Ball(player='Kevin', team ='home', close=88, deep=75)
kawhi_leonard = Ball(player='Kawhi', team ='away', close=90, deep=70)
paul_george = Ball(player='Paul', team ='away', close=84, deep=78)
luka_doncic = Ball(player='Luka', team ='home', close=85, deep=80)
kristaps_porzingis = Ball(player='Kristaps', team='home', close=88, deep=79)
joel_embiid = Ball(player='Joel', team='away', close=91, deep=58)
ben_simmons = Ball(player='Ben', team='away', close=90, deep=60)

players = {"stephen_curry":stephen_curry,"lebron_james":lebron_james,
"klay_thompson":klay_thompson,"anthony_davis":anthony_davis,
"kyrie_irving":kyrie_irving, "kevin_durant":kevin_durant,
"kawhi_leonard":kawhi_leonard, "paul_george":paul_george,
"luka_doncic":luka_doncic, "kristaps_porzingis":kristaps_porzingis,
"ben_simmons":ben_simmons, "joel_embiid":joel_embiid}
player_pool_dic = {"Warriors": ("Stephen Curry", "Klay Thompson"),
                   "Lakers": ("Anthony Davis", "Lebron James"),
                  "Nets": ("Kyrie Irving", "Kevin Durant"),
                  "Clippers": ("Kawhi Leonard", "Paul George"),
                  "Mavs": ("Luka Doncic", "Kristaps Porzingis"),
                  "Sixers": ("Ben Simmons", "Joel Embiid")}
print("Pick a team: Warriors, Lakers, Clippers, Nets, Sixers, or Mavs!")
user_team = input("Capitalize the first letter. First one to 20 wins ")
while score1 >= 25 or score2 >= 25:
    shot_select = input("Would you like to shoot a three or a dunk ")
    if shot_select == "three":
        players[shot_taker].three()
    elif shot_select == "dunk":
        players[shot_taker].dunk()
    else:
        print("Not an accepted shot type ")

if str(user_team) == "Warriors":
    print(player_pool_dic["Warriors"])
    user_player = "0"
    shot_taker = "0"
    while str(user_player) != "Stephen" or user_player != "Klay":
        user_player = input("Choose a player, ")
        if str(user_player) == "Stephen":
            print("You have selected Steph Curry")
            shot_taker = ("stephen_curry")
            break
        elif str(user_player) == "Klay":
            print("You have selected Klay Thompson")
            shot_taker = ("klay_thompson")
            break
        else:
            print("Please only use their full first name. Capitalize the first letter ")
    while score1 <= 20 and score2 <= 20:
        shot_select = input("Would you like to shoot a [three] or a [dunk] or [change] player? ")
        if shot_select == "three":
            players[shot_taker].three()
        elif shot_select == "dunk":
            players[shot_taker].dunk()
        elif shot_select == "change":
            Ball.shotcount2 += 1 #needed to add a feature to change players in
            shot_count_list2.append(Ball.shotcount2) #the middle of the game
            list2.append(Ball.count_team2)
            print(player_pool_dic['Warriors'])
            user_player = input("Choose a player, first name only ")
            if str(user_player) == "Stephen" or str(user_player) == "stephen":
                print("You have selected stephen_curry")
                shot_taker = ("stephen_curry")
            elif str(user_player) == "Klay" or str(user_player) == "klay":
                print("You have selected Klay Thompson")
                shot_taker = ("klay_thompson")
            else: #if you spell wrong you get a turnover, I think its fair
                print("Not the first name, Turnover!")
        else: #now we run the same portion the user chose, except based off of rng
            list2.append(Ball.count_team2)
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            print("Not an accepted shot type ")
        probability2 = (randrange(100))
        probability3 = (randrange(100))
        if probability2 >= 50:
            shot_taker2 = "lebron_james"
            if probability3 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        else:
            shot_taker2 = "anthony_davis"
            if probability2 <= 50:
                players[shot_taker2].three() #the whole thing runs for a cpu team
            else:
                players[shot_taker2].dunk()
        if Ball.count_team1 >= 20 or Ball.count_team2 >= 20:
            print("Good Game, the final score was Lakers-", Ball.count_team1, \
            "to Warriors-", Ball.count_team2) #we print out a plot of both teams
            plt.plot(shot_count_list1, list1, color='purple')
            plt.plot(shot_count_list2, list2, color='blue')
            plt.ylabel('Points')
            plt.xlabel('Possessions')
            plt.title('Lakers(purple) vs. Warriors(blue)')
            plt.show()
            fgpercent2 = Ball.fieldgoalm2 / Ball.shotcount2
            print("The Warriors shot", Ball.fieldgoalm2, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent2, 2)*100, "%")
            fgpercent1 = Ball.fieldgoalm1 / Ball.shotcount1
            print("The Lakers shot", Ball.fieldgoalm1, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent1, 2)*100, "%")
            break
#I have the same functions running as an if for the Lakers, Clippers, and Nets
elif str(user_team) == "Lakers": #only difference is I change the names
    print(player_pool_dic["Lakers"])
    user_player = "0"
    shot_taker = "0"
    while str(user_player) != "Lebron" or user_player != "Anthony":
        user_player = input("Choose a player, ")
        if str(user_player) == "Lebron" or str(user_player) == 'lebron':
            print("You have selected Lebron James")
            shot_taker = ("lebron_james")
            break
        elif str(user_player) == "Anthony" or str(user_player) == 'anthony':
            print("You have selected Anthony Davis")
            shot_taker = ("anthony_davis")
            break
        else:
            print("Please only use their full first name,")
    while Ball.count_team1 <= 20 and Ball.count_team2 <= 20:
        shot_select = input("Would you like to shoot a [three] or a [dunk], or [change] player? ")
        if shot_select == "three":
            players[shot_taker].three()
        elif shot_select == "dunk":
            players[shot_taker].dunk()
        elif shot_select == "change":
            Ball.shotcount1 += 1
            shot_count_list1.append(Ball.shotcount1)
            list1.append(Ball.count_team1)
            print(player_pool_dic['Lakers'])
            user_player = input("Choose a player, ")
            if str(user_player) == "Lebron" or str(user_player) == "lebron":
                print("You have selected Lebron James")
                shot_taker = ("lebron_james")
            elif str(user_player) == "Anthony" or str(user_player) == "anthony":
                print("You have selected Anthony Davis")
                shot_taker = ("anthony_davis")
            else:
                print("Not the right name. Turnover!")
        else: #because of the home/away system I had to switch opponents for
            list2.append(Ball.count_team2)#each team
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            print("Not an accepted shot type. Turnover ")
        probability2 = (randrange(100))
        probability3 = (randrange(100))
        if probability2 >= 50:
            shot_taker2 = "kawhi_leonard"
            if probability3 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        else:
            shot_taker2 = "paul_george"
            if probability2 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        if Ball.count_team1 >= 20 or Ball.count_team2 >= 20:
            print("The final score was Lakers-", Ball.count_team1, " Clippers-", Ball.count_team2)
            plt.plot(shot_count_list1, list1, color='purple')
            plt.plot(shot_count_list2, list2, color='red')
            plt.ylabel('Points')
            plt.xlabel('Possessions')
            plt.title('Lakers(purple) vs. Clippers(red)')
            plt.show()
            fgpercent1 = Ball.fieldgoalm1 / Ball.shotcount1
            print("The Lakers shot", Ball.fieldgoalm1, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent1, 2)*100, "%")
            fgpercent2 = Ball.fieldgoalm2 / Ball.shotcount2
            print("The Clippers shot", Ball.fieldgoalm2, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent2, 2)*100, "%")
            break

if str(user_team) == "Clippers":
    print(player_pool_dic["Clippers"])
    user_player = "0"
    shot_taker = "0"
    while str(user_player) != "Kawhi" or user_player != "Paul":
        user_player = input("Choose a player, ")
        if str(user_player) == "Kawhi" or str(user_player) == "kawhi":
            print("You have selected Kawhi Leonard")
            shot_taker = ("kawhi_leonard")
            break
        elif str(user_player) == "Paul" or str(user_player) == "paul":
            print("You have selected Paul George")
            shot_taker = ("paul_george")
            break
        else:
            print("Please only use their full first name ")
    while Ball.count_team1 <= 20 and Ball.count_team2 <= 20:
        shot_select = input("Would you like to shoot a [three] or a [dunk], or [change] player? ")
        if shot_select == "three":
            players[shot_taker].three()
        elif shot_select == "dunk":
            players[shot_taker].dunk()
        elif shot_select == "change":
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            list2.append(Ball.count_team2)
            print(player_pool_dic['Clippers'])
            user_player = input("Choose a player, ")
            if str(user_player) == "Kawhi" or str(user_player) == "kawhi":
                print("You have selected Kawhi Leonard")
                shot_taker = ("kawhi_leonard")
            elif str(user_player) == "Paul" or str(user_player) == "paul":
                print("You have selected Paul George")
                shot_taker = ("paul_george")
            else:
                print("Not a first name. Turnover!")
        else:
            list2.append(Ball.count_team2)
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            print("Not an accepted shot type, Turnover ")
        probability2 = (randrange(100))
        probability3 = (randrange(100))
        if probability2 >= 50:
            shot_taker2 = "kyrie_irving"
            if probability3 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        else:
            shot_taker2 = "kevin_durant"
            if probability2 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        if Ball.count_team1 >= 20 or Ball.count_team2 >= 20:
            print("Good Game! The final score was Nets-", Ball.count_team1, "Clippers -", Ball.count_team2)
            plt.plot(shot_count_list1, list1, color='black')
            plt.plot(shot_count_list2, list2, color='red')
            plt.ylabel('Points')
            plt.xlabel('Possessions')
            plt.title('Nets(black) vs. Clippers(red)')
            plt.show()
            fgpercent2 = Ball.fieldgoalm2 / Ball.shotcount2
            print("The Clippers shot", Ball.fieldgoalm2, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent2, 2)*100, "%")
            fgpercent1 = Ball.fieldgoalm1 / Ball.shotcount1
            print("The Nets shot", Ball.fieldgoalm1, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent1, 2)*100, "%")
            break

if str(user_team) == "Nets":
    print(player_pool_dic["Nets"])
    user_player = "0"
    shot_taker = "0"
    while str(user_player) != "Kyrie" or user_player != "Kevin":
        user_player = input("Choose a player, ")
        if str(user_player) == "Kyrie" or str(user_player) == "kyrie":
            print("You have selected Kyrie Irving")
            shot_taker = ("kyrie_irving")
            break
        elif str(user_player) == "Kevin" or str(user_player) == 'snek' or str(user_player) == 'kevin':
            print("You have selected Kevin Durant")
            shot_taker = ("kevin_durant")
            break
        else:
            print("Please only use their full first name, or call kd snek ")
    while Ball.count_team1 <= 20 and Ball.count_team2 <= 20:
        shot_select = input("Would you like to shoot a [three] or a [dunk], or [change] player? ")
        if shot_select == "three":
            players[shot_taker].three()
        elif shot_select == "dunk":
            players[shot_taker].dunk()
        elif shot_select == "change":
            Ball.shotcount1 += 1
            shot_count_list1.append(Ball.shotcount1)
            list1.append(Ball.count_team1)
            print(player_pool_dic['Nets'])
            user_player = input("Choose a player, ")
            if str(user_player) == "Kyrie" or str(user_player) == "kyrie":
                print("You have selected Kyrie Irving")
                shot_taker = ("kyrie_irving")
            elif str(user_player) == "Kevin" or str(user_player) == "kevin" or str(user_player) == "snek":
                print("You have selected Kevin Durant")
                shot_taker = ("kevin_durant")
            else:
                print("Not a first name. Turnover!")
        else:
            list2.append(Ball.count_team2)
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            print("Not an accepted shot type, Turnover! ")
        probability2 = (randrange(100))
        probability3 = (randrange(100))
        if probability2 >= 50:
            shot_taker2 = "stephen_curry"
            if probability3 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        else:
            shot_taker2 = "klay_thompson"
            if probability2 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        if Ball.count_team1 >= 20 or Ball.count_team2 >= 20:
            print("Good Game, the final score was Nets-", Ball.count_team1, "Warriors-", Ball.count_team2)
            plt.plot(shot_count_list1, list1, color='black')
            plt.plot(shot_count_list2, list2, color='blue')
            plt.ylabel('Points')
            plt.xlabel('Possessions')
            plt.title('Nets(black) vs. Warriors(blue)')
            plt.show()
            fgpercent2 = Ball.fieldgoalm2 / Ball.shotcount2
            print("The Warriors shot", Ball.fieldgoalm2, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent2, 2)*100, "%")
            fgpercent1 = Ball.fieldgoalm1 / Ball.shotcount1
            print("The Nets shot", Ball.fieldgoalm1, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent1, 2)*100, "%")
            break

if str(user_team) == "Mavs":
  print(player_pool_dic["Mavs"])
  user_player = "0"
  shot_taker = "0"
  while str(user_player) != "Luka" or user_player != "Kristaps":
      user_player = input("Choose a player, ")
      if str(user_player) == "Luka":
        print("You have selected Luka Donic")
        shot_taker = ("luka_doncic")
        break
      elif str(user_player) == "Kristaps":
        print("You have selected Kristaps Porzingis")
        shot_taker = ("kristaps_porzingis")
        break
      else:
          print("Please only use their full first name. Capitalize the first letter ")
  while score1 <= 20 and score2 <= 20:
      shot_select = input("Would you like to shoot a [three] or a [dunk] or [change] player? ")
      if shot_select == "three":
          players[shot_taker].three()
      elif shot_select == "dunk":
          players[shot_taker].dunk()
      elif shot_select == "change":
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            list2.append(Ball.count_team2)
            print(player_pool_dic['Mavs'])
            user_player = input("Choose a player, first name only ")
            if str(user_player) == "Luka" or str(user_player) == "luka":
                print("You have selected Luka Doncic")
                shot_taker = ("luka_doncic")
            elif str(user_player) == "Kristaps" or str(user_player) == "kristaps" or str(user_player) == "tingus pingus":
                print("You have selected Kristaps Porzingis")
                shot_taker = ("kristaps_porzingis")
            else:
                print("Not the first name, Turnover!")
      else:
          list2.append(Ball.count_team2)
          Ball.shotcount2 += 1
          shot_count_list2.append(Ball.shotcount2)
          print("Not an accepted shot type ")
      probability2 = (randrange(100))
      probability3 = (randrange(100))
      if probability2 >= 50:
          shot_taker2 = "ben_simmons"
          if probability3 <= 88:
              players[shot_taker2].three()
          else:
              players[shot_taker2].dunk()
      else:
          shot_taker2 = "joel_embiid"
          if probability2 <= 50:
              players[shot_taker2].three() #the whole thing runs for a cpu team
          else:
              players[shot_taker2].dunk()
      if Ball.count_team1 >= 20 or Ball.count_team2 >= 20:
          print("Good Game, the final score was Mavs-", Ball.count_team1, \
          "to Sixers-", Ball.count_team2) #we print out a plot of both teams
          plt.plot(shot_count_list1, list1, color='blue')
          plt.plot(shot_count_list2, list2, color='red')
          plt.ylabel('Points')
          plt.xlabel('Possessions')
          plt.title('Sixers(red) vs. Mavs(blue)')
          plt.show()
          fgpercent2 = Ball.fieldgoalm2 / Ball.shotcount2
          print("The Sixers shot", Ball.fieldgoalm2, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent2, 2)*100, "%")
          fgpercent1 = Ball.fieldgoalm1 / Ball.shotcount1
          print("The Mavs shot", Ball.fieldgoalm1, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent1, 2)*100, "%")
          break

if str(user_team) == "Sixers":
    print(player_pool_dic["Sixers"])
    user_player = "0"
    shot_taker = "0"
    while str(user_player) != "Ben" or user_player != "Joel":
        user_player = input("Choose a player, ")
        if str(user_player) == "Ben":
            print("You have selected Ben Simmons")
            shot_taker = ("ben_simmons")
            break
        elif str(user_player) == "Joel":
            print("You have selected Joel Embiid")
            shot_taker = ("joel_embiid")
            break
        else:
            print("Please only use their full first name. Capitalize the first letter ")
    while score1 <= 20 and score2 <= 20:
        shot_select = input("Would you like to shoot a [three] or a [dunk] or [change] player? ")
        if shot_select == "three":
            players[shot_taker].three()
        elif shot_select == "dunk":
            players[shot_taker].dunk()
        elif shot_select == "change":
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            list2.append(Ball.count_team2)
            print(player_pool_dic['Sixers'])
            user_player = input("Choose a player, first name only ")
            if str(user_player) == "Ben" or str(user_player) == "ben":
                print("You have selected Ben Simmons")
                shot_taker = ("ben_simmons")
            elif str(user_player) == "Joel" or str(user_player) == "joel":
                print("You have selected Joel Embiid")
                shot_taker = ("joel_embiid")
            else:
                print("Not the first name, Turnover!")
        else:
            list2.append(Ball.count_team2)
            Ball.shotcount2 += 1
            shot_count_list2.append(Ball.shotcount2)
            print("Not an accepted shot type ")
        probability2 = (randrange(100))
        probability3 = (randrange(100))
        if probability2 >= 50:
            shot_taker2 = "luka_doncic"
            if probability3 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        else:
            shot_taker2 = "kristaps_porzingis"
            if probability2 <= 50:
                players[shot_taker2].three()
            else:
                players[shot_taker2].dunk()
        if Ball.count_team1 >= 20 or Ball.count_team2 >= 20:
            print("Good Game, the final score was Mavs-", Ball.count_team1, \
            "to Sixers-", Ball.count_team2) #we print out a plot of both teams
            plt.plot(shot_count_list1, list1, color='blue')
            plt.plot(shot_count_list2, list2, color='red')
            plt.ylabel('Points')
            plt.xlabel('Possessions')
            plt.title('Sixers(red) vs. Mavs(blue)')
            plt.show()
            fgpercent2 = Ball.fieldgoalm2 / Ball.shotcount2
            print("The Sixers shot", Ball.fieldgoalm2, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent2, 2)*100, "%")
            fgpercent1 = Ball.fieldgoalm1 / Ball.shotcount1
            print("The Mavs shot", Ball.fieldgoalm1, "for", Ball.shotcount2,". Their field goal percentage was", round(fgpercent1, 2)*100, "%")
            break
else:
    print("Good game. Please play again.")
