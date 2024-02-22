import tkinter as tk
from tkinter import messagebox
class ToDo:

    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('500x500')
        self.root.title("To Do List")
        self.widgets()
        self.root.protocol("WM_DELETE_WINDOW",self.quit)
        self.root.mainloop()

    def widgets(self):
        self.text=tk.Entry(self.root,font=('Arial',18))
        self.text.pack(padx=10,pady=10)

        self.btn1=tk.Button(self.root,text="Add task",font=('Arial',14),command=self.add_tasks,bg='#87CEEB')
        self.btn1.pack(padx=10,pady=10)

        self.list=tk.Listbox(self.root)
        self.list.pack(padx=10,pady=10)

        self.btn_frame=tk.Frame(self.root)
        self.btn_frame.pack(padx=5)

        self.btn2=tk.Button(self.btn_frame,text="Edit",command=self.edit_tasks,bg='#87CEEB')
        self.btn2.grid(row=0,column=0,padx=10)

        self.btn3=tk.Button(self.btn_frame,text="Delete",command=self.delete_tasks,bg='#87CEEB')
        self.btn3.grid(row=0,column=1,pady=10)

        self.btn4=tk.Button(self.btn_frame,text="Priority",command=self.prior,bg='#87CEEB')
        self.btn4.grid(row=0,column=2,padx=10)

        self.frame1=tk.Frame(self.root)
        self.frame1.pack()

        self.text1=tk.Label(self.frame1,text="Enter Priority:")
        self.text1.grid(row=0,column=0,padx=5)

        self.proiority=tk.Entry(self.frame1)
        self.proiority.grid(row=0,column=1,padx=5)


        
    

    def add_tasks(self):
        task=self.text.get()
        if task:
            self.list.insert(tk.END,task)
            self.text.delete(0,tk.END)

    def edit_tasks(self):
        task_index=self.list.curselection()
        if task_index:
            new_task=self.text.get()
            if new_task:
                self.list.delete(task_index)
                self.list.insert(task_index,new_task)
                self.text.delete(0,tk.END)

    def delete_tasks(self):
        task_index=self.list.curselection()
        if task_index:
            self.list.delete(task_index)

    def prior(self):
        task_index=self.list.curselection()
        if task_index:
            index=task_index[0]
            val=self.list.get(index)
            prior_no=self.proiority.get()
            self.proiority.delete(0,tk.END)
            self.list.insert(prior_no,val)
            self.delete_tasks()


    def quit(self):
        if messagebox.askyesno(title="Quit?",message="Do you want to really quit?"):
            self.root.destroy()


ToDo()