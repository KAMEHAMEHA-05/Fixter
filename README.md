# Fixter
Fixter is a Streamlit based web application designed for hostel residents to report any issues they encounter. Utilizing our internally developed AI technology, the app categorizes and prioritizes these issues, subsequently assigning them to the appropriate housekeeping staff for resolution. This streamlined process minimizes both the time and frustration typically associated with issue resolution, eliminating the need for residents to follow up on problem resolution.

## Explanation of each module:
1. **Login Module (Login.py)**: This pivotal module orchestrates user authentication, facilitating both login and logout functionalities within the application.

2. **Credential Storage (cred.txt)**: Serving as a rudimentary cookie system, this file stores pertinent user details post-login for subsequent interactions.

3. **Issue Management and Prioritization (fixterai.py)**: Housing both the categorization AI and a prioritization algorithm, this module systematically assigns priorities to queued issues. Additionally, it coordinates the allocation of tasks to domain-specific staff members for prompt issue resolution.

4. **Database Interaction (fixtermdb.py)**: Essential functions enabling seamless communication between the application and the MongoDB database are encapsulated within this module.

5. **SMS Communication (fixtersms.py)**: Leveraging the Twilio API, this module facilitates direct communication with housekeeping staff members via SMS, ensuring timely and efficient issue resolution.

6. **Website Pages (Pages Folder)**: This directory encompasses various pages integral to the functionality of our website:

    a. *Raise Ticket Page*: Users utilize this page to submit tickets outlining encountered issues. Details such as issue category, title, brief description, and location are provided.
    
    b. *Issue Status Page*: Offering users real-time visibility into the status of their submitted tickets, this page enables issue closure upon resolution. Furthermore, users can rate the performance of staff   members, thereby influencing their future workload.
    
    c. *Community Issues Page*: Designed for communal awareness, this page presents ongoing community issues to prevent duplicate submissions and streamline issue resolution efforts. Users can review existing problems before posting new ones, fostering efficiency and collaboration.

The AI Model is available at : [https://drive.google.com/drive/folders/1WbPb1ahPVyFlO_W2XPGYmLUypm9tdfkL?usp=sharing]
fixterai.py contains appropriate comments to know the appropriate place to put this model in the code
By placing the above files in the same structure one can run the following command in the command line to start Login.py, in a python environment :
streamlit run "Login.py"

The Mongo Folder contains JSON files to all the collections in the database Fixter.
   
