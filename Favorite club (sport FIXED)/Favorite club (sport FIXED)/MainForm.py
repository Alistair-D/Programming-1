import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Ravie", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 382)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(209, 62)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._button2.Font = System.Drawing.Font("Ravie", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(360, 382)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(209, 62)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Ravie", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(758, 382)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(209, 62)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.HotTrack
        self._label1.Location = System.Drawing.Point(12, 0)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(955, 379)
        self._label1.TabIndex = 3
        self._label1.Text = "Favorite Sport"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Old English Text MT", 21.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.DarkBlue
        self._label2.Location = System.Drawing.Point(269, 284)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(420, 95)
        self._label2.TabIndex = 4
        self._label2.Text = "..."
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Old English Text MT", 21.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic | System.Drawing.FontStyle.Underline | System.Drawing.FontStyle.Strikeout, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(341, 209)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(284, 106)
        self._label3.TabIndex = 5
        self._label3.Text = "..."
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Old English Text MT", 21.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic | System.Drawing.FontStyle.Underline | System.Drawing.FontStyle.Strikeout, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(341, 127)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(284, 106)
        self._label4.TabIndex = 6
        self._label4.Text = "..."
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Old English Text MT", 21.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic | System.Drawing.FontStyle.Underline | System.Drawing.FontStyle.Strikeout, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(341, 43)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(284, 106)
        self._label5.TabIndex = 7
        self._label5.Text = "..."
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightCyan
        self.ClientSize = System.Drawing.Size(966, 444)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Favorite club (sport FIXED)"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        Application.Exit()
        
        

    def Button1Click(self, sender, e):
        self._label2.Text = "Cross Country"
        self._label3.Text = "Baseball"
        self._label4.Text = "Tennis"
        self._label5.Text = "VolleyBall"
                
        

    def Button2Click(self, sender, e):
        self._label2.Text = "..."
        self._label3.Text = "..."
        self._label4.Text = "..."
        self._label5.Text = "..."
                

    def Label3Click(self, sender, e):
        pass