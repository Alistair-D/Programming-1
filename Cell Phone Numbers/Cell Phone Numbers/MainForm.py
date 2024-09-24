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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DimGray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 22.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button1.Location = System.Drawing.Point(2, 385)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(243, 66)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DimGray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 22.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button2.Location = System.Drawing.Point(365, 385)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(243, 66)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DimGray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 22.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button3.Location = System.Drawing.Point(716, 385)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(243, 66)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._label1.Location = System.Drawing.Point(310, 44)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(354, 96)
        self._label1.TabIndex = 3
        self._label1.Text = "0101010101"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._label2.Location = System.Drawing.Point(310, 118)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(354, 88)
        self._label2.TabIndex = 4
        self._label2.Text = "0101010101"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._label3.Location = System.Drawing.Point(310, 206)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(354, 83)
        self._label3.TabIndex = 5
        self._label3.Text = "0101010101"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._label4.Location = System.Drawing.Point(310, 289)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(354, 83)
        self._label4.TabIndex = 6
        self._label4.Text = "0101010101"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("OCR A Extended", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._label5.Location = System.Drawing.Point(310, -1)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(354, 45)
        self._label5.TabIndex = 7
        self._label5.Text = "0101010101"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(960, 463)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Cell Phone Numbers"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "(608) 756-9442 ,  Cozumel"
        self._label2.Text = "(608) 754-7800 , Walmart"
        self._label3.Text = "1-(877)-697-8222 , Subway"
        self._label4.Text = "(608)-756-0535,  Menards"
        self._label5.Text = "(608) 756-6000 , Mercy Hospital"


    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""


    def Button3Click(self, sender, e):
        Application.Exit()