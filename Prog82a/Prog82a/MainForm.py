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
        self._label4 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(333, 228)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(280, 60)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(333, 360)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(280, 60)
        self._button2.TabIndex = 1
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(333, 294)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(280, 60)
        self._button3.TabIndex = 2
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(379, 84)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(186, 32)
        self._label1.TabIndex = 3
        self._label1.Text = "Fine:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(12, 27)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(232, 32)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Transparent
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(232, 32)
        self._label2.TabIndex = 5
        self._label2.Text = "Speed Limit"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Transparent
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(364, 116)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(232, 32)
        self._label3.TabIndex = 6
        self._label3.Text = "Output"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Transparent
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 186)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(232, 32)
        self._label4.TabIndex = 7
        self._label4.Text = "Vehicle Speed"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(12, 151)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(232, 32)
        self._textBox2.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self.ClientSize = System.Drawing.Size(667, 422)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()

    Speedl = 0
    Speed = 0
    Charge = 20.00
    Addition = 0.0

    def Button1Click(self, sender, e):
        Speedl = self._textBox1.Text
        Speed = self._textBox2.Text
        if Speed < Speedl:
            self._label1.Text = "No Fine"
        elif Speed > Speed1:
            self._label1.Text = "Fine:" + str(Charge) 

    def Button3Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass