# name: Kshiti Adhyapak
# Reg No.: 25BAI10330
# PROBLEM STATEMENT
The main problem addressed by this system is the lack of a quick and reliable method for identifying diseases based on symptoms. Many people rely on self-diagnosis or delay consulting doctors, which can lead to incorrect conclusions and serious health risks. Manual analysis of symptoms is often time-consuming and prone to errors. Therefore, there is a need for an automated and user-friendly system that can analyze symptoms efficiently, predict possible diseases, provide basic treatment suggestions, and maintain patient records for future reference.
# FUNCTIONAL REQUIREMENTS 
 
The key functional requirements are: 
 1. Data Management (Persistence)
•	1. User Authentication & Profile Management
•	The system must ensure that data is secure and personalized for different user roles (Patients, Doctors, Administrators).
•	User Registration & Login: Secure signup/signin using Multi-Factor Authentication (MFA).
•	Role-Based Access Control (RBAC): Restrict data access based on the user type (e.g., a patient cannot see another patient's records).
•	Profile Management: Allow users to update personal health history, allergies, and demographic information.
•	2. Data Input & Integration
•	To predict a disease, the system needs high-quality data.
•	Symptom Entry: A user interface for patients to select symptoms from a predefined list or via natural language input.
•	Medical Record Upload: Support for uploading lab reports (PDF/Images) and integrating with Electronic Health Records (EHR).
•	Wearable Data Syncing: Functional capability to pull real-time data (heart rate, sleep patterns, SpO2) from IoT devices or smartwatches.
•	3. Disease Prediction Engine (The Core)
•	This is the functional "brain" of the application where the ML models reside.
•	Preprocessing: Automatically clean and normalize input data (e.g., converting "high fever" into a numerical value).
•	Risk Assessment: Calculate the probability of specific diseases based on input features using trained algorithms.
•	Differential Diagnosis: Provide a list of potential conditions ranked by confidence scores.
•	Trend Analysis: Analyze historical data to predict the progression of chronic diseases (e.g., predicting a diabetic spike).
•	4. Diagnostic Reporting & Visualization
•	The output must be easy for a human to interpret.
•	Report Generation: Generate a summary of the prediction, including the logic behind the result (Explainable AI).
•	Data Visualization: Display heal th trends using interactive charts (e.g., glucose levels over six months).
•	Urgency Flagging: Automatically highlight "Red Flags" that require immediate emergency intervention.
•	5. Communication & Recommendations
•	The system should act as a bridge to actual medical care.
•	Doctor Referral: Suggest nearby specialists based on the predicted condition.
•	Appointment Scheduling: Integration with booking systems to secure a consultation immediately.
Health Tips: Provide personalized lifestyle or dietary advice based on the risk profile. 
