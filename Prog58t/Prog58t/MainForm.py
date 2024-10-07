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
        self._label1.Location = System.Drawing.Point(125, 257)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(507, 115)
        self._label1.TabIndex = 3
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
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(823, 455)
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
        Change  = float(TotalDue - TotalPaid)
        Change = float(self._label1.Text

    def Button2Click(self, sender, e):
        self._textBox1.text = ""
        self._textBox2.Text = ""
        self._label1.Text   = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label1Click(self, sender, e):
        pass