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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Navy
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Coral
        self._button1.Location = System.Drawing.Point(693, -2)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(258, 78)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Navy
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Coral
        self._button2.Location = System.Drawing.Point(693, 82)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(258, 78)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Navy
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Coral
        self._button3.Location = System.Drawing.Point(693, 166)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(258, 78)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Times New Roman", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 192)
        self._textBox1.Location = System.Drawing.Point(12, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(397, 38)
        self._textBox1.TabIndex = 4
        self._textBox1.Text = "Enter a number:"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Times New Roman", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(0, 0, 192)
        self._label1.Location = System.Drawing.Point(12, 53)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(258, 36)
        self._label1.TabIndex = 5
        self._label1.Text = "Factorial:"
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 30.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label2.Location = System.Drawing.Point(693, 318)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(258, 59)
        self._label2.TabIndex = 6
        self._label2.Text = "Prog162a"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Transparent
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 30.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label3.Location = System.Drawing.Point(693, 247)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(258, 59)
        self._label3.TabIndex = 7
        self._label3.Text = "-----"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self.ClientSize = System.Drawing.Size(949, 438)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog162a"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        input = int(self._textBox1.Text)
        for num in range (0,input+1):
            list = str(num)
            self._label1.text = list

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()

    def MainFormLoad(self, sender, e):
        pass

    def Label1Click(self, sender, e):
        pass