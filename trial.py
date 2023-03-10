import json
from datetime import datetime
import re

class AgePrediction:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def format_date(self, collection_name):
        data = self.load_data()
        #collection_name = data[f"member{collection_name}collection"]
        for item in collection_name:
            date_str = item["date_from"]
            if date_str:
                if re.match(r'\d{4}-\d{2}-\d{2}', date_str):
                    return
                else:
                    date_str_split = str(item["date_from"]).split()
                    if len(date_str_split) == 1:
                        to_be_formatted_date = datetime.strptime(date_str, "%Y")
                    else:
                        to_be_formatted_date = datetime.strptime(date_str,"%B %Y")
                    formatted_date = to_be_formatted_date.strftime('%Y-%m-%d')
                    item["date_from"] = formatted_date     
                    with open(self.file_path, 'w') as f:
                        json.dump(data, f, indent=4)              
        

#calculate the age of a person based on current time and their date of  birth
    def calculate_duration(self, starting_date):
        today = datetime.today()
        starting_date = datetime.strptime(starting_date, '%Y-%m-%d')
        duration = today.year - starting_date.year - (today.month < starting_date.month)   #whether had their birthday this year
        return duration

    def get_education_age(self):

        high_school_terms = ['high school', '12', 'XII', 'secondary school']
        bachelors_terms = ['bachelor', 'bachelors', 'btech', 'b.tech', 'bcom', 'b.com']
        masters_terms = ['master', 'masters', 'mtech', 'mba', 'm.b.a']
     
        data = self.load_data()
        education = data["member_education_collection"]
        if education:
            self.format_date(education)
            earliest_date = min(filter(lambda x: x["date_from"] is not None, education), key=lambda x: x["date_from"])["date_from"]
            #earliest_date = min(education, key = lambda x: x['date_from'])['date_from']
            earliest_title = min(filter(lambda x: x["date_from"] is not None, education), key=lambda x: x["date_from"])["title"]
            earliest_subtitle = min(filter(lambda x: x["date_from"] is not None, education), key=lambda x: x["date_from"])["subtitle"]
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
        self.format_date(experience)
        if experience:
            earliest_date = min(filter(lambda x: x["date_from"] is not None, experience), key=lambda x: x["date_from"])["date_from"]
            if earliest_date:
                duration = self.calculate_duration(earliest_date)
                return duration+22
        return None

    def get_certifications_age(self):
        data = self.load_data()
        certifications = data.get("member_certifications_collection")
        self.format_date(certifications)
        if certifications:
            earliest_date = min(filter(lambda x: x["date_from"] is not None, certifications), key=lambda x: x["date_from"])["date_from"]
            if earliest_date:
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
        elif age_from_certifications:
            return age_from_certifications
        else:
            return None

#Driver code
filename = 'cs_profiles/' + input("Person name") + '.json'
age_predictor = AgePrediction(filename)
#age_predictor.format_date()
predicted_age = age_predictor.predict_age()
print("Predicted age:", predicted_age)