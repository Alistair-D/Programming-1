﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.R = System.Random()
        self.ballup = 0
        self.balld = 0
        self.flagleft = False
        self.flagright = False
        
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        self._lbltitle = System.Windows.Forms.Label()
        self._leftscore = System.Windows.Forms.Label()
        self._rightscore = System.Windows.Forms.Label()
        self._lblball = System.Windows.Forms.Label()
        self._lblleft = System.Windows.Forms.Label()
        self._lblright = System.Windows.Forms.Label()
        self._timerdummy = System.Windows.Forms.Timer(self._components)
        self._timerboolean = System.Windows.Forms.Timer(self._components)
        self._timerright = System.Windows.Forms.Timer(self._components)
        self._timerleft = System.Windows.Forms.Timer(self._components)
        self._timerball = System.Windows.Forms.Timer(self._components)
        self._timermulti = System.Windows.Forms.Timer(self._components)
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # lbltitle
        # 
        self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._lbltitle.ForeColor = System.Drawing.Color.White
        self._lbltitle.Location = System.Drawing.Point(12, 25)
        self._lbltitle.Name = "lbltitle"
        self._lbltitle.Size = System.Drawing.Size(958, 52)
        self._lbltitle.TabIndex = 0
        self._lbltitle.Text = "Press Enter to Start or M to Start Multiplayer"
        self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._lbltitle.Click += self.Label1Click
        # 
        # leftscore
        # 
        self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._leftscore.ForeColor = System.Drawing.Color.White
        self._leftscore.Location = System.Drawing.Point(78, 96)
        self._leftscore.Name = "leftscore"
        self._leftscore.Size = System.Drawing.Size(166, 109)
        self._leftscore.TabIndex = 1
        self._leftscore.Text = "0"
        self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # rightscore
        # 
        self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._rightscore.ForeColor = System.Drawing.Color.White
        self._rightscore.Location = System.Drawing.Point(734, 96)
        self._rightscore.Name = "rightscore"
        self._rightscore.Size = System.Drawing.Size(166, 109)
        self._rightscore.TabIndex = 2
        self._rightscore.Text = "0"
        self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # lblball
        # 
        self._lblball.BackColor = System.Drawing.Color.White
        self._lblball.Location = System.Drawing.Point(479, 304)
        self._lblball.Name = "lblball"
        self._lblball.Size = System.Drawing.Size(20, 20)
        self._lblball.TabIndex = 3
        self._lblball.Click += self.LblballClick
        # 
        # lblleft
        # 
        self._lblleft.BackColor = System.Drawing.Color.White
        self._lblleft.Location = System.Drawing.Point(12, 246)
        self._lblleft.Name = "lblleft"
        self._lblleft.Size = System.Drawing.Size(20, 100)
        self._lblleft.TabIndex = 4
        # 
        # lblright
        # 
        self._lblright.BackColor = System.Drawing.Color.White
        self._lblright.Location = System.Drawing.Point(950, 246)
        self._lblright.Name = "lblright"
        self._lblright.Size = System.Drawing.Size(20, 100)
        self._lblright.TabIndex = 5
        # 
        # timerright
        # 
        self._timerright.Interval = 20
        self._timerright.Tick += self.TimerrightTick
        # 
        # timerleft
        # 
        self._timerleft.Interval = 20
        self._timerleft.Tick += self.TimerleftTick
        # 
        # timerball
        # 
        self._timerball.Interval = 20
        self._timerball.Tick += self.TimerballTick
        # 
        # timermulti
        # 
        self._timermulti.Interval = 20
        # 
        # label2
        # 
        self._label2.ForeColor = System.Drawing.Color.Black
        self._label2.Location = System.Drawing.Point(950, 584)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(46, 23)
        self._label2.TabIndex = 8
        self._label2.Text = "Ocean"
        self._label2.MouseClick += self.Label2MouseClick
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(988, 607)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._lblright)
        self.Controls.Add(self._lblleft)
        self.Controls.Add(self._lblball)
        self.Controls.Add(self._rightscore)
        self.Controls.Add(self._leftscore)
        self.Controls.Add(self._lbltitle)
        self.Name = "MainForm"
        self.Text = "Pong"
        self.Load += self.MainFormLoad
        self.SizeChanged += self.MainFormSizeChanged
        self.KeyDown += self.MainFormKeyDown
        self.ResumeLayout(False)



    def Label1Click(self, sender, e):
        pass

    def TimerballTick(self, sender, e):
        tdum =  self._timerdummy
        ball = self._lblball
        lpdl = self._lblleft
        rpdl = self._lblright
        rscore = int(self._rightscore.Text)
        lscore = int(self._leftscore.Text)
        ball.Top += self.ballup
        ball.Left += 8 * self.balld
        
        if ball.Right >= rpdl.Right and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
            self.balld = -1
            self.ballup = self.R.Next(-4,5)
        elif ball.Left <= lpdl.Left and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
            self.balld = 1
            self.ballup = self.R.Next(-4,5)
            
        if ball.Top <= 0:
            self.balld = -1
            self.Top += 5 * self.balld
        elif ball.Bottom >= self.Height:
            self.balld = 1
            self.Top += 5 * self.balld
            
        if ball.Top <= self.Top + 10:
            self.ballup = 1
        elif ball.Top >= self.Height - 50:
            self.ballup = -1
        
        
        if ball.Location.X <= 0 or \
            (ball.Location.X < lpdl.Left - 20 and ball.Location.Y < lpdl.Top):
                rscore += 1
                self._rightscore.Text = str(rscore)
                ball.Left = self.Width // 2
                ball.Top = self.Height // 2
                

                
        if ball.Location.X >= self.Width or \
            (ball.Location.X > rpdl.Right + 20 and ball.Location.Y  > rpdl.Top):
                lscore += 1
                self._leftscore.Text = str(lscore)
                ball.Left = self.Width // 2
                ball.Top = self.Height // 2
                
                """TODO: FINISH RIGHT SCORE WIN CONDITION"""
        if rscore == 10:
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "Right Player Wins! Press R to Restart"
            self._lbltitle.Visible = True
                
        if lscore == 10:
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "left Player Wins! Press R to Restart"
            self._lbltitle.Visible = True
            
        if tdum.Enabled == True:
            if lscore == 9:
                if ball.Location.X < 50:
                    ball.Location.Y = ball.Location.Y + 200
                    
                    
        if self._timerboolean.Enabled:
            lpdl.Top = ball.Top - 20
            
            
        pass
    
    def MainFormKeyDown(self, sender, e):
        tball = self._timerball
        tdum =  self._timerdummy
        tbool = self._timerboolean
        tmult = self._timermulti
        tleft = self._timerleft
        tright = self._timerright
        bl = self._lblball
        lpdl = self._lblleft
        rpdl = self._lblright
        title = self._lbltitle
        
        def reset():
            title.Visible = True
            title.Text = "Press Enter to Start or M to start Multiplayer"
            self._leftscore.Text = "0"
            self._rightscore.Text = "0"
            tball.Enabled = False
            tdum.Enabled = False
            tbool.Enabled = False       #Deactivating Timers (Freezing the game to a halt)
            tmult.Enabled = False
            tleft.Enabled = False
            tright.Enabled = False
            bl.Left = self.Width // 2
            bl.Top = self.Height // 2
            lpdl.Top = (self.Height // 2) - 50 + lpdl.Height
            rpdl.Top = (self.Height // 2) - 50 + rpdl.Height
            """TODO: RESET SECRETS"""
            bl.BackColor = Color.White
            self._lblball.BackColor = Color.White
            self._lblleft.BackColor = Color.White
            self._lblright.BackColor = Color.White
            self.BackColor = Color.Black
            self._label2.ForeColor = Color.Black
            
        if e.KeyCode == Keys.R:
            reset()
            
        #Secret Easter Eggs
        if e.KeyCode == Keys.I:
            self._lblball.BackColor = Color.Black
            MessageBox.Show("Impossible Mode Activated! Ball is Invisible!")
        
        if e.KeyCode == Keys.Enter:
            tball.Enabled = True
            tdum.Enabled = True
            tbool.Enabled = not tmult.Enabled
            title.Visible = False
        
        if e.KeyCode == Keys.M:
            reset()
            title.Visible = True
            title.Text = "Use W and S to move the left Paddle; hit Enter to Start!"
            tmult.Enabled = True
            
        if tdum.Enabled:
            if e.KeyCode == Keys.Up:
                self.flagright = False
                tright.Enabled = True
            elif e.KeyCode == Keys.Down:
                self.flagright = True
                tright.Enabled = True
                
                    
                    
                    
        if tmult.Enabled and tball.Enabled:
            if e.KeyCode == Keys.W:
                self.flagleft = False
                tleft.Enabled = True
            elif e.KeyCode == Keys.S:
                self.flagleft = True
                tleft.Enabled = True
        pass
    
    def MainFormLoad(self, sender, e):
        """ TODO: ADD 3 UNIQUE SECRETS/CHEATS/EASTER EGGS 
        IN TOTAL & FINISH MULTIPLAYER & SCOREBOARD & DUMMY AI"""
        self.balld = 1
        self.ballup = self.R.Next(-4, 5)
    
    def pdlTick(self, pdl, flagd, tmr):
        if flagd == True:
            pdl.Top += 5
        else:
            pdl.Top -= 5
        if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
            tmr.Enabled = False

    def TimerleftTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

    def TimerrightTick(self, sender, e):
        self.pdlTick(self._lblright, self.flagright, self._timerright)
    
    def LblballClick(self, sender, e):
        self._lblball.BackColor = Color.Red
        self.BackColor = Color.Green #Form Background Color (Easter egg)
        # "PUT MORE EASTER EGGS LATER"
    
    def MainFormSizeChanged(self, sender, e):
        #Resize Code (When Expanding and changing size of Window)
        self._lblright.Left = self.Width - 25 - self._lblright.Width
        self._rightscore.Left = self.Width - 75 - self._rightscore.Width
        self._lbltitle.Width = self.Width - 25
        self._lblball.Left = self.Width // 2
        self._lblball.Top = self.Height // 2


#Easter Egg 2
    def Button1Click(self, sender, e):
        pass
        
     

    def Label2MouseClick(self, sender, e):
        self._lblball.BackColor = Color.Yellow
        self._lblleft.BackColor = Color.Coral
        self._lblright.BackColor = Color.Coral
        self._label2.ForeColor = Color.DeepSkyBlue
        self.BackColor = Color.DeepSkyBlue
        MessageBox.Show("Woahhh! There was a Flood!")
        MessageBox.Show("Under the Seaaaaaaa")
        MessageBox.Show("Darlin' its better")
        MessageBox.Show("Under the Seaaaaaaa")
        
        
        
        