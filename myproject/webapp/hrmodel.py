

def prediction_model(satisfaction_level, last_evaluation, number_project, average_montly_hours, time_spend_company,Work_accident, promotion_last_5years, Departments, salary):
    import pickle
    x = [[satisfaction_level, last_evaluation, number_project, average_montly_hours, time_spend_company, Work_accident,promotion_last_5years, Departments, salary]]
    rf = pickle.load(open('HRmodel.sav', 'rb'))
    prediction = rf.predict(x)
    return prediction
