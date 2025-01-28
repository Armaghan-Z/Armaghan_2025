---
layout: page
title: My Sprint 5
permalink: /sprint5/
---

# Individual Feature Documentation: Study Log

## Overview
The Study Log feature provides a comprehensive system to log, retrieve, update, and delete study sessions. This feature is implemented using a full-stack approach, consisting of frontend, backend, and database integration. Below is a detailed account of the design, implementation, and functionality of this feature, along with the requirements met for the AP Computer Science Principles Create Task.

---

## Purpose
- **Group Program Purpose**: The group's project aims to provide a user-friendly application that supports tracking academic progress through features like study logs and grade tracking.
- **Individual Feature Purpose**: The Study Log feature allows users to log their study sessions, retrieve records, and manage them efficiently, enabling students to monitor their academic efforts over time.

---

## Input/Output

### **Frontend Input and API Integration**
#### Adding a Study Log
1. **Frontend Form Submission**: Users provide the following inputs:
   - Subject
   - Hours Studied
   - Notes (optional)

2. **API Request**: The frontend sends the input as a `POST` request to the API endpoint:
```javascript
fetch('http://127.0.0.1:8887/api/studylognew', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        user_id: 1, // Replace with actual user ID
        subject,
        hours_studied: parseFloat(hours),
        notes
    }),
    credentials: 'include',
});
```

3. **Response**: The API responds with the created log in JSON format, which is dynamically displayed in the frontend DOM.

<img src="/Armaghan_2025/assets/Images/input1.png" width= 600px height=450px>

#### Viewing Logs
- The frontend fetches logs via a `GET` request:
```javascript
fetch('http://127.0.0.1:8887/api/studylognew', {
    credentials: 'include'
});
```
- The response contains a list of logs, formatted and displayed using JavaScript.

<img src="/Armaghan_2025/assets/Images/form1.png" width= 600px height=450px>

---

## Raw API Demo

### **Using Postman**
#### **1. POST Request**
- **Request**:
```json
{
    "user_id": 1,
    "subject": "Math",
    "hours_studied": 2.5,
    "notes": "Reviewed algebra."
}
```
- **Response**:
```json
{
    "id": 4,
    "user_id": 1,
    "subject": "Math",
    "hours_studied": 2.5,
    "notes": "Reviewed algebra.",
    "date": "2025-01-27 14:00:00"
}
```

#### **2. GET Request**
- **Response**:
```json
[
    {
        "id": 1,
        "user_id": 1,
        "subject": "Science",
        "hours_studied": 1.5,
        "notes": "Physics concepts.",
        "date": "2025-01-26 10:00:00"
    },
    ...
]
```

#### **3. Error Response**
- **Request**: Missing `subject`
```json
{
    "user_id": 1,
    "hours_studied": 2.5,
    "notes": "Reviewed algebra."
}
```
- **Response**:
```json
{
    "message": "Subject is required"
}
```

<img src="/Armaghan_2025/assets/Images/post1.png" width= 600px height=450px>

---

## Data Operations

### **Database Interactions**
1. **List (Rows)**:
   - Query to retrieve logs:
   ```python
   logs = StudyLog.query.all()
   ```
   - This returns a list of logs, each represented as a Python object.

2. **Dictionary (Columns)**:
   - Columns like `id`, `user_id`, `subject`, `hours_studied`, and `notes` are managed as attributes of the `StudyLog` model.

3. **Formatting API Response**:
   - Data is formatted as JSON:
   ```python
   {
       "id": self.id,
       "user_id": self.user_id,
       "subject": self.subject,
       "hours_studied": self.hours_studied,
       "notes": self.notes,
       "date": self.date.strftime('%Y-%m-%d %H:%M:%S')
   }
   ```

---

## Algorithms and Methods

### **RESTful API Implementation**
1. **Methods in API Class**:
   - `GET`: Retrieves all logs.
   - `POST`: Adds a new log.
   - `PUT`: Updates an existing log.
   - `DELETE`: Deletes a log.

2. **Sample `POST` Method**:
```python
@token_required()
def post(self):
    data = request.get_json()
    studylog = StudyLog(
        user_id=data['user_id'],
        subject=data['subject'],
        hours_studied=data['hours_studied'],
        notes=data['notes']
    )
    studylog.create()
    return jsonify(studylog.read())
```

### **Restore Functionality**
- Avoids duplicates by checking for existing records:
```python
existing_log = StudyLog.query.filter_by(user_id=log_data['user_id'], subject=log_data['subject']).first()
if existing_log:
    existing_log.update(log_data)
else:
    new_log = StudyLog(**log_data)
    db.session.add(new_log)
```

---

## Observations
- **Frontend**: Dynamic interaction through `fetch` API calls.
- **Error Handling**: Demonstrated robust error responses for invalid or incomplete requests.
- **REST Principles**: Proper use of `GET`, `POST`, `PUT`, and `DELETE`.
- **Database Backup/Restore**: Recovery of data using structured restore logic.


---

## Learning Outcomes
- Demonstrates how programming is a collaborative and creative process.
- Implements a program that solves a problem, enables innovation, and explores creativity.
- Follows structured review and testing methodologies to improve software quality.

**Reference**: [AP CSP Course and Exam Description](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-course-and-exam-description.pdf)

---

This documentation covers the detailed implementation of the Study Log feature, tying it to the learning objectives of the AP CSP Create Task and demonstrating its technical components through examples.

