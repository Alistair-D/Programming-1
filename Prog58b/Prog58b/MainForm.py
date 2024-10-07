import System.Drawing
import System.Windows.Forms
from math import sqrt
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.Control
        self._button1.Font = System.Drawing.Font("Perpetua Titling MT", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(-4, 381)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(196, 64)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.Control
        self._button2.Font = System.Drawing.Font("Perpetua Titling MT", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(393, 381)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(171, 64)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Control
        self._button3.Font = System.Drawing.Font("Perpetua Titling MT", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(802, 381)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(159, 64)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Info
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(635, 226)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(295, 97)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 94)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(295, 33)
        self._label3.TabIndex = 5
        self._label3.Text = "Input"
        self._label3.TextAlign = System.Drawing.ContentAlignment.BottomCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(635, 314)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(295, 33)
        self._label4.TabIndex = 6
        self._label4.Text = "Output"
        self._label4.TextAlign = System.Drawing.ContentAlignment.BottomCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(313, 141)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(283, 94)
        self._label5.TabIndex = 7
        self._label5.Text = "-------------->"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 226)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(295, 33)
        self._label6.TabIndex = 9
        self._label6.Text = "Input"
        self._label6.TextAlign = System.Drawing.ContentAlignment.BottomCenter
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(12, 344)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(295, 33)
        self._label8.TabIndex = 11
        self._label8.Text = "Input"
        self._label8.TextAlign = System.Drawing.ContentAlignment.BottomCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.Info
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(635, 85)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(295, 105)
        self._label12.TabIndex = 12
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.White
        self._label13.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(635, 170)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(295, 33)
        self._label13.TabIndex = 13
        self._label13.Text = "Output"
        self._label13.TextAlign = System.Drawing.ContentAlignment.BottomCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(52, 43)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(255, 35)
        self._textBox1.TabIndex = 14
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(52, 171)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(255, 35)
        self._textBox2.TabIndex = 15
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(52, 306)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(255, 35)
        self._textBox3.TabIndex = 16
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.InactiveCaption
        self.ClientSize = System.Drawing.Size(957, 444)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog58b"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        inputA      = float(self._textBox1.Text)
        inputB      = float(self._textBox2.Text)
        inputC      = float(self._textBox3.Text)
        NegInputB   = int(-inputB)
        FourAC      = int(4 * inputA * inputC)
        TwoA        = int(inputA * 2)
        initialRoot = sqrt(inputB**2 - FourAC)
        PosParenth  = int(NegInputB + initialRoot)
        NegParenth  = int(NegInputB - initialRoot)
        FirstRoot   = int(PosParenth / TwoA)
        SecondRoot  = int(NegInputB / TwoA)
        self._label12.Text = str(FirstRoot)
        self._label2.Text = str(SecondRoot)
        
    def Button2Click(self, sender, e):
        self._label2.Text = ""
        self._label12.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label5Click(self, sender, e):
        pass