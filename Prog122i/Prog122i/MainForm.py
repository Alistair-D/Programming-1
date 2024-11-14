import math
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
        self._listBox1 = System.Windows.Forms.ListBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(613, 11)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(336, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(613, 75)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(336, 58)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(613, 139)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(336, 58)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.ForeColor = System.Drawing.Color.Green
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 24
        self._listBox1.Location = System.Drawing.Point(12, 11)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(595, 436)
        self._listBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 25.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Green
        self._label1.Location = System.Drawing.Point(668, 291)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(228, 54)
        self._label1.TabIndex = 4
        self._label1.Text = "Program122i"
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 25.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Green
        self._label2.Location = System.Drawing.Point(613, 237)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(336, 54)
        self._label2.TabIndex = 5
        self._label2.Text = "--------------------------"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(961, 447)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog122i"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        header = "Number" + "\t" + "Cube Root" + "\t" + "Cube"
        self._listBox1.Items.Add(header)
        for nums in range(-25,26):
            CubeRoot = float(abs(nums) ** (1/3.00))
            if nums < 0:
                CubeRoot = 0 - CubeRoot 
            
            Cubed = abs(nums) ** 3
            if nums < 0:
                Cubed = 0 - Cubed
            
            List = str(nums) + "\t" + str(CubeRoot) + "\t" + str(Cubed)
            self._listBox1.Items.Add(List)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()