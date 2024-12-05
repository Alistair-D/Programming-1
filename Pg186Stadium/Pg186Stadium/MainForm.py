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
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(44, 402)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(232, 50)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(347, 364)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(232, 50)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(347, 420)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(232, 50)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit()"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(103, 64)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(155, 26)
        self._label1.TabIndex = 3
        self._label1.Text = "Class A"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(103, 119)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(155, 26)
        self._label2.TabIndex = 4
        self._label2.Text = "Class B"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(103, 172)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(155, 26)
        self._label3.TabIndex = 5
        self._label3.Text = "Class C"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(238, 64)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(198, 29)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(238, 119)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(198, 29)
        self._textBox2.TabIndex = 7
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(238, 172)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(198, 29)
        self._textBox3.TabIndex = 8
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Segoe Script", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(173, 39)
        self._label4.TabIndex = 9
        self._label4.Text = """Enter 




"""
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(447, 284)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(193, 26)
        self._label5.TabIndex = 10
        self._label5.Text = "Total Revenue"
        self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(-15, 357)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(155, 26)
        self._label6.TabIndex = 14
        self._label6.Text = "Class C"
        self._label6.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(-15, 304)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(155, 26)
        self._label7.TabIndex = 13
        self._label7.Text = "Class B"
        self._label7.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Showcard Gothic", 14, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(-15, 249)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(155, 26)
        self._label8.TabIndex = 12
        self._label8.Text = "Class A"
        self._label8.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Segoe Script", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(2, 204)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(663, 39)
        self._label9.TabIndex = 18
        self._label9.Text = "--------------------------------------------------------------------------------------------"
        self._label9.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.White
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(116, 252)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(142, 23)
        self._label10.TabIndex = 19
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.White
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(116, 307)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(142, 23)
        self._label11.TabIndex = 20
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.White
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(116, 357)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(142, 23)
        self._label12.TabIndex = 21
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.White
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(429, 252)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(223, 23)
        self._label13.TabIndex = 22
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(664, 482)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg186Stadium"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        TicketA = float(self._textBox1.Text)
        TicketB = float(self._textBox2.Text)
        TicketC = float(self._textBox3.Text)
        
        RevenueA = float(TicketA * 15)
        RevenueB = float(TicketB * 12)
        RevenueC = float(TicketC * 9)
        
        TotalRevenue = float(RevenueA + RevenueB + RevenueC)
        
        
        self._label13.Text = str("$") + str(TotalRevenue)
        self._label10.Text = str("$") + str(RevenueA)
        self._label11.Text = str("$") + str(RevenueB)
        self._label12.Text = str("$") + str(RevenueC)
        
        
        

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()