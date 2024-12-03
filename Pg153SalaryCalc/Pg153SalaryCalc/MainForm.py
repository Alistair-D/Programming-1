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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._label12 = System.Windows.Forms.Label()
        self._textBox9 = System.Windows.Forms.TextBox()
        self._label13 = System.Windows.Forms.Label()
        self._textBox10 = System.Windows.Forms.TextBox()
        self._label14 = System.Windows.Forms.Label()
        self._textBox11 = System.Windows.Forms.TextBox()
        self._label15 = System.Windows.Forms.Label()
        self._textBox12 = System.Windows.Forms.TextBox()
        self._label16 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(1, 431)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(200, 51)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate Changes"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(359, 431)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(241, 51)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(818, 431)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(144, 51)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(505, 44)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(158, 23)
        self._label1.TabIndex = 3
        self._label1.Text = "Today's Date:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Transparent
        self._label2.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(85, 44)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(295, 52)
        self._label2.TabIndex = 4
        self._label2.Text = "Highlander Hotel"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(467, 82)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(158, 23)
        self._label3.TabIndex = 5
        self._label3.Text = "Time:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(631, 47)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(156, 26)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(631, 79)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(156, 26)
        self._textBox2.TabIndex = 7
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(28, 141)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(324, 146)
        self._label4.TabIndex = 8
        self._label4.Text = "Room Info"
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(165, 212)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(156, 26)
        self._textBox3.TabIndex = 12
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(165, 180)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(156, 26)
        self._textBox4.TabIndex = 11
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(40, 215)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(119, 23)
        self._label5.TabIndex = 10
        self._label5.Text = "Night Change:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(40, 180)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(119, 23)
        self._label6.TabIndex = 9
        self._label6.Text = "Nights:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.TopRight
        self._label6.Click += self.Label6Click
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(557, 212)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(156, 26)
        self._textBox5.TabIndex = 17
        self._textBox5.TextChanged += self.TextBox5TextChanged
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(557, 180)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(156, 26)
        self._textBox6.TabIndex = 16
        self._textBox6.TextChanged += self.TextBox6TextChanged
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 10.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(432, 215)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(119, 23)
        self._label7.TabIndex = 15
        self._label7.Text = "Telephone:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label7.Click += self.Label7Click
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(432, 180)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(119, 23)
        self._label8.TabIndex = 14
        self._label8.Text = "Room Service:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.TopRight
        self._label8.Click += self.Label8Click
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(420, 141)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(324, 146)
        self._label9.TabIndex = 13
        self._label9.Text = "Additional Charges"
        self._label9.Click += self.Label9Click
        # 
        # textBox7
        # 
        self._textBox7.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox7.Location = System.Drawing.Point(557, 244)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(156, 26)
        self._textBox7.TabIndex = 19
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 10.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(432, 247)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(119, 23)
        self._label10.TabIndex = 18
        self._label10.Text = "Misc:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label10.Click += self.Label10Click
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(1, 306)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(935, 122)
        self._label11.TabIndex = 20
        self._label11.Text = "Output"
        # 
        # textBox8
        # 
        self._textBox8.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox8.Location = System.Drawing.Point(224, 317)
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(156, 26)
        self._textBox8.TabIndex = 23
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(85, 317)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(133, 23)
        self._label12.TabIndex = 22
        self._label12.Text = "Room Charges:"
        # 
        # textBox9
        # 
        self._textBox9.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox9.Location = System.Drawing.Point(535, 317)
        self._textBox9.Name = "textBox9"
        self._textBox9.Size = System.Drawing.Size(156, 26)
        self._textBox9.TabIndex = 25
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(410, 317)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(119, 23)
        self._label13.TabIndex = 24
        self._label13.Text = "Add. Charges:"
        self._label13.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # textBox10
        # 
        self._textBox10.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox10.Location = System.Drawing.Point(224, 346)
        self._textBox10.Name = "textBox10"
        self._textBox10.Size = System.Drawing.Size(156, 26)
        self._textBox10.TabIndex = 27
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(85, 346)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(133, 23)
        self._label14.TabIndex = 26
        self._label14.Text = "Subtotal:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # textBox11
        # 
        self._textBox11.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox11.Location = System.Drawing.Point(535, 349)
        self._textBox11.Name = "textBox11"
        self._textBox11.Size = System.Drawing.Size(156, 26)
        self._textBox11.TabIndex = 29
        # 
        # label15
        # 
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(410, 349)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(119, 23)
        self._label15.TabIndex = 28
        self._label15.Text = "Tax:"
        self._label15.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # textBox12
        # 
        self._textBox12.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox12.Location = System.Drawing.Point(410, 395)
        self._textBox12.Name = "textBox12"
        self._textBox12.Size = System.Drawing.Size(156, 26)
        self._textBox12.TabIndex = 31
        # 
        # label16
        # 
        self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(285, 395)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(119, 23)
        self._label16.TabIndex = 30
        self._label16.Text = "Total Charges:"
        self._label16.TextAlign = System.Drawing.ContentAlignment.TopRight
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(960, 483)
        self.Controls.Add(self._textBox12)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._textBox11)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._textBox10)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._textBox9)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._textBox8)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._textBox7)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg153SalaryCalc"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()



    def MainFormLoad(self, sender, e):
        self._lblDateToday.Text = date.today().strftime("%A,%B %D, %Y")
        self._lblTimeToday.Text = time.strfTime("XI: %M:%S %P")
    
    def Label3Click(self, sender, e):
        pass

    def Label6Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        pass