#!python
#!/usr/bin/env python

from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics.instructions import CanvasBase
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


Builder.load_string('''
#template for menu items
[ListButton@ToggleButton]
    background_normal: 'button_normal_cmenu.jpg'
    background_down: 'button_normal_cmenu_d.jpg'
    #background_color: ctx.background_color if hasattr(ctx, 'background_color') else [1, 1, 1, 1]
    group: 'context_menue_root'
    on_release: ctx.on_release(self) if hasattr(ctx, 'on_release') else None
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    width: ctx.width if hasattr(ctx, 'width') else 1
    text: ctx.text if hasattr(ctx, 'text') else ''
    

<Button>:
    font_size: self.texture_size[1]/5 
    size_hint: 0.25,0.130
    color: (0, 0, 0, 1)
    #background_color: (0.81, 0.20, 0.81, 1)
    #width: self.texture_size[0]
    #height: self.texture_size[1]
    text_size: self.width,self.height
    halign: 'center'
    valign: 'middle'
    background_down: 'button_down.png'
    #background_down: 'atlas://data/images/defaulttheme/bubble_btn'
    background_normal: 'button_normal.jpg'
    markup: True

<MainScreen>
    id: "main"
    pos_hint: {"right":1,"top":1} 
    size_hint: 0.75, 1
    canvas:
        Rectangle:
            source: 'main_canvas2.jpg'
            pos: self.pos
            size: self.size
   
<ScrollableLabel>
    


<MainMenu>
    canvas:
        Rectangle:
            source: 'button_back.jpg'
            pos: self.pos
            size: self.size
    
    MainScreen:
        Label:
            id: label1
            text:"ATEC" 
            text_size: root.width-root.width*0.45,  root.height-root.height*0.1
            font_size: self.texture_size[1]/20 
            size: self.texture_size
            pos_hint: {"right":0.92,"top":1} 
            color: (1, 0, 1, 1)
            halign: 'left'
            valign: 'top'
        
        Label:
            id: label2
            text: "General-Instructions"
            text_size: root.width-root.width*0.45,  root.height-root.height*0.1
            font_size: self.texture_size[1]/22 
            size: self.texture_size
            pos_hint: {"right":0.92,"top":0.87} 
            color: (1, 1, 0, 0.9)
            halign: 'left'
            valign: 'top'
        
        ScrollableLabel
            pos_hint: {"right":0.8,"top":0.7} 
            
            Label:
                id:label3
                text:"[b][color=#FF0000]INTRODUCTION:[/color][/b]\\n[i][color=#FFA500][Begin with child standing.][/color][/i]\\n\\n[color=#FF0000]SCRIPT[/color]:\\nWe are going to play games today that involve using your body in lots of different ways.\\n\\nSometimes, you will do movements that are familiar to you; sometimes you will do movements you may not have done before.\\n\\nWe will always make sure to tell you exactly what to do and sometimes we will show you how to do them. And we always play safe.\\n\\nAre you ready to play the games?\\n\\n\\n\\n\\n"
                text_size: root.width-root.width*0.7, None
                font_size: 30 
                #size: self.texture_size
                size_hint_y: None
                height:self.texture_size[1]
                color: (1, 1, 1, 1)
                halign: 'left'
                valign: 'top'
                markup: True

               

        Button:
            #text: "START"
            on_release:  root.on_control(args[0],"start")
            pos_hint: {"right":1,"top":0.8} 
            background_normal: "start2.png"
            size_hint: 0.1,0.1
            background_down: 'record_pressed.png'

        Button:
            #text: "PAUSE"
            on_release:  root.on_control(args[0],"pause")
            pos_hint: {"right":1,"top":0.6}   
            background_normal: "pause.png"
            size_hint: 0.1,0.1
            background_down: 'pause_pressed.png'

        Button:
            #text: "STOP"
            on_release:  root.on_control(args[0],"stop")
            pos_hint: {"right":1,"top":0.4}  
            background_normal: "stop.png"
            size_hint: 0.1,0.1
            background_down: 'stop_pressed.png'

        Button:
            #text: "Task Copleted"
            on_release:  root.on_control(args[0],"complete")
            pos_hint: {"right":1,"top":1}  
            background_normal: "complete2.png"
            background_down: 'complete.png'
            size_hint: 0.1,0.1

        Button:
            #text: "HELP"
            on_release:  root.on_control(args[0],"help")
            pos_hint: {"right":0.99,"top":0.12}  
            background_normal: "help2.png"
            size_hint: 0.08,0.08
            background_down: 'help.png'

        
        

    Button:
        id: "sdsd"
        text: "Gross Motor \\nGait and Balance"
        on_release:  root.add_menu(args[0],1)
        pos_hint: {"right":0.25,"top":1}  


    Button:
        on_release:  root.add_menu(args[0],2)
        text: "Synchronous Movements"
        pos_hint: {"right":0.25,"top":0.873}

    Button:
        on_release:  root.add_menu(args[0],3)
        text: "Bilateral Coordination &\\n Response Inhibition"
        pos_hint: {"right":0.25,"top":0.745}

    Button:
        on_release:  root.add_menu(args[0],4)
        text: "Bilateral Coordination &\\n Response Inhibition \\n([color=#FF0000]Red[/color]/[color=#00FF00]Green[/color] Light)"
        pos_hint: {"right":0.25,"top":0.620}

    Button:
        on_release:  root.add_menu(args[0],5)
        text: "Visual Response\\n Inhibition"
        pos_hint: {"right":0.25,"top":0.495}

    Button:
        on_release:  root.add_menu(args[0],6)
        text: "Cross Body Game"
        pos_hint: {"right":0.25,"top":0.370}

    Button:
        on_release:  root.add_menu(args[0],7)
        text: " Finger-Nose\\n Coordination"
        pos_hint: {"right":0.25,"top":0.245}

    Button:
        on_release:  root.add_menu(args[0],8)
        text: "Rapid Sequential\\n Movements"
        pos_hint: {"right":0.25,"top":0.120}



<Cmenu1>
    id:t11
    size_hint: 0.41, 0.6
    pos_hint: {"right":0.65,"top":1}
    padding: 0.005
    #background_color: 1, 0, 0, 1
    
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Natural Walk'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Gait on Toes'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Tandem Gain'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Stand eyes closed hands outstretched'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Stand on One Foot'
                        on_release: root.menu_selected


<Cmenu2>
    size_hint: 0.41, 0.3
    pos_hint: {"right":0.65,"top":0.87}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'March Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'March Fast'
                        on_release: root.menu_selected
                       

<Cmenu3>
    size_hint: 0.41, 0.3
    pos_hint: {"right":0.65,"top":0.75}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Bi-manual Bag Pass Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Bi-manual Bag Pass Fast'
                        on_release: root.menu_selected

<Cmenu4>
    size_hint: 0.41, 0.6
    pos_hint: {"right":0.65,"top":0.62}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Red Light/Green Light -- Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light -- Fast'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Slow'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Fast'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Red Light/Green Light/Yellow Light -- Visual Slow'
                        on_release: root.menu_selected

<Cmenu5>
    size_hint: 0.41, 0.16
    pos_hint: {"right":0.65,"top":0.50}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: ' A sailor went to Sea, Sea, Sea '
                        on_release: root.menu_selected

<Cmenu6>
    size_hint: 0.41, 0.35
    pos_hint: {"right":0.65,"top":0.37}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Cross Body Ears - Knees'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Cross Body Shoulders = Cross Body Hips'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Combined Reverse Actions'
                        on_release: root.menu_selected


<Cmenu7>
    size_hint: 0.41, 0.15
    pos_hint: {"right":0.65,"top":0.25}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Finger-Nose Coordination'
                        on_release: root.menu_selected

<Cmenu8>
    size_hint: 0.41, 0.7
    pos_hint: {"right":0.65,"top":0.68}
    padding: .005
    background_color: 1, 0, 0, 1
    orientation: 'vertical'
    BoxLayout:
        padding: 5
        ScrollView:
            BoxLayout:
                size_hint: 1, 1
                width: root.width * 2 - 40
                #root menu add/edit items here to show them in root menu
                BoxLayout:
                    orientation: 'vertical'
                    ListButton:
                        text: 'Foot Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Foot-Heel-Toe Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hand Pat'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Hand Pronate/supinate'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Finger Tap'
                        on_release: root.menu_selected
                    ListButton:
                        text: 'Appose Finger Succession'
                        on_release: root.menu_selected                 
''')

