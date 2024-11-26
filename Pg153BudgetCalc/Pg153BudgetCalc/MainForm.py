import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(243, 414)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(482, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(86, 43)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(233, 48)
        self._label1.TabIndex = 1
        self._label1.Text = "Annual Salary:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(297, 43)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(567, 38)
        self._textBox1.TabIndex = 2
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(2, 112)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(317, 48)
        self._label2.TabIndex = 3
        self._label2.Text = "Pay Periods per year:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(297, 112)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(567, 38)
        self._textBox2.TabIndex = 4
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(2, 175)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(317, 48)
        self._label3.TabIndex = 5
        self._label3.Text = "Salary Pay per Period:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(297, 175)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(567, 38)
        self._textBox3.TabIndex = 6
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Red
        self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(885, -4)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(58, 43)
        self._button2.TabIndex = 7
        self._button2.Text = "X"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self.ClientSize = System.Drawing.Size(943, 475)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg153BudgetCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        decAnnualSalary = 0.0
        intPayPeriods = 0
        decSalary = 0
        
        decAnnualSalary = float(self._textBox1.Text)
        intPayPeriods = int(self._textBox2.Text)
        decSalary = decAnnualSalary / intPayPeriods
        self._textBox3.Text = str(round(decSalary, 2))