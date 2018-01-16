import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from functools import partial
import time
import numpy as np
import sys,os, cPickle


kivy.require('1.9.0')

global experiment
experiment = "initial_study"

# Initialize Variables
class WisconsinGame(FloatLayout):

    def __init__(self, **kwargs):
        super(WisconsinGame, self).__init__(**kwargs)
        
        self.total_rounds = 63  #total trials
        self.countdown_time = 6 #seconds
        #initial experiments --> major modalities changes randomly
        #final experiments --> modalities change according to more potential modality
        self.score = 0

        self.data = []
        self.choice = ""
        self.clock = 0
        self.round = 0
        self.correct = 0
        #self.errors = 0
        self.major_modality_change_round = 1
        self.persistent_errors = 0
        self.non_persistent_errors = 0
        self.error_persistant = 0

        global response_given 
        response_given = False

        self.valid_response = True

        self.modalities = ["visual","text","audio"]

        self.major_modality = self.modalities[np.random.randint(3)]
        self.major_stimuli = ''
        self.stimuli_type = ''

        
        self.commands_all = {}
        self.commands_all['color'] = ["red","green","blue","yellow","magenta"]
        self.commands_all['number'] = ["one","two","three","four","five"]
        self.commands_all['shape'] = ["circle","triangle","cross","star","heart"]

        self.commands = {}

        self.perm =[]

        self.level = 0 #gamelevel
        self.level_change()
        self.next_round("")

        
#Evaluate answer according to current major modality
    def check_result(self):
        print self.stimuli_type,self.choice
        if self.stimuli_type in ['red','circle','one'] and  self.choice == "b1":
           self.correct += 1  
           self.valid_response = True
           self.error_persistant = 0
        elif self.stimuli_type in ['green','triangle','two'] and  self.choice == "b2":
           self.correct += 1  
           self.valid_response = True
           self.error_persistant = 0
        elif self.stimuli_type in ['blue','cross','three'] and  self.choice == "b3":
            self.correct += 1  
            self.valid_response = True
            self.error_persistant = 0
        elif self.stimuli_type in ['yellow','star','four'] and  self.choice == "b4":
            self.correct += 1  
            self.valid_response = True
            self.error_persistant = 0
        elif self.stimuli_type in ['magenta','heart','five'] and  self.choice == "b5":
            self.correct += 1  
            self.valid_response = True
            self.error_persistant = 0
        else:
            self.valid_response = False
            #self.errors+=1
            if self.round == self.major_modality_change_round +1 or self.round == self.major_modality_change_round:
                self.non_persistent_errors +=1
                self.error_persistant = 1
            else:
                self.persistent_errors +=1
                self.error_persistant = 2

        if self.valid_response == True:
            if self.level == 0 :
                self.score += 1
            elif self.level == 1 :
                self.score += 2
            elif self.level == 2 :
                self.score += 3
            elif self.level == 3 :
                self.score += 4
            elif self.level == 4 :
                self.score += 5
        #print "CORRECT: "+str(self.correct),"NON-PER ERRORS: "+str(self.non_persistent_errors), "PER ERRORS: "+str(self.persistent_errors)

#Change object's opacity
    def chage_opacity(self,wid_id,_):
                self.ids[wid_id].opacity = 0

#Give audiovisual feedback
    def feedback(self):
        if self.valid_response == True:
            self.ids['feedback'].source = "correct.png"
            sound = SoundLoader.load('correct.mp3')     
            sound.play()   
        else:    
            self.ids['feedback'].source = "wrong.png"
            sound = SoundLoader.load('wrong.mp3')     
            sound.play()   
        self.ids['feedback'].opacity = 1
        Clock.schedule_once(partial(self.chage_opacity,'feedback'), 1)

#Capture when a button is pressed
    def button_pressed(self):
        global response_given
        response_given = True

#Start countdouwn
    def countdown(self,_):
         global response_given
         if self.clock >= self.countdown_time: # give error when predifined time has passed and terminate current timer
            self.valid_response = False
            self.persistent_errors += 1
            self.error_persistant = 2
            self.feedback()
            self.data.append([self.round, self.level,self.major_modality,self.major_stimuli, self.stimuli_type,self.valid_response, self.error_persistant ,self.clock, self.choice,self.perm[0],self.perm[1],self.perm[2],self.audio,self.text,self.visual,self.correct,self.non_persistent_errors, self.persistent_errors]) 
            if self.round == self.total_rounds:
                Clock.schedule_once(self.log_and_terminate, 1.5)
            Clock.schedule_once(self.next_round, 1.5)
            return False

         if response_given==True:  #terminate timer when answer is given in time
            return False

         self.clock += 1
         #print self.clock


    def level_change(self):
        print self.commands_all
        ids =  np.random.permutation(5)
        self.level = 0
        while self.level == 0:
            self.level = np.random.randint(5)
        
        if self.level == 4:
            self.commands = dict(self.commands_all)
        elif self.level == 3:
            self.commands['color'] = [self.commands_all['color'][ids[0]],self.commands_all['color'][ids[1]],self.commands_all['color'][ids[2]],self.commands_all['color'][ids[3]]]
            self.commands['shape'] = [self.commands_all['shape'][ids[0]],self.commands_all['shape'][ids[1]],self.commands_all['shape'][ids[2]],self.commands_all['color'][ids[3]]]
            self.commands['number'] = [self.commands_all['number'][ids[0]],self.commands_all['number'][ids[1]],self.commands_all['number'][ids[2]],self.commands_all['color'][ids[3]]]
        elif self.level == 2:
            self.commands['color'] = [self.commands_all['color'][ids[0]],self.commands_all['color'][ids[1]],self.commands_all['color'][ids[2]]]
            self.commands['shape'] = [self.commands_all['shape'][ids[0]],self.commands_all['shape'][ids[1]],self.commands_all['shape'][ids[2]]]
            self.commands['number'] = [self.commands_all['number'][ids[0]],self.commands_all['number'][ids[1]],self.commands_all['number'][ids[2]]]
        elif self.level == 1 :
            self.commands['color'] = [self.commands_all['color'][ids[0]],self.commands_all['color'][ids[1]]]
            self.commands['shape'] = [self.commands_all['shape'][ids[0]],self.commands_all['shape'][ids[1]]]
            self.commands['number'] = [self.commands_all['number'][ids[0]],self.commands_all['number'][ids[1]]]
        elif self.level == 0 :
            self.commands['color'] = [self.commands_all['color'][ids[0]]]
            self.commands['shape'] = [self.commands_all['shape'][ids[0]]]
            self.commands['number'] = [self.commands_all['number'][ids[0]]]
        print
        print "LEVEL: ",self.level+1
        print self.commands
        print


