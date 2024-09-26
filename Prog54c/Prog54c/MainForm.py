import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("Prog54c.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 25.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(91, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(274, 46)
        self._textBox1.TabIndex = 0
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Coral
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(-1, 360)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(228, 75)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Coral
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(352, 360)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(228, 75)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Coral
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(707, 360)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(228, 75)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.CornflowerBlue
        self._label1.Location = System.Drawing.Point(-1, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 66)
        self._label1.TabIndex = 4
        self._label1.Text = "Enter Radius here:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.ForeColor = System.Drawing.Color.Cornsilk
        self._label2.Location = System.Drawing.Point(-1, 323)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(936, 23)
        self._label2.TabIndex = 5
        self._label2.Text = resources.GetString("label2.Text")
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.CornflowerBlue
        self._label3.Location = System.Drawing.Point(-1, 116)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 66)
        self._label3.TabIndex = 6
        self._label3.Text = "Area:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 25.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(105, 136)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(274, 46)
        self._textBox2.TabIndex = 7
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.CornflowerBlue
        self._label4.Location = System.Drawing.Point(187, 67)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 66)
        self._label4.TabIndex = 8
        self._label4.Text = """I
I
V
"""
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 25.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(105, 208)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(274, 46)
        self._textBox3.TabIndex = 10
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.CornflowerBlue
        self._label5.Location = System.Drawing.Point(-1, 188)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(112, 66)
        self._label5.TabIndex = 9
        self._label5.Text = "C :"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlText
        self.ClientSize = System.Drawing.Size(936, 434)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass
    
    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass