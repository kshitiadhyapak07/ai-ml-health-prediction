import json

# File to store patient records
FILE_NAME = "patient_data.json"

#  Disease database
disease_data = [
    {
        "disease": "Flu",
        "symptoms": ["fever", "cough", "fatigue"],
        "medicines": ["Paracetamol", "Cough Syrup"],
        "treatment": "Take rest, drink fluids, and take prescribed medicines."
    },
    {
        "disease": "Migraine",
        "symptoms": ["headache", "nausea", "vomiting"],
        "medicines": ["Ibuprofen", "Sumatriptan"],
        "treatment": "Avoid bright light, take rest, and use pain relievers."
    },
    {
        "disease": "Dengue",
        "symptoms": ["fever", "rash", "joint pain"],
        "medicines": ["Paracetamol"],
        "treatment": "Drink fluids, rest, and consult a doctor immediately."
    },
    {
        "disease": "COVID-19",
        "symptoms": ["cough", "chest pain", "shortness of breath"],
        "medicines": ["Paracetamol", "Vitamin C"],
        "treatment": "Isolate, monitor oxygen, and seek medical help if severe."
    }
]

#  Load previous records
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

#  Save records
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

#  Disease prediction function
def predict_disease(user_symptoms):
    best_match = None
    max_match = 0

    for entry in disease_data:
        match_count = len(set(user_symptoms) & set(entry["symptoms"]))
        
        if match_count > max_match:
            max_match = match_count
            best_match = entry

    return best_match

#  Main Program
def main():
    print("==== Disease Prediction System ====")

    name = input("Enter your name: ")
    symptoms_input = input("Enter symptoms (comma separated): ").lower()
    user_symptoms = [s.strip() for s in symptoms_input.split(",")]

    result = predict_disease(user_symptoms)

    if result:
        print("\n Possible Disease:", result["disease"])
        print(" Medicines:", ", ".join(result["medicines"]))
        print(" Treatment:", result["treatment"])
    else:
        print(" No matching disease found")

    #  Save patient record
    records = load_data()
    records.append({
        "name": name,
        "symptoms": user_symptoms,
        "prediction": result["disease"] if result else "Unknown"
    })
    save_data(records)

    print("\n Data saved successfully!")

#  Run program
main()

