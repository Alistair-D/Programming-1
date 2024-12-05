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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 388)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 60)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate Average"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(171, 391)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 57)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(341, 388)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(131, 60)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Ravie", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 72)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(151, 39)
        self._label1.TabIndex = 3
        self._label1.Text = "Score 1"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(151, 27)
        self._label2.TabIndex = 4
        self._label2.Text = "Enter"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(-6, 38)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(510, 27)
        self._label3.TabIndex = 5
        self._label3.Text = "---------------------------------------------------------------------"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(146, 72)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(303, 29)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(146, 114)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(303, 29)
        self._textBox2.TabIndex = 8
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Ravie", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 114)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(151, 39)
        self._label4.TabIndex = 7
        self._label4.Text = "Score 2"
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(146, 156)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(303, 29)
        self._textBox3.TabIndex = 10
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Ravie", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 156)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(151, 39)
        self._label5.TabIndex = 9
        self._label5.Text = "Score 3"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Ravie", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 263)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(151, 39)
        self._label6.TabIndex = 11
        self._label6.Text = "Average"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(146, 273)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(303, 23)
        self._label7.TabIndex = 12
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Myanmar Text", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(-13, 217)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(510, 27)
        self._label8.TabIndex = 13
        self._label8.Text = "---------------------------------------------------------------------"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(484, 460)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg198ScoreAverage"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()