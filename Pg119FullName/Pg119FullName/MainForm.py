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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(3, 408)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(285, 67)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(333, 408)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(285, 67)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(734, 408)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(118, 67)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(44, 33)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(341, 23)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter your First Name ---->"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(44, 173)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(341, 23)
        self._label2.TabIndex = 4
        self._label2.Text = "Enter your Last Name ---->"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(44, 340)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(341, 23)
        self._label3.TabIndex = 5
        self._label3.Text = "Full Name --->"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox1
        # 
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(391, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(405, 32)
        self._textBox1.TabIndex = 6
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(391, 186)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(405, 32)
        self._textBox2.TabIndex = 7
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(304, 340)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(533, 34)
        self._label4.TabIndex = 8
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(849, 474)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg119FullName"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        Fname = str(self._textBox1.Text)
        Lname = str(self._textBox2.Text)
        fname = str(Fname) + " " + str(Lname)
        self._label4.Text = str(fname)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()