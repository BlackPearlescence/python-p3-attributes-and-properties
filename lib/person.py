#!/usr/bin/env python3

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
    def set_name(self,name):
        # 1 to 25
        if(name == ""):
            print("Name must be string between 1 and 25 characters.")
        elif(type(name) is not str):
            print("Name must be string between 1 and 25 characters.")
        elif(len(name) > 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()

    def get_name(self):
        return self._name

    def set_job(self,job):
        if(job not in self.approved_jobs):
            print("Job must be in list of approved jobs.")
        else:
            self._job = job

    def get_job(self):
        return self._job
    
    name = property(get_name,set_name,)
    job = property(get_job,set_job)

