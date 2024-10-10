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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(195, 214)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(379, 40)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(195, 138)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 81)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(388, 138)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(187, 81)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit Program"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.CornflowerBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(22, 260)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(370, 31)
        self._label1.TabIndex = 3
        self._label1.Text = "Total = "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(87, 64)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(220, 30)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PowderBlue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(87, 88)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(220, 21)
        self._label2.TabIndex = 6
        self._label2.Text = "Total Due"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PowderBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(484, 88)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(220, 21)
        self._label3.TabIndex = 8
        self._label3.Text = "Total Paid"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(484, 64)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(220, 30)
        self._textBox3.TabIndex = 7
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.CornflowerBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(22, 343)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(370, 31)
        self._label4.TabIndex = 9
        self._label4.Text = "Change = "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.CornflowerBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(22, 305)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(370, 27)
        self._label5.TabIndex = 10
        self._label5.Text = "Paid = "
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.CornflowerBlue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(22, 435)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(370, 25)
        self._label6.TabIndex = 11
        self._label6.Text = "Quarters Due ="
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.CornflowerBlue
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(422, 263)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(370, 28)
        self._label7.TabIndex = 12
        self._label7.Text = "Dimes Due ="
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.CornflowerBlue
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(425, 353)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(367, 31)
        self._label11.TabIndex = 14
        self._label11.Text = "Pennies Due ="
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.CornflowerBlue
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(422, 305)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(367, 31)
        self._label12.TabIndex = 13
        self._label12.Text = "Nickels Due:"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.CornflowerBlue
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(22, 387)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(370, 31)
        self._label8.TabIndex = 15
        self._label8.Text = "Dollars Due = "
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(842, 479)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label2Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        TotalDue  = float(self._textBox1.Text)
        TotalPaid    = float(self._textBox3.Text)
        Change  = float(TotalPaid - TotalDue)
        DollarsDue = float(Change / 1)
        QuartersDue = int(DollarsDue * 0.25 - 1)
        DimesDue = int(DollarsDue / 10)
        NickelsDue = (DimesDue / 1)
        Dollars = float(DollarsDue * .100)
        AmountOfQuarters = int(QuartersDue * .25)
        AmountOfDimes = int(DimesDue * .10)
        AmountOfNickels = int(NickelsDue * .5)
        PenniesDue = int(Change - 10 - Dollars - AmountOfQuarters - AmountOfDimes - AmountOfNickels)
        if PenniesDue <= 0:
            PenniesDue = 0
        
        
        self._label1.Text = "Total = " + str(TotalDue)
        self._label5.Text = "Paid = " + str(TotalPaid)
        self._label4.Text = "Change = " + str(Change)
        self._label6.Text = "Quarters Due = " + str(QuartersDue)
        self._label8.Text = "Dollars Due = " + str(DollarsDue)
        self._label7.Text = "Dimes Due = " + str(DimesDue)
        self._label12.Text = "Nickels Due = "  + str(NickelsDue)
        self._label11.Text = "Pennies Due = " + str(PenniesDue)
        
        
    def Button3Click(self, sender, e):
        Application.Exit()
        
    def Label1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox3.Text = ""
        self._label1.Text = ""