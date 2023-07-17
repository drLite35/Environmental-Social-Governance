import tkinter as tk
import sys


questions = [
    "What is the size of the company?",
    "What is the greenhouse gas emission of CO2 in metric tonnes?",
    "What is the energy consumption of the company in megawatt-hours per year?",
    "What percentage of energy is sourced from renewable sources?",
    "How much capital goes towards waste management by the company?",
    "Rate the labor conditions on a scale of 1-10 (1 = Poor, 10 = Excellent)",
    "Rate the community engagement on a scale of 1-100",
    "How frequently does your fintech company conduct ESG assessments or audits of its portfolio companies?",
    "Should the reporting framework for companies include disclosure requirements for ESG risks and opportunities? If yes, how should these be addressed in the reporting?",
    "How does the company consider the environment, social issues, and company rules when making decisions or judging risks?",
    "How does the company make sure it keeps user data safe and protects important financial information in accordance with its governance goals?",
    "How does the company work to make its employees happy and encourage diversity, and how does it keep track of its progress in these areas?",
    "What is the company doing to make sure all parts of its business, including its digital systems, are meeting standards for the environment and society?",
    "How does the company communicate its ESG strategy and performance to investors and the public?",
    "How does the company assess and manage risks associated with emerging technologies or business models?"
]


current_question = 0
company_size = ""

def display_question():
    global current_question
    question_label.configure(text=questions[current_question])
    answer_entry.delete(0, tk.END)  

def process_answer():
    global current_question, company_size
    answer = answer_entry.get()

    if current_question == 0:
        company_size = answer.lower()
        if company_size not in ["small", "medium", "large"]:
            output_label.configure(text="Invalid input. Exiting...")
            sys.exit()
        output_label.configure(text=f"The company is {company_size}-sized.")

    elif current_question == 1:
        emission = float(answer)
        if company_size == "small" or company_size == "medium":
            if emission < 100:
                output_label.configure(text='The company has low CO2 emissions.')
            elif 100 <= emission <= 10000:
                output_label.configure(text='The company has optimal CO2 emissions within the range.')
            elif emission > 10000:
                output_label.configure(text='The company has high CO2 emissions and needs to be monitored.')
        elif company_size == "large":
            if emission < 10000:
                output_label.configure(text='The company has low CO2 emissions.')
            elif 10000 <= emission <= 100000:
                output_label.configure(text='The company has optimal CO2 emissions within the range.')
            elif emission > 100000:
                output_label.configure(text='The company has high CO2 emissions and needs to be monitored.')

    elif current_question == 2:
        consumption = float(answer)
        if company_size == "small" or company_size == "medium":
            if consumption < 1000:
                output_label.configure(text='The company has low energy consumption.')
            elif 1000 <= consumption <= 10000:
                output_label.configure(text='The company has optimal energy consumption within the range.')
            elif consumption > 10000:
                output_label.configure(text='The company has high energy consumption and needs to be monitored.')
        elif company_size == "large":
            if consumption < 10000:
                output_label.configure(text='The company has low energy consumption.')
            elif 10000 <= consumption <= 100000:
                output_label.configure(text='The company has optimal energy consumption within the range.')
            elif consumption > 100000:
                output_label.configure(text='The company has high energy consumption and needs to be monitored.')

    elif current_question == 3:
        percentage = float(answer)
        if company_size == "small" or company_size == "medium":
            if percentage < 25:
                output_label.configure(text='Your energy output from renewable sources is very low. You should aspire towards more renewable sources.')
            elif 25 <= percentage <= 75:
                output_label.configure(text='Your energy sourcing is optimal, but there is still scope for improvement.')
            elif percentage > 75:
                output_label.configure(text='You are on the right path with a high percentage of energy sourced from renewable sources.')
        elif company_size == "large":
            if percentage < 50:
                output_label.configure(text='Your energy output from renewable sources is very low. You should aspire towards more renewable sources.')
            elif 50 <= percentage <= 90:
                output_label.configure(text='Your energy sourcing is optimal, but there is still scope for improvement.')
            elif percentage > 90:
                output_label.configure(text='You are on the right path with a high percentage of energy sourced from renewable sources.')

    elif current_question == 4:
        waste_cost = float(answer)
        if company_size == "small" or company_size == "medium":
            if waste_cost < 60000:
                output_label.configure(text='Your capital towards waste management is very low. It needs to be monitored and increased.')
            elif 60000 <= waste_cost <= 100000:
                output_label.configure(text='Your capital towards waste management is optimal, but there is still room for improvement.')
            elif waste_cost > 100000:
                output_label.configure(text='Your capital towards waste management is good.')
        elif company_size == "large":
            if waste_cost < 80000:
                output_label.configure(text='Your capital towards waste management is very low. It needs to be monitored and increased.')
            elif 80000 <= waste_cost <= 160000:
                output_label.configure(text='Your capital towards waste management is optimal, but there is still room for improvement.')
            elif waste_cost > 160000:
                output_label.configure(text='Your capital towards waste management is good.')

    elif current_question == 5:
        labor_conditions = float(answer)
        if company_size == "small" or company_size == "medium":
            if labor_conditions < 5:
                output_label.configure(text='The company has poor labor conditions. Improvement is necessary.')
            elif 5 <= labor_conditions <= 8:
                output_label.configure(text='The company has fair labor conditions.')
            elif labor_conditions > 8:
                output_label.configure(text='The company has good labor conditions.')
        elif company_size == "large":
            if labor_conditions < 7:
                output_label.configure(text='The company has poor labor conditions. Improvement is necessary.')
            elif 7 <= labor_conditions <= 9:
                output_label.configure(text='The company has fair labor conditions.')
            elif labor_conditions > 9:
                output_label.configure(text='The company has good labor conditions.')

    elif current_question == 6:
        community_engagement = float(answer)
        if company_size == "small" or company_size == "medium":
            if community_engagement < 20:
                output_label.configure(text='The company has low engagement with the community. Improvement is necessary.')
            elif 20 <= community_engagement <= 50:
                output_label.configure(text='The company has moderate engagement with the community.')
            elif community_engagement > 50:
                output_label.configure(text='The company has high engagement with the community.')
        elif company_size == "large":
            if community_engagement < 30:
                output_label.configure(text='The company has low engagement with the community. Improvement is necessary.')
            elif 30 <= community_engagement <= 70:
                output_label.configure(text='The company has moderate engagement with the community.')
            elif community_engagement > 70:
                output_label.configure(text='The company has high engagement with the community.')

    elif current_question == 7:
        assessment_frequency = int(answer)
        if assessment_frequency < 2:
            output_label.configure(text='The company needs improvement in conducting ESG assessments or audits of its portfolio companies.')
        elif 2 <= assessment_frequency <= 4:
            output_label.configure(text='The company conducts ESG assessments or audits of its portfolio companies at an optimal frequency.')
        elif assessment_frequency > 4:
            output_label.configure(text='The company is auditing its portfolio companies very frequently, which is a good practice.')

  
    elif current_question >= 8 and current_question <= 14:
        output_label.configure(text='Your input has been recorded.')


    if current_question < len(questions) - 1:
        current_question += 1
        display_question()
    else:
       
        output_label.configure(text="Your inputs are sent for further research, and we will reach you with further insights.")


window = tk.Tk()
window.title("ESG Monitoring and Questionnaire")


question_label = tk.Label(window, text="")
question_label.pack()

answer_entry = tk.Entry(window)
answer_entry.pack()


submit_button = tk.Button(window, text="Submit", command=process_answer)
submit_button.pack()


output_label = tk.Label(window, text="")
output_label.pack()

display_question()

window.mainloop()


