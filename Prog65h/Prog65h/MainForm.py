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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(0, 369)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(207, 55)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(343, 369)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(207, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(667, 369)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(207, 55)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(137, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(141, 35)
        self._textBox1.TabIndex = 3
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(137, 66)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(141, 35)
        self._textBox2.TabIndex = 4
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Vladimir Script", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 35)
        self._label1.TabIndex = 5
        self._label1.Text = "Pounds"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Vladimir Script", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 68)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 35)
        self._label2.TabIndex = 6
        self._label2.Text = "Shillings"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(137, 129)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(141, 35)
        self._textBox3.TabIndex = 7
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Vladimir Script", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 129)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 35)
        self._label3.TabIndex = 8
        self._label3.Text = "Pence"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Imprint MT Shadow", 20.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(355, 82)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(211, 35)
        self._label4.TabIndex = 9
        self._label4.Text = "---->"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Imprint MT Shadow", 20.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(609, 47)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(211, 35)
        self._label5.TabIndex = 10
        self._label5.Text = "Amount:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Imprint MT Shadow", 20.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(609, 82)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(211, 49)
        self._label6.TabIndex = 11
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self.ClientSize = System.Drawing.Size(871, 422)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def Label4Click(self, sender, e):
        pass


    # 20 Shillings = Pound
    # 12 Pence = Shilling
    def Button1Click(self, sender, e):
        Pounds = (self._textBox1.Text)
        Schillings = (self._textBox2.Text)
        Pence = (self._textBox3.Text)
        
        

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()