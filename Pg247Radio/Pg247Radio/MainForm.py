import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(249, 32)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(156, 90)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Choice 4"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(249, 119)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(156, 90)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Choice 5"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(249, 204)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(156, 90)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Choice 6"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(249, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(137, 23)
        self._label1.TabIndex = 3
        self._label1.Text = "CheckBoxes"
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(65, 65)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(129, 24)
        self._radioButton1.TabIndex = 4
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Choice 1"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(65, 151)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(129, 24)
        self._radioButton2.TabIndex = 5
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice 2"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(65, 236)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(129, 24)
        self._radioButton3.TabIndex = 6
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice 3"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(65, 22)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(137, 23)
        self._label2.TabIndex = 7
        self._label2.Text = "RadioButtons"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(218, 22)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(14, 348)
        self._label3.TabIndex = 8
        self._label3.Text = """|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

"""
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(65, 313)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(115, 41)
        self._button1.TabIndex = 9
        self._button1.Text = "Ok"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(249, 313)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(115, 41)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(435, 366)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Name = "MainForm"
        self.Text = "Pg247Radio"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass