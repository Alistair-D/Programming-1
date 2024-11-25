import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Black
        self._button1.Font = System.Drawing.Font("Segoe Print", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Yellow
        self._button1.Location = System.Drawing.Point(-3, 428)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(222, 55)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Black
        self._button2.Font = System.Drawing.Font("Segoe Print", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Yellow
        self._button2.Location = System.Drawing.Point(394, 428)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(222, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Black
        self._button3.Font = System.Drawing.Font("Segoe Print", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Yellow
        self._button3.Location = System.Drawing.Point(740, 428)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(222, 55)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.WindowFrame
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.Yellow
        self._textBox1.Location = System.Drawing.Point(173, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(184, 38)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.WindowFrame
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.Yellow
        self._textBox2.Location = System.Drawing.Point(173, 84)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(184, 38)
        self._textBox2.TabIndex = 4
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Yellow
        self._label1.Location = System.Drawing.Point(12, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(132, 38)
        self._label1.TabIndex = 6
        self._label1.Text = "Guests --->"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Yellow
        self._label2.Location = System.Drawing.Point(12, 84)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(132, 38)
        self._label2.TabIndex = 7
        self._label2.Text = "Chair --->"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.WindowFrame
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Yellow
        self._label3.Location = System.Drawing.Point(173, 139)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(184, 38)
        self._label3.TabIndex = 8
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.WindowFrame
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Yellow
        self._label4.Location = System.Drawing.Point(173, 208)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(184, 38)
        self._label4.TabIndex = 9
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Yellow
        self._label5.Location = System.Drawing.Point(-3, 141)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(177, 38)
        self._label5.TabIndex = 10
        self._label5.Text = "Permutations --->"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Yellow
        self._label6.Location = System.Drawing.Point(12, 192)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(132, 74)
        self._label6.TabIndex = 11
        self._label6.Text = "Guest Standing -->"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("MV Boli", 30.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Yellow
        self._label7.Location = System.Drawing.Point(590, 105)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(321, 141)
        self._label7.TabIndex = 12
        self._label7.Text = "Program162h"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(963, 483)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog162h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        GuestAmount = int(self._textBox1.Text)
        ChairAmount = int(self._textBox2.Text)
        if GuestAmount < ChairAmount:
            MessageBox.Show("You have enough Guests!")
        else:
            Standing = GuestAmount - ChairAmount
            self._label4.Text = str(Standing)
            Permutation = math.factorial(GuestAmount) / math.factorial(GuestAmount - ChairAmount)
            self._label3.Text = str(Permutation)
            

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()