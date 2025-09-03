import selenium
import tkinter as tk
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        
        self.driver = LinkedInScraper.login_linkedin(email, password, job)
        #badan scrape kone
       # badan save kone
        self.driver.quit()
    
    def save_jobs_to_csv(self, jobs):
        with open("linkedin_jobs.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["Title", "Company", "Location"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs)

class LinkedInScraper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    @classmethod
    def login_linkedin(cls, email, password, job):
        driver = webdriver.Chrome()
        driver.get("https://linkedin.com/login")
        
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
        email_input.send_keys(email)
        
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        
        wait.until(EC.presence_of_element_located((By.ID, "global-nav-search")))
        print("✅ Logged in successfully!")
        
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_box.send_keys(job)
        search_box.send_keys(Keys.RETURN)
        print(f"🔍 Searching for jobs: {job}")
        
        return driver
