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
        self._monthCalendar1 = System.Windows.Forms.MonthCalendar()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Tempus Sans ITC", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self._button1.Location = System.Drawing.Point(695, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(239, 84)
        self._button1.TabIndex = 0
        self._button1.Text = "Show Schedule"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Tempus Sans ITC", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Maroon
        self._button2.Location = System.Drawing.Point(695, 141)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(239, 84)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Tempus Sans ITC", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Navy
        self._button3.Location = System.Drawing.Point(695, 270)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(239, 84)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # monthCalendar1
        # 
        self._monthCalendar1.CalendarDimensions = System.Drawing.Size(2, 1)
        self._monthCalendar1.Location = System.Drawing.Point(164, -10)
        self._monthCalendar1.Name = "monthCalendar1"
        self._monthCalendar1.TabIndex = 3
        self._monthCalendar1.DateChanged += self.MonthCalendar1DateChanged
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(10, 152)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(679, 30)
        self._label1.TabIndex = 4
        self._label1.Text = "1st Period: ..."
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(11, 195)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(679, 30)
        self._label2.TabIndex = 5
        self._label2.Text = "2nd period: ..."
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(11, 235)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(679, 30)
        self._label3.TabIndex = 6
        self._label3.Text = "3rd Period: ..."
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Transparent
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(10, 270)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(679, 30)
        self._label5.TabIndex = 8
        self._label5.Text = "4th Period: ..."
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(10, 311)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(679, 30)
        self._label6.TabIndex = 9
        self._label6.Text = "5th Period: ..."
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(10, 395)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(679, 30)
        self._label7.TabIndex = 10
        self._label7.Text = "7th Period: ..."
        self._label7.Click += self.Label7Click
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(10, 356)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(679, 30)
        self._label8.TabIndex = 11
        self._label8.Text = "6th Period: ..."
        self._label8.Click += self.Label8Click
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(11, 435)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(679, 30)
        self._label4.TabIndex = 12
        self._label4.Text = "8th Period: ..."
        self._label4.Click += self.Label4Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(957, 484)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._monthCalendar1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Schedule (Craig)"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""
        self._label4.Text = ""

    def Button1Click(self, sender, e):
        self._label1.Text = "1st period : Freshman Seminar"               
        self._label2.Text = "2nd Period: Computer Programming"
        self._label3.Text = "3rd Period: Drawing 1"
        self._label5.Text = "4th Period: Ap Human Geography"
        self._label6.Text = "5th Period: BIology Honors"
        self._label7.Text = "7th Period: Spanish II"
        self._label8.Text = "6th Period: Lunch + Geometry Honors"
        self._label4.Text = "8th Period: English 9"


    def MonthCalendar1DateChanged(self, sender, e):
        pass

    def Label1Click(self, sender, e):
        pass

    def Label2Click(self, sender, e):
        pass

    def Label7Click(self, sender, e):
        pass

    def Label8Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label4Click(self, sender, e):
        pass