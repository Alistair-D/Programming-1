import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(967, 340)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkSalmon
        self._button1.Font = System.Drawing.Font("Microsoft NeoGothic", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.DarkSlateBlue
        self._button1.Location = System.Drawing.Point(44, 360)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(182, 68)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSalmon
        self._button2.Font = System.Drawing.Font("Microsoft NeoGothic", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.DarkSlateBlue
        self._button2.Location = System.Drawing.Point(420, 360)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(182, 68)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSalmon
        self._button3.Font = System.Drawing.Font("Microsoft NeoGothic", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.DarkSlateBlue
        self._button3.Location = System.Drawing.Point(768, 360)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(182, 68)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Coral
        self.ClientSize = System.Drawing.Size(991, 424)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122h"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        header = "Number" + "\t\t" + "Square" + "\t\t" +  "Square Root" + "\t\t" + "Cube" + "\t\t" + "4th Root"
        Number = 0
        self._listBox1.Items.Add(header)
        for num in range(1,21):
            num1 = math.sqrt(num)
            num2 = num * num
            num3 = num * num * num
            num4 = num ** 0.25
            rest = str(num) + "\t\t" + str(num2) + "\t\t" +   str(round(num1,4)) + "\t\t\t" + str(round(num3,4)) + "\t\t" + str(round(num4,4))
            self._listBox1.Items.Add(rest)            
            

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()