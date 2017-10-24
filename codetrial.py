import pickle

class game_info():
    
    def __init__(self):
        self.sound_var=0
        self.effect_var=0
        self.highScore=0
        self.total_score=0
        self.games_played=0
        self.average=0
        self.tools=[]
    def info_update(self):
        pickle.dump(self,open("Data/gameinfo.txt","wb"))

st=game_info()
st.info_update()
st = pickle.load(open("Data/gameinfo.txt","rb"))

print st.sound_var,st.tools,st.total_score


t=game_info()
t.info_update()
t = pickle.load(open("Data/gameinfo.txt","rb"))

print t.sound_var,t.tools,t.total_score

f=open("Data/gameinfo.txt","rb")
for t in f:
    t = pickle.load(open("Data/gameinfo.txt","rb"))
    print t.sound_var,t.tools,t.total_score
