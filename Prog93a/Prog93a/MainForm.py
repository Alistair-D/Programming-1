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
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Yellow
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(0, 343)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(269, 89)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Yellow
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(324, 343)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(269, 89)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Yellow
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(630, 343)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(269, 89)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(22, 147)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(151, 32)
        self._textBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Cornsilk
        self._label1.Location = System.Drawing.Point(22, 121)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(162, 23)
        self._label1.TabIndex = 4
        self._label1.Text = "Enter KWH used:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Cornsilk
        self._label2.Location = System.Drawing.Point(212, 151)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(162, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "----------------- >"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Cornsilk
        self._label3.Location = System.Drawing.Point(585, 26)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(93, 23)
        self._label3.TabIndex = 6
        self._label3.Text = "Amounts:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FloralWhite
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Black
        self._label4.Location = System.Drawing.Point(551, 72)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(179, 27)
        self._label4.TabIndex = 7
        self._label4.Text = "BaseRate:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FloralWhite
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Black
        self._label5.Location = System.Drawing.Point(551, 117)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(179, 27)
        self._label5.TabIndex = 8
        self._label5.Text = "Surcharge:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FloralWhite
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(551, 164)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(179, 27)
        self._label6.TabIndex = 9
        self._label6.Text = "CityTax:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FloralWhite
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Black
        self._label7.Location = System.Drawing.Point(513, 245)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(234, 27)
        self._label7.TabIndex = 10
        self._label7.Text = "Pay this amount:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FloralWhite
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.Black
        self._label8.Location = System.Drawing.Point(513, 286)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(234, 27)
        self._label8.TabIndex = 11
        self._label8.Text = "After May 20th:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(899, 432)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        KWH = float(self._textBox1.Text)
        Bsrate   = (round(KWH * 0.0475,2))
        SRcharge = float(round(Bsrate / 10,2))
        CityTax = float (round(SRcharge * 0.3,2))
        Amount = float (Bsrate + SRcharge + CityTax)
        Late = float(round(Amount * 0.04,2))


        self._label4.Text = "Base Rate: $" + str(Bsrate)
        self._label5.Text = "Surcharge: $" + str(SRcharge)
        self._label6.Text = "CityTax: $" + str(CityTax)
        self._label7.Text = "Pay this Amount: $" + str(Amount)
        self._label8.Text = "After May 20th: $" + str(Late + Amount)
        
    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        pass