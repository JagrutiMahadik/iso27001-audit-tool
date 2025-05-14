# iso27001-audit-tool
ISO 27001 Internal Audit Tool
Overview
The ISO 27001 Internal Audit Tool is a web-based application built to help organizations conduct internal audits based on the ISO 27001 Information Security Management System (ISMS) standards. This tool provides auditors with a straightforward interface to assess an organization's compliance with the ISO 27001 standard, generate reports, and track improvements over time.

By utilizing a set of predefined audit questions, the tool evaluates various domains of information security, calculates a score based on the responses, and provides a report in both PDF and Excel formats. The application also includes user authentication, ensuring only authorized personnel can access the audit features.

Features
1. User Authentication
The tool includes a simple login system to ensure that only authenticated users can access and perform audits.

Users can register a new account or login to access the audit tool.

Passwords are hashed using SHA-256 for secure storage and validation.

2. Audit Questionnaire
The tool includes a series of predefined questions based on ISO 27001 standards, categorized into domains such as "Access Control," "HR Security," etc.

Auditors can review the questions and provide answers based on the organization's implementation of the relevant security controls.

Answers are collected through dropdown options ("Yes," "No," "Partial"), with points assigned to each answer (2 points for "Yes," 1 point for "Partial," and 0 for "No").

3. Score Calculation and Compliance Status
The tool automatically calculates a score for each domain based on the answers provided by the auditor.

The total score is calculated by summing up the scores for all domains, and the compliance status is determined:

Compliant: 100% score

Needs Improvement: 50% or more

Non-Compliant: Less than 50%

4. Report Generation
After completing the audit, users can generate a PDF and Excel report.

The PDF report includes a summary of the audit, including scores per domain, overall status, and recommendations.

The Excel report provides a detailed view of the audit, listing domains, scores, and audit metadata (e.g., auditor name, audit date).

5. Visualizations
The tool provides a bar chart visualization of compliance scores for each domain, helping auditors quickly identify areas of strength and weakness.

6. Audit History
The application allows auditors to view the history of past audits, providing a record of completed audits with the corresponding results.

Technologies Used
Streamlit: For building the web-based user interface.

Python: For backend functionality, including handling logic for scoring, report generation, and user authentication.

FPDF: For generating PDF reports.

OpenPyXL: For generating Excel reports.

Matplotlib: For charting the compliance status by domain.

JSON: For storing the audit questions.

Installation
Prerequisites
Ensure that you have Python and pip installed on your system.

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/iso27001-audit-tool.git
cd iso27001-audit-tool
Install the required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt file, you can manually install the dependencies:

bash
Copy
Edit
pip install streamlit fpdf openpyxl matplotlib
Running the Application
Start the application using Streamlit:

bash
Copy
Edit
streamlit run app.py
The app will open in your default browser, where you can begin the audit process.

Usage
Login or Register:

Users must log in to use the application. New users can register by providing a username and password.

Conduct the Audit:

After logging in, auditors will see a list of audit domains (e.g., Access Control, HR Security, etc.).

For each domain, a set of questions will be displayed. The auditor will select answers (Yes, No, Partial) for each question.

Generate Reports:

Once the audit is complete, the auditor can click the "Generate Reports" button.

The tool will generate a PDF and Excel report of the audit results.

View Audit History:

Past audit sessions are stored in the application and can be reviewed at any time.

Example Output
PDF Report: Contains a summary of the audit, including each domain's score and overall compliance status.

Excel Report: Contains detailed information about each domain, along with the scores for each question and the total score.

Future Improvements
While the current version of the ISO 27001 Audit Tool provides essential audit functionality, there are several areas for improvement and potential features for future releases:

Multi-user Support: Allow multiple auditors to perform and track audits at the same time.

Database Integration: Instead of storing user data and audit results in files, use a relational database for scalability and security.

Better User Interface: Improve the UI to make it more intuitive, with more styling and usability enhancements.

Customizable Questionnaires: Allow administrators to customize the audit questions based on their organization's needs.

Real-time Collaboration: Implement features that allow auditors to collaborate in real-time.

Additional Report Formats: Support for additional report formats (e.g., Word, CSV).

License
This project is licensed under the MIT License - see the LICENSE file for details.

Conclusion
The ISO 27001 Internal Audit Tool is designed to make the process of internal audits more efficient and accessible. It helps organizations assess their compliance with ISO 27001, track improvements, and generate detailed reports. The tool is easily extendable, and with future enhancements, it can be scaled to meet the needs of larger organizations.
