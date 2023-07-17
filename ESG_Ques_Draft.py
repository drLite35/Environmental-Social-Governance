import tkinter as tk

def process_company_size():
    
    answer = company_size_entry.get()

    
    if answer.lower() == 'small':
        output_label.configure(text='The company is small-sized.')
        emission_question_label.pack()
        co2_emission_entry.pack()
        submit_emission_button.pack()
        energy_question_label.pack()
        energy_consumption_entry.pack()
        submit_energy_button.pack()
        renewable_question_label.pack()
        renewable_percentage_entry.pack()
        submit_renewable_button.pack()
        waste_question_label.pack()
        waste_management_entry.pack()
        submit_waste_button.pack()
        labor_question_label.pack()
        labor_conditions_entry.pack()
        submit_labor_button.pack()
        community_question_label.pack()
        community_engagement_entry.pack()
        submit_community_button.pack()
        custom_question1_label.pack()
        custom_question1_entry.pack()
        submit_custom1_button.pack()
    elif answer.lower() == 'medium':
        output_label.configure(text='The company is medium-sized.')
        emission_question_label.pack()
        co2_emission_entry.pack()
        submit_emission_button.pack()
        energy_question_label.pack()
        energy_consumption_entry.pack()
        submit_energy_button.pack()
        renewable_question_label.pack()
        renewable_percentage_entry.pack()
        submit_renewable_button.pack()
        waste_question_label.pack()
        waste_management_entry.pack()
        submit_waste_button.pack()
        labor_question_label.pack()
        labor_conditions_entry.pack()
        submit_labor_button.pack()
        community_question_label.pack()
        community_engagement_entry.pack()
        submit_community_button.pack()
        custom_question1_label.pack()
        custom_question1_entry.pack()
        submit_custom1_button.pack()
    elif answer.lower() == 'large':
        output_label.configure(text='The company is large-sized.')
        emission_question_label.pack()
        co2_emission_entry.pack()
        submit_emission_button.pack()
        energy_question_label.pack_forget()
        energy_consumption_entry.pack_forget()
        submit_energy_button.pack_forget()
        renewable_question_label.pack_forget()
        renewable_percentage_entry.pack_forget()
        submit_renewable_button.pack_forget()
        waste_question_label.pack()
        waste_management_entry.pack()
        submit_waste_button.pack()
        labor_question_label.pack()
        labor_conditions_entry.pack()
        submit_labor_button.pack()
        community_question_label.pack()
        community_engagement_entry.pack()
        submit_community_button.pack()
        custom_question1_label.pack()
        custom_question1_entry.pack()
        submit_custom1_button.pack()
    else:
        output_label.configure(text='Invalid input. Please enter small, medium, or large.')

def process_co2_emission():
  
    emission = co2_emission_entry.get()

    # Perform necessary logic based on the answer
    emission = float(emission)
    if company_size_entry.get().lower() == 'small' or company_size_entry.get().lower() == 'medium':
        if emission < 100:
            output_label.configure(text='The company has low CO2 emissions.')
        elif 100 <= emission <= 10000:
            output_label.configure(text='The company has optimal CO2 emissions within the range.')
        elif emission > 10000:
            output_label.configure(text='The company has high CO2 emissions and needs to be monitored.')

def process_energy_consumption():
 
    consumption = energy_consumption_entry.get()

    # Perform necessary logic based on the answer
    consumption = float(consumption)
    if company_size_entry.get().lower() == 'small' or company_size_entry.get().lower() == 'medium':
        if consumption < 1000:
            output_label.configure(text='The company has low energy consumption.')
        elif 1000 <= consumption <= 10000:
            output_label.configure(text='The company has optimal energy consumption within the range.')
        elif consumption > 10000:
            output_label.configure(text='The company has high energy consumption and needs to be monitored.')

def process_renewable_percentage():
  
    percentage = renewable_percentage_entry.get()


    percentage = float(percentage)
    if company_size_entry.get().lower() == 'small' or company_size_entry.get().lower() == 'medium':
        if percentage < 25:
            output_label.configure(text='Your energy output from renewable sources is very low. You should aspire towards more renewable sources.')
        elif 25 <= percentage <= 75:
            output_label.configure(text='Your energy sourcing is optimal, but there is still scope for improvement.')
        elif percentage > 75:
            output_label.configure(text='You are on the right path with a high percentage of energy sourced from renewable sources.')
    elif company_size_entry.get().lower() == 'large':
        if percentage < 50:
            output_label.configure(text='Your energy output from renewable sources is very low. You should aspire towards more renewable sources.')
        elif 50 <= percentage <= 90:
            output_label.configure(text='Your energy sourcing is optimal, but there is still scope for improvement.')
        elif percentage > 90:
            output_label.configure(text='You are on the right path with a high percentage of energy sourced from renewable sources.')

def process_waste_management():

    waste_cost = waste_management_entry.get()


    waste_cost = float(waste_cost)
    if company_size_entry.get().lower() == 'small' or company_size_entry.get().lower() == 'medium':
        if waste_cost < 60000:
            output_label.configure(text='Your capital towards waste management is very low. It needs to be monitored and increased.')
        elif 60000 <= waste_cost <= 100000:
            output_label.configure(text='Your capital towards waste management is optimal, but there is still room for improvement.')
        elif waste_cost > 100000:
            output_label.configure(text='Your capital towards waste management is good.')
    elif company_size_entry.get().lower() == 'large':
        if waste_cost < 80000:
            output_label.configure(text='Your capital towards waste management is very low. It needs to be monitored and increased.')
        elif 80000 <= waste_cost <= 160000:
            output_label.configure(text='Your capital towards waste management is optimal, but there is still room for improvement.')
        elif waste_cost > 160000:
            output_label.configure(text='Your capital towards waste management is good.')

