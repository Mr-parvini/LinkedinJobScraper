import tkinter as tk
import selenium 
import csv
from selenium import webdriver

class LinkedInScraperApp:
    def __init__(self, master):
        self.master = master
        self.master.title("LinkedIn Job Scraper")
        self.master.geometry("900x700")
        
        self.font_style = ("Helvetica", 10)
        self.driver = None
        
        self.create_widgets()
    
    def create_widgets(self):
        
        self.label_email = tk.Label(self.master, font=self.font_style, text="Email:")
        self.label_email.grid(row=0, column=0, sticky="e", padx=10, pady=18)
        self.entry_email = tk.Entry(self.master, font=self.font_style, width=40)
        self.entry_email.grid(row=0, column=1, padx=10, pady=18)
        
        
        self.label_password = tk.Label(self.master, font=self.font_style, text="Password:")
        self.label_password.grid(row=1, column=0, sticky="e", padx=10, pady=18)
        self.entry_password = tk.Entry(self.master, font=self.font_style, width=40, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=18)
        
        
        self.label_job = tk.Label(self.master, font=self.font_style, text="Job Title:")
        self.label_job.grid(row=2, column=0, sticky="e", padx=10, pady=18)
        self.entry_job = tk.Entry(self.master, font=self.font_style, width=40)
        self.entry_job.grid(row=2, column=1, padx=10, pady=18)
        
        
        self.result_label = tk.Label(self.master, font=self.font_style, text="", fg="blue")
        self.result_label.grid(row=4, column=0, columnspan=2)
        
        
        self.start_button = tk.Button(self.master,font=self.font_style,text="Start",command=self.start_job_finder)
        self.start_button.grid(row=5, column=0, columnspan=2, pady=18)
    
    def start_job_finder(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        job = self.entry_job.get()
        self.result_label.config(text=f"Email: {email}\nPassword: ***\nJob: {job}")
        
        #badan save kone
    
    def save_jobs_to_csv(self, jobs):
        with open("linkedin_jobs.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["Title", "Company", "Location"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs)