global tast,text
text =""
task=''


intro= """[b][color=#FF0000]INTRODUCTION:[/color][/b]\n[i][color=#FFA500][Begin with child standing.][/color][/i]\n\n[color=#FF0000]SCRIPT[/color]:\nWe are going to play games today that involve using your body in lots of different ways.
\nSometimes, you will do movements that are familiar to you; sometimes you will do movements you may not have done before.
\nWe will always make sure to tell you exactly what to do and sometimes we will show you how to do them. And we always play safe.
\nAre you ready to play the games?\n\n\n\n
"""

t11 = """[color=#FF0000]SCRIPT[/color]:\nNow show me how you can walk straight, turn around and come back.\nKeep your hands by your side and walk naturally.\nI will count your steps for you.\n[i][color=#FFA500][Do not demonstrate][/i][/color]\n\n
[color=#FF0000]SCORE[/color]:
Raw Score and converted score are the same: Falling = 0
Awkward gait, asymmetry of arms and legs = 1
Normal even with exaggerations, wriggling etc...= 2
\n\n\n\n
"""

t12 = """[color=#FF0000]SCRIPT[/color]:
Good. Now I want you to walk forward 8 steps on your toes.
Don't walk on your tippy toes, like you are in the ballet, just on the balls of your feet with your heel off the ground, medium toes.
Keep your hands at your sides.
Let me show you.
[i][color=#FFA500][Demonstrate:  Walk with arms at side, walking on balls of feet.][/i][/color]
Are you ready?  I will count your steps for you.

[color=#FF0000]SCORE[/color]:
Raw Score = number of steps on toes out of eight.
Fewer than 4 steps = 0
4-6 = 1
7-8 = 2
\n\n\n\n\n\n
"""