#Draw next round
    def next_round(self,_):
        global response_given
        response_given = False
        self.clock = 0
        Clock.schedule_interval(self.countdown, 1)

        self.round += 1

        # Change Stimuli
        if self.round%8 == 0 and self.valid_response == True:
            tmp = self.major_modality
            while tmp == self.major_modality:
                     self.major_modality = self.modalities[np.random.randint(3)]
                     self.major_modality_change_round = self.round
            self.level_change()
        
        self.perm =  np.random.permutation(self.commands.keys())   
        
        #update stimulis by securing that each stimuli will represent a different button if possible
        mix_the_command = np.random.permutation(self.level+1)
        if len(mix_the_command) >= 3: # in levels 3 and 4 all stimulis are different
            self.text = self.commands[self.perm[1]][mix_the_command[0]]
            self.visual = self.commands[self.perm[2]][mix_the_command[1]]
            self.audio = self.commands[self.perm[0]][mix_the_command[2]]
        elif len(mix_the_command) == 2: #in level two, two of the randomly chosen stimulis represent the same button
            rand = np.random.rand()
            print rand
            if rand <= 0.33:
                self.text = self.commands[self.perm[1]][mix_the_command[0]]
                self.visual = self.commands[self.perm[2]][mix_the_command[0]]
                self.audio = self.commands[self.perm[0]][mix_the_command[1]]
            elif rand <= 0.66:
                self.text = self.commands[self.perm[1]][mix_the_command[1]]
                self.visual = self.commands[self.perm[2]][mix_the_command[0]]
                self.audio = self.commands[self.perm[0]][mix_the_command[0]]
            else:
                self.text = self.commands[self.perm[1]][mix_the_command[0]]
                self.visual = self.commands[self.perm[2]][mix_the_command[1]]
                self.audio = self.commands[self.perm[0]][mix_the_command[0]]
        elif len(mix_the_command) == 1:#in level 1 all stimuli represent the same button
                self.text = self.commands[self.perm[1]][mix_the_command[0]]
                self.visual = self.commands[self.perm[2]][mix_the_command[0]]
                self.audio = self.commands[self.perm[0]][mix_the_command[0]]





        self.ids['visual'].source = ('.').join((self.visual,'jpg'))
        self.ids['text'].text = self.text
        sound = SoundLoader.load(self.audio+'.wav')     
        sound.play()   


        if self.major_modality == 'audio':
            self.major_stimuli = self.perm[0]
            self.stimuli_type = self.audio
        elif self.major_modality == 'text':
            self.major_stimuli = self.perm[1]
            self.stimuli_type = self.text
        else:
             self.major_stimuli = self.perm[2]
             self.stimuli_type = self.visual

        print "Round:",self.round
        print self.major_modality
        print self.major_stimuli
        print self.stimuli_type
        #print ''

#Terminate session function
    def log_and_terminate(self,_):
        global args

        path_save = "Data/"+experiment+"/"  
        path_leaderboard =  "Data/leaderbord.csv"   
        leaderbord_pickle =  "Data/leaderbord"     

        if not os.path.exists(path_save):
            os.makedirs(path_save)
        with open(path_save + args[0]+'_'+args[1]+'_'+str(self.score)+'.csv','w') as f:
                    f.write("Round\tLevel\tModality\tStimuli\tStimuli Type\tResponse\tPersistence\tTime\tButton Pressed\tVoice Stimuli\tText Stimuli\tImage Stimuli\tVoice Choice\tText Choice\tImage Choice\tCorrect\tNON-PER Errors\tPER Errorsn\n")
                    for sample in self.data:
                        f.write((('\t').join([str(i) for i in sample])+'\n'))
        f.close

      # save cpickle file with correct,correct_red,correct_blue
        d={}
        if os.path.isfile(leaderbord_pickle):
            fo = open(leaderbord_pickle, "rb")
            d = cPickle.load(fo)
            fo.close()

        d[args[0]+'_'+args[1]] = self.correct
        fo = open(leaderbord_pickle, "wb")
        cPickle.dump(d, fo, protocol=cPickle.HIGHEST_PROTOCOL)
        fo.close()

        with open(path_leaderboard,'w') as f:
            f.write('ID\tEMAIL\tSCORE\n')
            for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k),reverse=True):
                f.write((('\t').join((key.split('_')[0],key.split('_')[1],str(value)+"\n"))))
            f.close
        
        sys.exit()


#App control function
    def on_control(self,choice):
        self.choice = choice
        self.check_result()
        self.feedback()
        self.data.append([self.round, self.level,self.major_modality,self.major_stimuli, self.stimuli_type,self.valid_response, self.error_persistant, self.clock,self.choice,self.perm[0],self.perm[1],self.perm[2],self.audio,self.text,self.visual,self.correct,self.non_persistent_errors, self.persistent_errors]) 
        # terminate session when round limit has been reached
        print self.score
        if self.round >= self.total_rounds:
            Clock.schedule_once(self.log_and_terminate, 1.5)
        Clock.schedule_once(self.next_round, 1.5)
       

class WisconsinApp(App):
    def build(self):
        return WisconsinGame()



if __name__ == '__main__':
    global args, data
    print "User: "+sys.argv[1], "Email: "+ sys.argv[2]
    args = sys.argv[1:]
    #with open(args[1]+'.csv','w') as f
    #close.f
    WisconsinApp().run()