def process_labor_conditions():

    labor_conditions = labor_conditions_entry.get()


    labor_conditions = float(labor_conditions)
    if company_size_entry.get().lower() == 'small' or company_size_entry.get().lower() == 'medium':
        if labor_conditions < 5:
            output_label.configure(text='The company has poor labor conditions. Improvement is necessary.')
        elif 5 <= labor_conditions <= 8:
            output_label.configure(text='The company has fair labor conditions.')
        elif labor_conditions > 8:
            output_label.configure(text='The company has good labor conditions.')
    elif company_size_entry.get().lower() == 'large':
        if labor_conditions < 7:
            output_label.configure(text='The company has poor labor conditions. Improvement is necessary.')
        elif 7 <= labor_conditions <= 9:
            output_label.configure(text='The company has fair labor conditions.')
        elif labor_conditions > 9:
            output_label.configure(text='The company has good labor conditions.')

def process_community_engagement():

    community_engagement = community_engagement_entry.get()


    community_engagement = float(community_engagement)
    if company_size_entry.get().lower() == 'small' or company_size_entry.get().lower() == 'medium':
        if community_engagement < 20:
            output_label.configure(text='The company has low engagement with the community. Improvement is necessary.')
        elif 20 <= community_engagement <= 50:
            output_label.configure(text='The company has moderate engagement with the community.')
        elif community_engagement > 50:
            output_label.configure(text='The company has high engagement with the community.')
    elif company_size_entry.get().lower() == 'large':
        if community_engagement < 30:
            output_label.configure(text='The company has low engagement with the community. Improvement is necessary.')
        elif 30 <= community_engagement <= 70:
            output_label.configure(text='The company has moderate engagement with the community.')
        elif community_engagement > 70:
            output_label.configure(text='The company has high engagement with the community.')

def process_custom_question1():

    answer = custom_question1_entry.get()


    output_label.configure(text='Your input has been recorded.')

def process_custom_question2():

    answer = custom_question2_entry.get()


    output_label.configure(text='Your input has been recorded.')

def process_custom_question3():

    answer = custom_question3_entry.get()

    output_label.configure(text='Your input has been recorded.')

def process_custom_question4():

    answer = custom_question4_entry.get()

    output_label.configure(text='Your input has been recorded.')

def process_custom_question5():

    answer = custom_question5_entry.get()


    output_label.configure(text='Your input has been recorded.')


window = tk.Tk()
window.title("ESG Monitoring and Questionnaire")

question1_label = tk.Label(window, text='What is the size of the company?')
question1_label.pack()

company_size_entry = tk.Entry(window)
company_size_entry.pack()

submit_size_button = tk.Button(window, text='Submit', command=process_company_size)
submit_size_button.pack()


emission_question_label = tk.Label(window, text='What is the greenhouse gas emission of CO2 in metric tonnes?')
co2_emission_entry = tk.Entry(window)
submit_emission_button = tk.Button(window, text='Submit', command=process_co2_emission)


energy_question_label = tk.Label(window, text='What is the energy consumption of the company in megawatt-hours per year?')
energy_consumption_entry = tk.Entry(window)
submit_energy_button = tk.Button(window, text='Submit', command=process_energy_consumption)


renewable_question_label = tk.Label(window, text='What percentage of energy is sourced from renewable sources?')
renewable_percentage_entry = tk.Entry(window)
submit_renewable_button = tk.Button(window, text='Submit', command=process_renewable_percentage)


waste_question_label = tk.Label(window, text='How much capital goes towards waste management by the company?')
waste_management_entry = tk.Entry(window)
submit_waste_button = tk.Button(window, text='Submit', command=process_waste_management)


labor_question_label = tk.Label(window, text='Rate the labor conditions on a scale of 1-10 (1 = Poor, 10 = Excellent)')
labor_conditions_entry = tk.Entry(window)
submit_labor_button = tk.Button(window, text='Submit', command=process_labor_conditions)


community_question_label = tk.Label(window, text='Rate the community engagement on a scale of 1-100')
community_engagement_entry = tk.Entry(window)
submit_community_button = tk.Button(window, text='Submit', command=process_community_engagement)

custom_question1_label = tk.Label(window, text='How frequently does your fintech company conduct ESG assessments or audits of its portfolio companies?')
custom_question1_entry = tk.Entry(window)
submit_custom1_button = tk.Button(window, text='Submit', command=process_custom_question1)

custom_question2_label = tk.Label(window, text='Should the reporting framework for companies include disclosure requirements for ESG risks and opportunities? If yes, how should these be addressed in the reporting?')
custom_question2_entry = tk.Entry(window)
submit_custom2_button = tk.Button(window, text='Submit', command=process_custom_question2)

custom_question3_label = tk.Label(window, text='How does the company consider the environment, social issues, and company rules when making decisions or judging risks?')
custom_question3_entry = tk.Entry(window)
submit_custom3_button = tk.Button(window, text='Submit', command=process_custom_question3)

custom_question4_label = tk.Label(window, text='How does the company make sure it keeps user data safe and protects important financial information in accordance with its governance goals?')
custom_question4_entry = tk.Entry(window)
submit_custom4_button = tk.Button(window, text='Submit', command=process_custom_question4)

custom_question5_label = tk.Label(window, text='How does the company work to make its employees happy and encourage diversity, and how does it keep track of its progress in these areas?')
custom_question5_entry = tk.Entry(window)
submit_custom5_button = tk.Button(window, text='Submit', command=process_custom_question5)


output_label = tk.Label(window, text='')
output_label.pack()

window.mainloop()






