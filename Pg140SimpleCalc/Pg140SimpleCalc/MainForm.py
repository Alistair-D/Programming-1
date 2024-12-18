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
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(500, 31)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(92, 64)
        self._button1.TabIndex = 0
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(598, 31)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(92, 64)
        self._button2.TabIndex = 1
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(696, 31)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(92, 64)
        self._button3.TabIndex = 2
        self._button3.Text = "*"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.ForeColor = System.Drawing.Color.White
        self._button4.Location = System.Drawing.Point(500, 101)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(92, 64)
        self._button4.TabIndex = 3
        self._button4.Text = "^"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.ForeColor = System.Drawing.Color.White
        self._button5.Location = System.Drawing.Point(598, 101)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(92, 64)
        self._button5.TabIndex = 4
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.ForeColor = System.Drawing.Color.White
        self._button6.Location = System.Drawing.Point(696, 101)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(92, 64)
        self._button6.TabIndex = 6
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.ForeColor = System.Drawing.Color.White
        self._button7.Location = System.Drawing.Point(598, 171)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(92, 64)
        self._button7.TabIndex = 7
        self._button7.Text = "MOD"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.ForeColor = System.Drawing.Color.White
        self._button8.Location = System.Drawing.Point(504, 322)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(278, 64)
        self._button8.TabIndex = 8
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.Maroon
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.ForeColor = System.Drawing.Color.White
        self._button9.Location = System.Drawing.Point(504, 392)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(278, 64)
        self._button9.TabIndex = 9
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(186, 44)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(261, 32)
        self._textBox1.TabIndex = 10
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Gray
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(5, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(175, 51)
        self._label1.TabIndex = 11
        self._label1.Text = """Number 
1 --->
"""
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Silver
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(5, 142)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(175, 34)
        self._label2.TabIndex = 12
        self._label2.Text = "Operation:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Silver
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Black
        self._label3.Location = System.Drawing.Point(213, 142)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(175, 34)
        self._label3.TabIndex = 13
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Gray
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(5, 273)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(175, 51)
        self._label4.TabIndex = 15
        self._label4.Text = """Number 
2 --->
"""
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(186, 286)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(261, 32)
        self._textBox2.TabIndex = 14
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Gray
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(5, 398)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(175, 29)
        self._label5.TabIndex = 17
        self._label5.Text = "Result:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(193, 398)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(254, 29)
        self._label6.TabIndex = 18
        self._label6.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Silver
        self.ClientSize = System.Drawing.Size(817, 484)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.ForeColor = System.Drawing.Color.White
        self.Name = "MainForm"
        self.Text = "Pg140SimpleCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label5Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label3.Text = "+"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        sum = num1 + num2
        self._label6.Text = str(sum)

    def Button2Click(self, sender, e):
        self._label3.Text = "-"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        Difference = num1 - num2
        self._label6.Text = str(Difference)

    def Button3Click(self, sender, e):
        self._label3.Text = "*"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        Product = num1 * num2
        self._label6.Text = str(Product)

    def Button4Click(self, sender, e):
        self._label3.Text = "^"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        Exponent = num1 ** num2
        self._label6.Text = str(Exponent)

    def Button5Click(self, sender, e):
        self._label3.Text = "/"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        Quotient = num1 / num2
        self._label6.Text = str(Quotient)
    

    def Button6Click(self, sender, e):
        self._label3.Text = "//"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        QuotientD = num1 // num2
        self._label6.Text = str(QuotientD)

    def Button7Click(self, sender, e):
        self._label3.Text = "%"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        Module = num1 % num2
        self._label6.Text = str(Module)

    def Button8Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label6.Text = ""

    def Button9Click(self, sender, e):
        Application.Exit()