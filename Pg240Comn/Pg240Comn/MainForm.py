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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
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
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._button1.Location = System.Drawing.Point(30, 478)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(236, 54)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._button2.Location = System.Drawing.Point(331, 478)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(236, 54)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._button3.Location = System.Drawing.Point(632, 478)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(236, 54)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(100, 103)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(193, 41)
        self._label1.TabIndex = 3
        self._label1.Text = "Sales for the Month:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(282, 104)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(285, 26)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(282, 147)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(285, 26)
        self._textBox2.TabIndex = 6
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(83, 145)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(193, 41)
        self._label2.TabIndex = 5
        self._label2.Text = "Advance Pay Awarded:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(83, 252)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(193, 41)
        self._label3.TabIndex = 7
        self._label3.Text = "Commision Rate:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(83, 306)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(193, 41)
        self._label4.TabIndex = 9
        self._label4.Text = "Comission:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(83, 364)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(193, 41)
        self._label5.TabIndex = 11
        self._label5.Text = "Net Pay:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(282, 252)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(285, 28)
        self._label6.TabIndex = 12
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(282, 306)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(285, 28)
        self._label7.TabIndex = 13
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(282, 364)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(285, 28)
        self._label8.TabIndex = 14
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(880, 544)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg240Comn"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        decSalesAmount = 0
        decAdvancedPayAmount = 0.0
        decCommissionRate = 0.0
        decCommissionAmount = 0.0
        decNetPay = 0.0
        
        decSalesAmount = float(self._txtSalesAmount.Text)
        self._textBox1.Text = "Sales amount must be Numeric"
        
        decAdvancePayAmount = float(self._txtAdvancePayAmount.Text)
        
        
        if decSalesAmount < 10000:
            decCommisionRate = 0.05
        elif decSalesAmount >= 10000 and decSalesAmount < 15000:
            decCommissionRate = 0.1
        elif decSalesAmount >= 15000 and decSalesAmount < 18000:
            decCommissionRate = 0.12
        elif decSalesAmount >= 18000 and decSalesAmount < 22000:
            decCommissionRate = 0.14
        elif decSalesAmount >= 22000:
            decCommissionRate = 0.15
            
        decCommissionAmount = decSalesAmount * decComissionRate
        decNetPay = decCommissionAmount - decAdvancePayAmount
        
        self._label6.Text = str(round(decCommissionRate, 2))
        self._label7.Text = str(round(decComissionAmount , 2))
        self._label8.Text = str(round(decNetPay, 2))
        

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()
        
        
        

