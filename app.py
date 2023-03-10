'''import json

filename = 'cs_profiles/' + input("Person name") + '.json'

with open(filename, 'r', encoding='utf-8') as fobj:
  data = json.load(fobj)
  education_data = data['member_education_collection']
  experience_data = data['member_experience_collection']
  certifications_data  = data['member_certifications_collection']
  for i in education_data:
    print(i['date_from'])'''
#+==========================================================================

import json
from datetime import datetime

class AgePrediction:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def format_date(self):
        data = self.load_data()
        education = data.get("member_education_collection")
        for item in education:
            date_str = item["date_from"]
            date_str_split = item.get("date_from").split()
            if len(date_str_split) == 1:
                to_be_formatted_date = datetime.strptime(date_str, "%Y")
            else:
                to_be_formatted_date = datetime.strptime(date_str, "%B" "%Y")
            formatted_date = to_be_formatted_date.strftime('%Y-%m-%d')
            item["date_from"] = formatted_date
            
            with open(self.sile_path, 'w') as f:
                json.dump(education, f, indent=4)              
        

#calculate the age of a person based on current time and their date of  birth
    def calculate_duration(self, starting_date):
        today = datetime.today()
        duration = today.year - starting_date.year - (today.month < starting_date.month)   #whether had their birthday this year
        return duration

    def get_education_age(self):
        high_school_terms = ['high school', '12', 'XII', 'secondary school']
        bachelors_terms = ['bachelor', 'bachelors', 'btech', 'b.tech', 'bcom', 'b.com']
        masters_terms = ['master', 'masters', 'mtech', 'mba', 'm.b.a']
    
        data = self.load_data()
        education = data.get("member_education_collection")
        if education:
            self.format_date()
            earliest_date = min(education, key = lambda x: x['date_from'])['date_from']
            earliest_title = min(education, key = lambda x: x['date_from'])['title']
            earliest_subtitle = min(education, key = lambda x: x['date_from'])['subtitle']
            #if earliest_data:
             #   edu_date = earliest_date.split()
              #  if len(edu_data) == 1:
               #     earliest_date = datetime.strptime(earliest_date, "%Y")
                #else:
                 #   earliest_date = datetime.strptime(earliest_date, "%B" "%Y")
                 
            duration = self.calculate_duration(earliest_date)
            for i in high_school_terms:
                if i in earliest_title.lower() or i in earliest_subtitle.lower():
                    return duration+18
            for i in bachelors_terms:
                if i in earliest_title.lower() or i in earliest_subtitle.lower():
                    return duration+22
            for i in masters_terms:
                if i in earliest_title.lower() or i in earliest_subtitle.lower():
                    return duration+24
            return duration+18
        return None

    def get_experience_age(self):
        data = self.load_data()
        experience = data.get("member_experience_collection")
        if experience:
            earliest_date = min(experience, key = lambda x: x['date_from'])['date_from']
            if earliest_date:
                exp_date = earliest_date.split()
                if len(exp_date) == 1:
                    earliest_date = datetime.strptime(earliest_date, "%Y")
                else:
                    earliest_date = datetime.strptime(earliest_date, "%B" "%Y")
                duration = self.calculate_duration(earliest_date)
                return duration+22
        return None

    def get_certificatios_age(self):
        data = self.load_data()
        certifications = data.get("member_certifications_collection")
        if certifications:
            earliest_date = min(certifications, key = lambda x: x['date_from'])['date_from']
            if earliest_date:
                cert_date = earliest_date.split()
                if len(cert_date) == 1:
                    earliest_date = datetime.strptime(earliest_date, "%Y")
                else:
                    earliest_date = datetime.strptime(earliest_date, "%B" "%Y")
                duration = self.calculate_duration(earliest_date)
                return duration+22
        return None

    def predict_age(self):
        age_from_education = self.get_education_age()
        age_from_experience = self.get_experience_age()
        age_from_certifications = self.get_certifications_age()
        
        if age_from_education:
            return age_from_education
        elif age_from_experience:
            return age_from_experience
        elif age_from_experience:
            return age_from_experience
        else:
            return None

#Driver code
filename = 'cs_profiles/' + input("Person name") + '.json'
age_predictor = AgePrediction(filename)
age_predictor.format_date()
predicted_age = age_predictor.predict_age()
print("Predicted age:", predicted_age)