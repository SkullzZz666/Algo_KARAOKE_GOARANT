#définition des classes
class Karaoke:
    def init(self, nombrechansons, nombrejoueurs):
        self.listchansons = nombrechansons
        self.listejoeurs = nombrejoueurs
        
    def getScoreRecordKaraoke(self):
        ScoreRecordKaraoke = 0
        
        
class Player:
    def init(self, pseudo, chanson0, chanson1, chanson2, chanson3, chanson4):
        self.nom = pseudo
        self.score = chanson0,chanson1,chanson2,chanson3,chanson4
        
    
    
    #affiche le meilleur score et les chansons
    def getScoreRecord(self, score):
        scorerecord = 0
        chanson = -1
        for i in range(self.score):
            if self.score[i] > scorerecord:
                scorerecord = score
        for i in range(self.score):
            if scorerecord > self.score:
                chanson = i
        print(chanson)
        print (scorerecord)
        return scorerecord
    
    
    #affiche la moyenne du score des joueu(s(es))r(s)
    def getMoyenne (self, score):
        moyennescore=0
        for i in range(self.score):
            moyennescore = 0
            for i in range(self.score):
                moyennescore += self.score[i]
            moyennescore = moyennescore/5
            print(moyennescore)
            return moyennescore 
        
    
    #affiche le pire score des joueu(s(es))r(s)
    def getPireScore (self, score):
        pirescore = 100
        for i in range(self.score):
            if score[i] < pirescore:
                pirescore = self.score[i]
            print("votre pire score est: ",pirescore)
            return pirescore
        
    
    #affiche le score des joueu(s(es))r(s)
    def getScore(self, score):
        for i in range (self.score):
            print (self.score[i])
            
    
    #affiche le nouveau meilleur score des joueu(se(s))((r)s)
    def nouveauMeilleurScore (self, score):
        chansonAModifier = int(input("Voici la chanson qui sera modifier: \n"))
        ScoreAModifier = int(input("Voici votre nouveau meilleur score: \n"))
        for i in range(self.score):
            if i == chansonAModifier:
                self.score[i] = ScoreAModifier


        