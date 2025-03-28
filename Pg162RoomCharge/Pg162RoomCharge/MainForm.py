﻿import time
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *


class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox13 = System.Windows.Forms.TextBox()
        self._label14 = System.Windows.Forms.Label()
        self._dateTimePicker1 = System.Windows.Forms.DateTimePicker()
        self._label12 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("PMingLiU-ExtB", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(39, 38)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(420, 47)
        self._label1.TabIndex = 0
        self._label1.Text = "Highlander Hotel"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(504, 44)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(192, 47)
        self._label2.TabIndex = 1
        self._label2.Text = "Today's Date:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(471, 91)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(192, 47)
        self._label3.TabIndex = 2
        self._label3.Text = "Time:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(669, 240)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(189, 29)
        self._textBox3.TabIndex = 8
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(669, 193)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(189, 29)
        self._textBox4.TabIndex = 7
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(471, 233)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(192, 47)
        self._label4.TabIndex = 6
        self._label4.Text = "Telephone:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(504, 186)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(192, 47)
        self._label5.TabIndex = 5
        self._label5.Text = "Room service:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(235, 240)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(189, 29)
        self._textBox5.TabIndex = 12
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(235, 193)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(189, 29)
        self._textBox6.TabIndex = 11
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(37, 233)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(192, 47)
        self._label6.TabIndex = 10
        self._label6.Text = "Nightly Charges:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(39, 186)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(192, 47)
        self._label7.TabIndex = 9
        self._label7.Text = "Nights:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(209, 353)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(192, 47)
        self._label8.TabIndex = 14
        self._label8.Text = "Additional Charges:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.BottomRight
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(242, 319)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(192, 47)
        self._label9.TabIndex = 13
        self._label9.Text = "Room Charges:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(209, 468)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(192, 47)
        self._label10.TabIndex = 18
        self._label10.Text = "Tax:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(209, 421)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(192, 47)
        self._label11.TabIndex = 17
        self._label11.Text = "Subtotal:"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(242, 503)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(192, 47)
        self._label13.TabIndex = 21
        self._label13.Text = "Total Charges:"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 550)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(162, 49)
        self._button1.TabIndex = 24
        self._button1.Text = "Calculate Charges"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(418, 553)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(162, 49)
        self._button2.TabIndex = 25
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(789, 550)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(162, 49)
        self._button3.TabIndex = 26
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox13
        # 
        self._textBox13.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox13.Location = System.Drawing.Point(669, 279)
        self._textBox13.Name = "textBox13"
        self._textBox13.Size = System.Drawing.Size(189, 29)
        self._textBox13.TabIndex = 29
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(504, 272)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(192, 47)
        self._label14.TabIndex = 27
        self._label14.Text = "Misc:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # dateTimePicker1
        # 
        self._dateTimePicker1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._dateTimePicker1.Location = System.Drawing.Point(669, 56)
        self._dateTimePicker1.Name = "dateTimePicker1"
        self._dateTimePicker1.Size = System.Drawing.Size(282, 26)
        self._dateTimePicker1.TabIndex = 30
        self._dateTimePicker1.ValueChanged += self.DateTimePicker1ValueChanged
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.White
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(669, 104)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(261, 23)
        self._label12.TabIndex = 31
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.White
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(418, 379)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(261, 23)
        self._label15.TabIndex = 32
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.White
        self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(418, 332)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(261, 18)
        self._label16.TabIndex = 33
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.White
        self._label17.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(418, 434)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(261, 23)
        self._label17.TabIndex = 34
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.White
        self._label18.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.Location = System.Drawing.Point(418, 481)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(261, 25)
        self._label18.TabIndex = 35
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.White
        self._label19.Font = System.Drawing.Font("Microsoft Sans Serif", 12.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label19.Location = System.Drawing.Point(418, 516)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(261, 23)
        self._label19.TabIndex = 36
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(954, 611)
        self.Controls.Add(self._label19)
        self.Controls.Add(self._label18)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._dateTimePicker1)
        self.Controls.Add(self._textBox13)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg162RoomCharge"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        self._label12.Text = time.strftime("%I: %M: %S: %p")
        
    
    def Button1Click(self, sender, e):
        decRoomCharges = 0.0
        decAddCharges = 0.0
        decSubtotal = 0.0
        decTax = 0.0
        decTotal = 0.0
        decTAX_RATE = 0.08
        
        try:
            decAddCharges = float(self._textBox4.Text) + \
                float(self._textBox3.Text) + \
                float(self._textBox13.Text)
            self._label15.Text = str(round(decAddCharges, 2))
        except:
            MessageBox.Show("Room Service, Telephone and Misc. must be numbers", "Error")
            
        try:
            decRoomCharges = float(self._textBox6.Text) * \
                float(self._textBox5.Text)
            self._label16.Text = str(round(decRoomCharges, 2))
        except:
            MessageBox.Show("Nights and Nightly Charges must be numbers", "Error")
        
        #Subtotal
        decSubtotal = decRoomCharges + decAddCharges
        self._label17.Text = str(round(decSubtotal, 2))


        #Tax
        decTax = decSubtotal * decTAX_RATE
        self._label18.Text = str(round(decTax, 2))
        
        #Total
        decTotal = decSubtotal + decTax
        self._label19.Text = str(round(decTotal, 2))
        
    def Button2Click(self, sender, e):
        self._textBox6.Text = ""
        self._textBox5.Text = ""
        self._textBox3.Text = ""
        self._textBox13.Text = ""
        self._textBox4.Text = ""
        self._label16.Text = ""
        self._label15.Text = ""
        self._label17.Text = ""
        self._label18.Text = ""
        self._label19.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def DateTimePicker1ValueChanged(self, sender, e):
        pass