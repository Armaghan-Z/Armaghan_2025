---
layout: post
title: "AP CSP Final Review Preparation"
permalink: /finalblog/
categories: [CSP, Retrospective]
tags: [AP CSP, Study Log, Full-Stack, CPT]
---

# AP CSP Final Review Preparation

## 1. Project Feature Blog (CPT/FRQ Write-Up)

### Project: Study Log Feature

#### Purpose & Function
The Study Log feature allows users to log their study hours, subjects, and notes. It provides an interactive way for students to track their learning progress. The feature includes:

- A **user-friendly UI** for adding/editing/deleting logs
- **Persistent data storage** with a relational database
- **Backend API** to handle CRUD operations
- **Authentication & authorization** to ensure only logged-in users access logs

#### CPT-Required Code Segment & Explanation
The backend API processes and stores study log data securely. Below is an example of how a new study log is created:

```python
@app.route('/api/studylognew', methods=['POST'])
def create_studylog():
    data = request.get_json()
    new_log = StudyLog(
        user_id=data['user_id'],
        subject=data['subject'],
        hours_studied=data['hours_studied'],
        notes=data.get('notes', '')
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify(new_log.read()), 201
```

- **Input:** JSON request containing study log details
- **Processing:** The function extracts the data, creates an entry in the database, and commits it
- **Output:** Returns the newly created log in JSON format

#### CPT Requirements Addressed
- ✅ **Data abstraction:** Logs are stored in a structured relational database
- ✅ **Algorithm implementation:** Functions for creating, reading, updating, and deleting logs
- ✅ **Procedural abstraction:** The API follows RESTful principles for structured data handling
- ✅ **Impact on society:** Helps students track their study habits, improving academic performance

## 2. Retrospective Blog (5 Key Contributions, Issues, & Burndown Analysis)

### 5 Key Contributions Over 12 Weeks

#### 1. Developed and Optimized a Full-Stack Study Log Feature
- Designed and implemented a **responsive front-end** using **HTML, CSS, and JavaScript**
- Built a **secure RESTful API** to handle CRUD operations efficiently
- Integrated the system with a **relational database (SQLAlchemy)**, ensuring persistent storage of user study logs
- **Example:** Users can log their study hours for "AP Computer Science" and retrieve past logs by selecting a date range

#### 2. Implemented Secure User Authentication & Role-Based Access Control
- Integrated **JWT-based authentication** to ensure only authorized users could access study logs
- Established **hashed passwords and session management** for security
- Restricted API endpoints based on user roles to **prevent unauthorized access**
- **Example:** If a user attempts to edit another person's study log, they will receive an **unauthorized access error (403 Forbidden)**

#### 3. Refined the Deployment Process and Fixed Major Production Bugs
- Assisted in deploying the project to a **live server**, ensuring a stable environment
- Debugged and resolved **CORS issues** that initially prevented API calls from functioning correctly
- Fixed **database migration errors**, ensuring smooth data consistency across deployments
- Implemented **error logging and monitoring**, improving system stability and debugging efficiency
- **Example:** During deployment, I identified an issue where study logs weren't saving due to a missing migration step. By applying `flask db migrate && flask db upgrade`, the issue was resolved

#### 4. Enhanced UI/UX for a Better User Experience
- Improved **mobile responsiveness**, ensuring the study log feature is accessible on all devices
- Added a **dark mode toggle** and adjusted color contrast to improve readability
- Integrated **interactive animations** and transitions to enhance the look and feel
- Simplified the form submission process by adding **real-time validation** and tooltips for better usability
- **Example:** If a user tries to submit a log with an empty subject field, a message now appears: **"Subject is required"**

#### 5. Collaborated Effectively and Contributed to Project Scalability
- Participated in **team code reviews**, ensuring high-quality, maintainable code
- Designed the study log system to be **modular and scalable**, making it easy to integrate with future features
- Documented API endpoints and **wrote clear README instructions** for future contributors
- Assisted peers with **debugging and deployment issues**, ensuring a smooth development cycle
- **Example:** I worked with another teammate to fix an API bug where duplicate study logs were being created due to improper ID handling. We added a unique constraint to resolve it

### Challenges Faced & Solutions

| Issue | Solution |
|-------|----------|
| UI was not responsive on mobile | Used CSS flexbox and media queries |
| API had security vulnerabilities | Implemented authentication & validation |
| Database performance issues | Optimized queries & indexed tables |
| Difficulty in deployment | Debugged server logs and fixed config errors |
| Users wanted more features | Added customization and filtering options |

## Final Submission Checklist

✅ Study Log Feature demo prepared  
✅ Blog posts written using **CPT/FRQ language**  
✅ Burndown chart ready  
✅ MCQ integrated into the review  
✅ Live review script practiced  
✅ Screenshots prepared for UI, API, database, and project progress  
✅ Strong **final reflection** ready to impress the teacher