t13="""[color=#FF0000]SCRIPT[/color]:
You're doing great.
Now, try walking in a straight line by putting one foot right in front of the other, so the heel of your foot touches the toe of the other foot.
Then you step forward again touching the heel of one foot to the toe of the other.
Don't leave any space between your feet, don't step to the side of your foot, and don't step on your foot.
Let me show you[i][color=#FFA500][Demonstrate][/i][/color].
Now walk 8 steps that way. I will count your steps for you.

[color=#FF0000]SCORE[/color]: 
Raw Score = Total correct steps.
Fewer than 4 steps = 0
4-6 steps = 1
7-8 steps = 2
\n\n\n\n\n\n
"""

t14="""[color=#FF0000]SCRIPT[/color]:
Now I want you to stand still with your eyes closed and your arms outstretched.
Put your feet next to each other, close side-by-side, raise your arms level with shoulders and spread all your fingers apart; now close your eyes, and stay as still as you can like this for until I say 'Relax'. 
[i][color=#FFA500][Demonstrate stance, arms up and straight out at shoulder level, fingers abducted, eyes closed.Time with stopwatch for the duration of success or up to 10 sec. Watch for involuntary movements.][/i][/color]

[color=#FF0000]SCORE[/color]: 
Raw Score = Total seconds without losing balance (slight swaying is allowed)
Less than 5 sec = 0
5 to 8 seconds = 1
9-10 second = 2
\n\n\n\n\n\n
"""


