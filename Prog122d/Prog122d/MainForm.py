﻿import System.Drawing
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
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button1.Font = System.Drawing.Font("Ravie", 16.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.CornflowerBlue
        self._button1.Location = System.Drawing.Point(662, 29)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(294, 89)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button2.Font = System.Drawing.Font("Ravie", 16.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.CornflowerBlue
        self._button2.Location = System.Drawing.Point(662, 115)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(294, 89)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button3.Font = System.Drawing.Font("Ravie", 16.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.CornflowerBlue
        self._button3.Location = System.Drawing.Point(662, 201)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(294, 89)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(644, 460)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(955, 471)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.ForeColor = System.Drawing.Color.CornflowerBlue
        self.Name = "MainForm"
        self.Text = "Prog122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        for num in range(-12,17):
            x = num
            
            step1 = x ** 6
            step2 = 3*(x) ** 5
            step3 = 93*(x)** 4
            step4 = 87*(x) ** 3
            step5 = 1596*(x)** 2
            step6 = 1380*(x)
            step7 = 2800
            
            All = int(step1) - int(step2) - int(step3) + int(step4) + int(step5) - int(step6) - int(step7)
            List = str(x) + "\t\t"  + str(All)
            self._listBox1.Items.Add(List)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()