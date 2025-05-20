# SkillCraft Technology Software Development Intern batch 15Th May TO 15TH June 
# Task 1
# Create a Program that converts temperatures between Celsius , Fahrenheit and Kelvin scales

from tkinter import*

screen=Tk()
screen.title("Temperature Conversion")
screen.config(padx=100,pady=100)

def convert_kelvin(temp,temp_scale):
    if temp_scale == "F" :
        return (temp - 32) * 5//9 + 273.15
    elif temp_scale == "C":
         return round((temp + 273.15),2)
    else:
        pass


def convert_fahrenheit(temp,temp_scale):
    if temp_scale == "C":
        return (temp * 9//5) + 32
    elif temp_scale == "K":
        return (temp - 273.15) * 9//5 + 32
    else:
        pass

def convert_celsius(temp,temp_scale):
    if temp_scale == "F":
        return (temp - 32) * 5//9
    elif temp_scale == "K":
        return round((temp - 273.15),2)
    else:
        pass
def convert():

    temp=temp_entry.get()
    if temp !="":

        temp_scale=temp[::-1][0].upper()
        temp_=""
        for i in range(0,len(temp)-1):
            temp_+=temp[i]

        temp_number=int(temp_)

        if temp_scale == "C":
         temp_k=convert_kelvin(temp_number,temp_scale)
         temp_f=convert_fahrenheit(temp_number,temp_scale)
         label_output.config(text=f"Given temperature {temp_number}°C = {temp_k}K in Kelvin scale and {temp_f}°F in Fahrenheit")
        

        if temp_scale == "F":
         temp_k=convert_kelvin(temp_number,temp_scale)
         temp_c=convert_celsius(temp_number,temp_scale)
         label_output.config(text=f"Given temperature {temp_number}°F = {temp_k}K in Kelvin scale and {temp_c}°C in Celsius")
   

        if temp_scale == "K":
            temp_f=convert_fahrenheit(temp_number,temp_scale)
            temp_c=convert_celsius(temp_number,temp_scale)
            label_output.config(text=f"Given temperature {temp_number}K = {temp_c}°C in Celsius scale and {temp_f}°F in Fahrenheit")
    else:
        label_output.config(text="Empty Field")
    

    
temp_entry=Entry(width=36,borderwidth=4)
temp_entry.grid(row=1,column=1,columnspan=2,pady=20)
temp_entry.focus()

convert_button=Button(text="Convert",width=20,command=convert,borderwidth=2)
convert_button.grid(row=2,column=1,columnspan=2)

label_input=Label(text="Enter the Temperature  and also enter the scale C/F/K for Celsius/Fahrenheit/Kelvin respectively",highlightbackground="black",highlightthickness=1)
label_input.grid(row=0,column=1,columnspan=2)

label_output=Label(text="Output",borderwidth=5,font="Arial",pady=10)
label_output.grid(row=3,column=1,columnspan=2)

screen.mainloop()






