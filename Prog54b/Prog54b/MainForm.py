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
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDark
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Cornsilk
        self._button1.Location = System.Drawing.Point(-3, 333)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(192, 79)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Cornsilk
        self._button2.Location = System.Drawing.Point(361, 333)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(192, 79)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlDark
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Cornsilk
        self._button3.Location = System.Drawing.Point(697, 333)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(192, 79)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(128, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(185, 32)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(128, 66)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(185, 32)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(128, 190)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(185, 32)
        self._textBox3.TabIndex = 5
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(128, 123)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(185, 32)
        self._textBox4.TabIndex = 6
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.CornflowerBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Cornsilk
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 213)
        self._label1.TabIndex = 7
        self._label1.Text = "Enter #Numbers Here    ---->"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Cornsilk
        self._label2.Location = System.Drawing.Point(392, 55)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(88, 33)
        self._label2.TabIndex = 9
        self._label2.Text = "Sum:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Cornsilk
        self._label3.Location = System.Drawing.Point(629, 55)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(131, 33)
        self._label3.TabIndex = 11
        self._label3.Text = "Average:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Cornsilk
        self._label4.Location = System.Drawing.Point(361, 89)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(119, 41)
        self._label4.TabIndex = 12
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft YaHei", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Cornsilk
        self._label5.Location = System.Drawing.Point(617, 89)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(119, 41)
        self._label5.TabIndex = 13
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDark
        self.ClientSize = System.Drawing.Size(889, 412)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Num3 = int(self._textBox3.Text)
        Num4 = int(self._textBox4.Text)
        Sum  = Num1 + Num2 + Num3 + Num4
        self._label4.Text = str(Sum)
        Avg = Sum // 4.0
        self._label5.Text = str(Avg)
        

    def Label4Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        