t15="""[color=#FF0000]SCRIPT[/color]:
Now I want you to stand on one leg until I tell you to relax. Now I want you to stand on the other leg.
[i][color=#FFA500][Demonstrate balance by standing on one leg with arms relaxed at side and one leg lifted off floor, bent back at knee.If the child compensates, (for example, child may put the other foot down briefly to get balance and try again), have them do it again. Repeat with other foot.][/i][/color] 

[color=#FF0000]SCORE[/color]: 
Raw Score = Total seconds without losing balance (use the longest time in position within the 10 seconds).
Less than 5 sec = 0
5 to 8 seconds = 1
9-10 second = 2

Right foot score 
Left foot score
\n\n\n\n\n\n
"""
t21="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]We're going to play a marching game. 
When you march, move forward raising your knees and lifting and swinging your arms.  
Now I am going to show you how I march.  
When I am done, I will ask you to do it the way I showed you.
[i][color=#FFA500][See video demonstration.][/i][/color]

Great.  Now show me how you do it.
[i][color=#FFA500][Offer any corrective suggestion and repeat demonstration and practice if needed][/i][/color]
[/color]

[color=#FF0000]SCRIPT[/color]: 
Now its your turn to march to the beat. 
Try marching 8 steps with the video. 
Remember, you are trying to march to the beat...Great job.


Trial 1: 
[color=#FF0000]SCRIPT[/color]:
Now, it's your turn to march on your own. 
I am going to play the drum sound for you and you march exactly to the beat. 
Stand up tall and use your arms. 
Remember your foot hits the ground on each beat. 
Ready? 1,2,3, Go.

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of steps in rhythm with opposite arm swings
0-2 beats correct = 0
3-5 beats correct = 1
6-8 beats correct = 2

\n\n\n\n\n\n
"""

t22="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]We're going to play a marching game. 
When you march, move forward raising your knees and lifting and swinging your arms.  
Now I am going to show you how I march.  
When I am done, I will ask you to do it the way I showed you.
[i][color=#FFA500][See video demonstration.][/i][/color]

Great.  Now show me how you do it.
[i][color=#FFA500][Offer any corrective suggestion and repeat demonstration and practice if needed][/i][/color]
[/color]

Trial 2: 
[color=#FF0000]SCRIPT[/color]: 
This time, we are going to march faster to the same drum beat. 
You are going to march in place to the beat just like before.
Try marching with the video to the beat for a few seconds. Great job.

[color=#FF0000]SCRIPT[/color]: 
Now it's your turn. Stand up tall and use your arms. 
Remember your foot hits the ground on each beat. 
Ready to march? 1,2,3, Go.

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of steps in rhythm with opposite arm swings.
0-2 beats correct = 0
3-5 beats correct = 1
6-8 beats correct = 2

\n\n\n\n\n\n
"""


t31="""[color=#FF0000]SCRIPT[/color]:
Now, we are going to pass a bag from one hand to the other, watch me.
[i][color=#FFA500][Stand facing student, pass the bag palms up, from one hand to the other, 1-8 at a slow even tempo of 65 bpm 4/4 time played on a metronome. DO NOT COUNT OUT LOUD Demonstrate or video.][/i][/color]
Notice that I am keeping a beat so that the bag hits my hand on the beat.

Trial 1:
Now it's your turn, pass the bag from one hand to the other back and forth 8 times. Try to stay on the beat. [i][color=#FFA500][Turn on metronome at 65 bpm 4/4 time and play for 8 beats][/i][/color]
Listen to the beat and when I say GO I want you to pass the bag between your hands keeping the beat. Remember to wait until I say 'GO' Ready to pass the bag? 1,2,3, Go
[i][color=#FFA500][STOP AFTER 8 BAG PASSES. Discontinue Bag sequence if the child fails to do at least half of the passes (8 errors correctly][/i][/color]

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of passes on beat
0-4 = 0
5-6 = 1
7-8 = 2

\n\n\n\n\n\n\n
"""

t32="""[color=#FF0000]SCRIPT[/color]:
Now, we are going to do the same thing we just did but at a faster tempo.
Listen to the beat. 
[i][color=#FFA500][Turn on metronome at 100 bpm 4/4 time and play for 8 beats][/i][/color] 
When I say GO I want you to pass the bag from one hand to the other.
The bag hits your hand on the beat. 
Remember to wait until I say 'GO' Ready to pass the bag? 1,2,3, Go
[i][color=#FFA500][STOP AFTER 8 BALL PASSES.][/i][/color]

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of passes on beat
0-4 = 0
5-6 = 1
7-8 = 2.

\n\n\n\n\n\n
"""

t41="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]Now we're going to play a game with a bag using the rules of Red/Green light.
Have you ever played that game? 
[i][color=#FFA500][Whatever answer, continue][/i][/color] 
Let me remind you of the rules.  When I say, Green Light pass the bag from one hand to the other as you did before, and when I say Red Light, don't pass the bag.

Practice
[color=#FF0000]SCRIPT[/color]: 
Let's try it. 
Green light, Green light, Red Light, Green Light, Red Light. Green light.  
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command Red-light - Green-light. Make any corrections needed during the practice and repeat practice if need.][/color]
[/color]

Trial 1: Slow Auditory
[color=#FF0000]SCRIPT[/color]: 
Great, now let's try some more.  
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command Red-light; Green-light.][/i][/color]

 1. Green Light
 2. Green Light
 3. Green Light
 4. Green Light
 5. Red Light
 6. Red Light
 7. Green Light
 8. Green Light
 9. Red Light
 10. Green Light
 11. Green Light
 12. Green Light
 13. Red Light
 14. Red Light
 15. Green Light 
 16. Red Light

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of correct passes even if out of rhythm. 0-7 = 0
8-13 = 1
14-16 = 2

\n\n\n\n\n\n
"""

t42="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]Now we're going to play a game with a bag using the rules of Red/Green light.
Have you ever played that game? 
[i][color=#FFA500][Whatever answer, continue][/i][/color] 
Let me remind you of the rules.  When I say, Green Light pass the bag from one hand to the other as you did before, and when I say Red Light, don't pass the bag.

Practice
[color=#FF0000]SCRIPT[/color]: 
Let's try it. 
Green light, Green light, Red Light, Green Light, Red Light. Green light.  
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command Red-light - Green-light. Make any corrections needed during the practice and repeat practice if need.][/color]
[/color]

Trial 2: Fast Auditory
[color=#FF0000]SCRIPT[/color]: 
Great, now let's try it again.
[i][color=#FFA500][Read the commands at a fast tempo. 100 pm 4/4 time with two counts per command Red-light; Green-light.][/i][/color]

 1. Green Light
 2. Green Light
 3. Green Light
 4. Green Light
 5. Red Light
 6. Red Light
 7. Green Light
 8. Green Light
 9. Red Light
 10. Green Light
 11. Green Light
 12. Green Light
 13. Red Light
 14. Red Light
 15. Green Light 
 16. Red Light

[i][color=#FFA500][Discontinue if there are more than 8 errors][/i][/color]

[color=#FF0000]SCORE[/color]: 
 Raw Score = Total number of correct passes even if out of rhythm
 0-7 = 0
 8-13 = 1
 14-16 = 2

[color=#FF0000]Additional Score[/color]: 
Red Lights correct (response inhibition)
0-2 = 0
3-5 = 1
6 = 2

\n\n\n\n\n\n
"""


t43="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]Now we're going to play a game with a bag using the rules of Red/Green light.
Have you ever played that game? 
[i][color=#FFA500][Whatever answer, continue][/i][/color] 
Let me remind you of the rules.  When I say, Green Light pass the bag from one hand to the other as you did before, and when I say Red Light, don't pass the bag.

Practice
[color=#FF0000]SCRIPT[/color]: 
Let's try it. 
Green light, Green light, Red Light, Green Light, Red Light. Green light.  
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command Red-light - Green-light. Make any corrections needed during the practice and repeat practice if need.][/color]
[/color]

Trial 3: Yellow Light Slow Auditory
Practice
[color=#FF0000]SCRIPT[/color]: 
Now we're going to slow it back down and add another color.  
Yellow means move the ball up and down in the same hand.  
When I say Yellow Light, you don't pass the bag to your other hand.  
Instead you move it up and down like this. 
Just move it up and down once. You try it. 
[i][color=#FFA500][Have child do it, and correct as necessary][/i][/color]
Let's practice with all three lights. 
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command.][/i][/color]

Green-Light; Yellow-Light; Green-Light; Yellow-Light: Red-Light; Yellow-Light.
[i][color=#FFA500][Make any corrections needed during the practice, and repeat practice once if necessary for child to get 3 correct.][/i][/color]

[color=#FF0000]SCRIPT[/color]: 
Great Now let's try some more.

 1. Green Light
 2. Green Light
 3. Yellow Light
 4. Green Light
 5. Red Light
 6. Yellow Light
 7. Red Light
 8. Yellow Light
 9. Green Light
 10. Green Light
 11. Yellow Light
 12. Red Light
 13. Red Light
 14. Yellow Light
 15. Yellow Light
 16. Green Light

[i][color=#FFA500][Skip Yellow Light Fast Auditory if there are more than 8 errors and go to Yellow Light Slow Visual][/i][/color]

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of correct passes even if out of rhythm. 
0-7 = 0
8-13 = 1
14-16 = 2

[color=#FF0000]Additional Score[/color]: 
Red Lights correct (response inhibition)
0-2 = 0
3-5 = 1
6 = 2

\n\n\n\n\n\n
"""

t44="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]Now we're going to play a game with a bag using the rules ofRed/Green light.
Have you ever played that game? 
[i][color=#FFA500][Whatever answer, continue][/i][/color] 
Let me remind you of the rules.  When I say, Green Light pass the bag from one hand to the other as you did before, and when I say Red Light, don't pass the bag.

Practice
[color=#FF0000]SCRIPT[/color]: 
Let's try it. 
Green light, Green light, Red Light, Green Light, Red Light. Green light.  
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command Red-light - Green-light. Make any corrections needed during the practice and repeat practice if need.][/color]
[/color]

Trial 4. Yellow Light Fast Auditory
[color=#FF0000]SCRIPT[/color]: 
We're going to keep playing the same game, only this time we are going to do it a little faster.  
Remember to pass the bag when you hear Green Light, don't pass it when you hear Red Light, and move the bag up and down when you hear Yellow Light.  
Are you ready?
[i][color=#FFA500][Read the commands at a faster tempo. 100 bpm 4/4 time with two counts per command. Do not make any corrections.][/i][/color]

 1. Green Light
 2. Green Light
 3. Yellow Light
 4. Green Light
 5. Red Light
 6. Yellow Light
 7. Red Light
 8. Yellow Light
 9. Green Light
 10. Green Light
 11. Yellow Light
 12. Red Light
 13. Red Light
 14. Yellow Light
 15. Yellow Light
 16. Green Light 

[i][color=#FFA500][Skip Yellow Light Fast Auditory if there are more than 8 errors and go to Yellow Light Slow Visual][/i][/color]

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of correct passes even if out of rhythm. 
0-7 = 0
8-13 = 1
14-16 = 2

[color=#FF0000]Additional Score[/color]: 
Red Lights correct (response inhibition)
0-2 = 0
3-5 = 1
6 = 2

\n\n\n\n\n\n
"""
t45="""[color=#FF0000]Intro-SCRIPT[/color]:
[color=#ADD8E6]Now we're going to play a game with a bag using the rules of Red/Green light.
Have you ever played that game? 
[i][color=#FFA500][Whatever answer, continue][/i][/color] 
Let me remind you of the rules.  When I say, Green Light pass the bag from one hand to the other as you did before, and when I say Red Light, don't pass the bag.

Practice
[color=#FF0000]SCRIPT[/color]: 
Let's try it. 
Green light, Green light, Red Light, Green Light, Red Light. Green light.  
[i][color=#FFA500][Read the commands at a moderate tempo. 65 pm 4/4 time with two counts per command Red-light - Green-light. Make any corrections needed during the practice and repeat practice if need.][/color]
[/color]

Trial 5. Yellow Light Slow Visual
[color=#FF0000]SCRIPT[/color]: 
Now we're going to slow it back down and use pictures of real traffic lights. You will do the same movements as before - when you see a green light you pass the bag; don't pass the bag when you see a red light; and move the bag up and down with the same hand when you see the yellow light.
[i][color=#FFA500][Play the video.  It will change the lights at a moderate tempo. 65 pm 4/4 time with two counts per command.][/i][/color]

 1. Green Light
 2. Green Light
 3. Yellow Light
 4. Green Light
 5. Red Light
 6. Yellow Light
 7. Red Light
 8. Yellow Light
 9. Green Light
 10. Green Light
 11. Yellow Light
 12. Red Light
 13. Red Light
 14. Yellow Light
 15. Yellow Light
 16. Green Light

[color=#FF0000]SCORE[/color]: 
Raw Score = Total number of correct passes even if out of rhythm. 
0-7 = 0
8-13 = 1
14-16 = 2

[color=#FF0000]Additional Score[/color]: 
Red Lights correct (response inhibition)
0-2 = 0
3-5 = 1
6 = 2

\n\n\n\n\n\n
"""

t51="""[color=#FF0000]SCRIPT[/color]:
We're going to play a new game. 
This one goes to a little rhyme that you may know.
"A sai-lor went to sea, sea, sea.  To see what he could see, see, see. But all that he could see, see, see.  Was the bot-tom of the deep blue sea, sea, sea."

We are going to move to the rhyme and we are going to use sea creatures to tell us how to move.

Now there are lots of creatures in the sea.  I want to tell you about 3 of the them.
[i][color=#FFA500][Show the large pictures] [/i][/color]

There's the Red Crab - he goes sideways to the right, so when you see the Red Crab, you go sideways to the right, one step moving both your feet.  
Don't make too big a step or it will be hard to stay in rhythm. 
There's the Blue Crab - he goes sideway to the left, so when you see the Blue Crab, you go sideways to the left one step, moving both your feet, the opposite way of the Red Crab.  
Remember, don't make too big a step. There's also the happy Clam.  
He's happy just where he is.  He doesn't move at all; so, when you see the Happy Clam, you just stay still, without going left or right.  
The tricky part is that you won't know which way to go until you see which creature it is. 
Try to stay in rhythm, but if you miss one, just keep going.

Let me show you how we do it. 
[i][color=#FFA500][Do the exercise while watching and listening to the power point][/i][/color]


Trial 1: Learning Trial
Okay, now you get to try it. 
[i][color=#FFA500][Use powerpoint. Do not correct errors][/i][/color] 

A sai-lor went to sea, sea, sea; to see what he could see, see, see, but all that he could see, see, see; Was the bot-tom of the deep blue sea, sea, sea

[color=#FF0000]SCORE[/color]: 
Stop, R, R, L, L, R, L, R
Stop, L, L, R, R, Stop, L, R
Stop, L, L, R, R, Stop, L, Stop
R, R, L, L, R, Stop, L, Stop  
 
Raw Score = Total number correct. 
1-15 = 0
16-28 = 1
29-32 = 2. 

[color=#FF0000]Additional Score[/color]: 
Stop (Clam) correct (response inhibition) 
0-4 = 0
5-6 = 1
7-8 = 2

-------------------------------

Trial 2: Learning Trial
Let''s try it again. 
[i][color=#FFA500][Use powerpoint. Do not correct errors][/i][/color] 

[color=#FF0000]SCORE[/color]: 
Stop, R, R, L, L, R, L, R
Stop, L, L, R, R, Stop, L, R
Stop, L, L, R, R, Stop, L, Stop
R, R, L, L, R, Stop, L, Stop

Raw Score = Total number correct
1-15 = 0
16-28 = 1
29-32 = 2. 
 

[color=#FF0000]Additional Score[/color]: 
Stop (Clam) correct (response inhibition) 
0-4 = 0
5-6 = 1
7-8 = 2

-------------------------------

Trial 3: Final Trial
Okay, it's time to see if you know all the moves.  
Are you ready?  Here we go. 
[i][color=#FFA500][Use powerpoint] [/i][/color] 

[color=#FF0000]SCORE[/color]: 
Stop, R, R, L, L, R, L, R
Stop, L, L, R, R, Stop, L, R
Stop, L, L, R, R, Stop, L, Stop
R, R, L, L, R, Stop, L, Stop

Raw Score = Total number correct
1-15 = 0
16-28 = 1
29-32 = 2. 
 

[color=#FF0000]Additional Score[/color]: 
Stop (Clam) correct (response inhibition) 
0-4 = 0
5-6 = 1
7-8 = 2

\n\n\n\n\n\n
"""




class ScrollableLabel(ScrollView):
    pass

class Cmenu1(Bubble):
    def __init__(self, **kwargs):
        super(Cmenu1, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
        text = l[0].text

        if text == 'Natural Walk':
            task ='11'
        elif text == 'Gait on Toes':
            task ='12'
        elif text == 'Tandem Gain':
            task ='13'
        elif text == 'Stand eyes closed hands outstretched':
            task ='14'
        elif text == 'Stand on One Foot':
            task ='15'
        self.parent.on_select_task(task)


        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)


class Cmenu2(Bubble):
    def __init__(self, **kwargs):
        super(Cmenu2, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
        text = l[0].text

        if text == 'March Slow':
            task ='21'
        elif text == 'March Fast':
            task ='22'
        self.parent.on_select_task(task)
        
        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)





class Cmenu3(Bubble):
    
    def __init__(self, **kwargs):
        super(Cmenu3, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
        text = l[0].text

        if text == 'Bi-manual Bag Pass Slow':
            task ='31'
        elif text == 'Bi-manual Bag Pass Fast':
            task ='32'
        self.parent.on_select_task(task)

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)



class Cmenu4(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu4, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
        text = l[0].text

        if text == 'Red Light/Green Light -- Slow':
            task ='41'
        elif text == 'Red Light/Green Light -- Fast':
            task ='42'
        elif text == 'Red Light/Green Light/Yellow Light -- Slow':
            task ='43'
        elif text == 'Red Light/Green Light/Yellow Light -- Fast':
            task ='44'
        elif text == 'Red Light/Green Light/Yellow Light -- Visual Slow':
            task ='45'
        self.parent.on_select_task(task)

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)



class Cmenu5(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu5, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text,task
        text = l[0].text
        task = '51'
        self.parent.on_select_task(task)

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)


class Cmenu6(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu6, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)

class Cmenu7(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu7, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)


class Cmenu8(Bubble):

    def __init__(self, **kwargs):
        super(Cmenu8, self).__init__(**kwargs)
        self.show_arrow = False

    def menu_selected(self,*l):
        global text
       
        text = l[0].text

        (r, g, b, a) = self.parent.context_menu.background_color
        print self.parent.context_menu.background_color
        def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

        for child in self.parent.children:
                   # child.clear_widgets()
                    child.background_normal = "button_normal.jpg"
                    child.color = (0, 0, 0, 1)

        anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
        anim.start(self.parent.context_menu)
        anim.bind(on_complete = on_anim_complete)




class MainScreen(FloatLayout) :

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        #self.ids['label'].text = self.ids['label'].text+"\n"+intro


class MainMenu(FloatLayout) :

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.context_menu = Cmenu1()
        global t1,t2,t3,t4,t5,t6,t7,t8 
        t1 = Cmenu1()
        t2 = Cmenu2()
        t3 = Cmenu3()
        t4 = Cmenu4()
        t5 = Cmenu5()
        t6 = Cmenu6()
        t7 = Cmenu7()
        t8 = Cmenu8()




    def on_touch_down(self, *l):
        #allow kids to get touch
        if super(MainMenu, self).on_touch_down(*l):
            return True
        self.remove_widget(self.context_menu)
        for child in self.children:
                #child.clear_widgets()
                child.background_normal = "button_normal.jpg"
                child.color = (0, 0, 0, 1)


    def add_menu(self, obj, submenu_id,*l):
        for child in self.children:
                #child.clear_widgets()
                child.background_normal = "button_normal.jpg"
                child.color = (0, 0, 0, 1)

        if  hasattr(self, 'context_menu'):
                self.remove_widget(self.context_menu)
        if submenu_id == 1:
            self.context_menu = t1
        elif submenu_id == 2:
            self.context_menu = t2
        elif submenu_id == 3:
            self.context_menu = t3
        elif submenu_id == 4:
            self.context_menu = t4
        elif submenu_id == 5:
            self.context_menu = t5
        elif submenu_id == 6:
            self.context_menu = t6
        elif submenu_id == 7:
            self.context_menu = t7
        elif submenu_id == 8:
            self.context_menu = t8

        if submenu_id not in ["start","stop","pause"]:
            obj.background_normal = "button_normal_is_on.jpg"
            obj.color = (1, 1, 1, 1)
            self.add_widget(self.context_menu)
            self.context_menu.pos = obj.pos[0]+ obj.width, obj.pos[1]
       
    def  on_control(self, obj, control_id,*l):
        if control_id == "start":
            print "play button pressed"
        elif control_id == "pause":
            print "pause button pressed"
        elif control_id =="help":
            print "Initial Instructions"
            self.ids['label1'].text = "ATEC"
            self.ids['label2'].text = "General-Instructions"
            self.ids['label3'].text = intro
        elif control_id =="complete":
            print "Task Copleted"
            print self.context_menu.ids
            for button in self.context_menu.children[1].children[0].children[0].children[0].children[0].children:
                if button.text == text:
                    button.background_normal = "button_normal_cmenu_c.jpg"
                    button.background_down = 'button_normal_cmenu_c.jpg'

        else:
            print "stopped"

    def on_select_task(self,task_id):
        print task_id
        if task_id[0]=='1':
            self.ids['label1'].text ="A. GROSS MOTOR - GAIT and BALANCE"
            if task_id[1]=='1':
                self.ids['label2'].text ="1. WALK FORWARD AND BACK (8 steps each way)"
                self.ids['label3'].text = t11
            elif task_id[1]=='2':
                self.ids['label2'].text ="2. GAIT ON TOES (8 steps)"
                self.ids['label3'].text = t12
            elif task_id[1]=='3':
                self.ids['label2'].text = "3. TANDEM GAIT FORWARD (heel to toe; 8 steps)"
                self.ids['label3'].text = t13
            elif task_id[1]=='4':
                self.ids['label2'].text = "4. STAND Feet Close, Eyes Closed, Arms & Fingers Outstretched - 10 sec."
                self.ids['label3'].text = t14
            elif task_id[1]=='5':
                self.ids['label2'].text = "3. TANDEM GAIT FORWARD (heel to toe; 8 steps)"
                self.ids['label3'].text = t15
        elif task_id[0]=='2':
            self.ids['label1'].text ="B. RHYTHMIC MOVEMENT"
            if task_id[1]=='1':
                self.ids['label2'].text ="1. March 8 Beats Slow (65 bpm 4/4 time)"
                self.ids['label3'].text = t21
            elif task_id[1]=='2':
                self.ids['label2'].text ="2. March 8 Beats Fast (100 bpm 4/4/ time)"
                self.ids['label3'].text = t22
        elif task_id[0]=='3':
            self.ids['label1'].text ="C. BILATERAL COORDINATION"
            if task_id[1]=='1':
                self.ids['label2'].text ="1. Bi-manual Bag Pass Slow"
                self.ids['label3'].text = t31
            elif task_id[1]=='2':
                self.ids['label2'].text ="2. Bi-manual Bag Pass Fast"
                self.ids['label3'].text = t32
        if task_id[0]=='4':
            self.ids['label1'].text ="A. GROSS MOTOR - GAIT and BALANCE"
            self.ids['label2'].text ="Bi-Manual Bag Pass with Red Light/Green Light Auditory and Visual"
            if task_id[1]=='1':
                self.ids['label3'].text = t41
            elif task_id[1]=='2':
                self.ids['label3'].text = t42
            elif task_id[1]=='3':
                self.ids['label3'].text = t43
            elif task_id[1]=='4':
                self.ids['label3'].text = t44
            elif task_id[1]=='5':
                self.ids['label3'].text = t45
        if task_id[0]=='5':
            self.ids['label1'].text ="E. VISUAL RESPONSE INHIBITION (A Sailor Went to Sea, Sea, Sea)."
            self.ids['label3'].text = t51



class MyApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MyApp().run()
