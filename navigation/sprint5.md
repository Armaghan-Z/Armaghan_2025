---
layout: page
title: My Sprint 5
permalink: /sprint5/
---

# **Individual Feature Documentation: Study Log**

Below is a concise but robust documentation of the **Study Log** feature, meeting AP Computer Science Principles Create Task requirements. This blog highlights purpose, implementation, and demonstrations of input/output, database interaction, and core algorithms used in the Study Log feature.

---

## **1. Purpose**

| Aspect                | Description                                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Group Program**     | Provides multiple academic tracking tools (e.g., grade logger, study logger) to help students monitor their academic progress in one place.    |
| **My Feature Focus**  | **Study Log** allows users to create, read, update, and delete study records. It helps students track daily study hours, subjects, and notes.   |

---

## **2. Input/Output Requests**

| I/O Mechanism                  | Description                                                                               |
|--------------------------------|-------------------------------------------------------------------------------------------|
| **Frontend Form**              | • **Subject**<br/>• **Hours Studied**<br/>• **Notes** (optional)                         |
| **API Endpoints**              | • **GET** `/api/studylognew`<br/>• **POST** `/api/studylognew`<br/>• **PUT** `/api/studylognew`<br/>• **DELETE** `/api/studylognew` |
| **Database**                   | SQLite (via SQLAlchemy). Stores logs in a `studylog` table.                                |
| **Output**                     | JSON data containing study log records.                                                   |

<img src="/Armaghan_2025/assets/Images/input1.png" width="600" height="450" />


### **2.1 Frontend Demo**

- **Add New Log**  
  Users fill out the form and submit:

  ```javascript
  fetch('http://127.0.0.1:8887/api/studylognew', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      user_id: 1,
      subject: subject,
      hours_studied: parseFloat(hours),
      notes: notes
    }),
    credentials: 'include',
  });
  ```

- **Display Logs**  
  On success, logs are displayed in the DOM using JavaScript.

  **On success, logs are displayed in the DOM using JavaScript.**

<br/>

<img src="/Armaghan_2025/assets/Images/form1.png" width="600" height="450" />

### **2.2 Postman Demo**

- **POST**:

  ```json
  POST /api/studylognew
  {
    "user_id": 1,
    "subject": "Math",
    "hours_studied": 2.0,
    "notes": "Algebra practice"
  }
  ```

- **Response**:

  ```json
  {
    "id": 101,
    "user_id": 1,
    "subject": "Math",
    "hours_studied": 2.0,
    "notes": "Algebra practice",
    "date": "2025-01-27 14:00:00"
  }
  ```

- **Error (missing field)**:

  ```json
  {
    "message": "Subject is required"
  }
  ```

<img src="/Armaghan_2025/assets/Images/post1.png" width="600" height="450" />

### **2.3 DB Backup/Restore**

- Executed via custom CLI commands:
  - `./scripts/db_backup.py`
  <img src="/Armaghan_2025/assets/Images/backup1.png" width="600" height="450" />

  - `./scripts/db_init.py`
    <img src="/Armaghan_2025/assets/Images/init1.png" width="600" height="450" />

  - `./scripts/db_restore.py`
      <img src="/Armaghan_2025/assets/Images/restore1.png" width="600" height="450" />

- Backs up all table rows (lists) as JSON and restores them when needed.

---

## **3. Data and List/Dictionaries**

| Data Handling          | Implementation                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------|
| **List (Rows)**        | `StudyLog.query.all()` returns a **list** of studylog objects.                                           |
| **Dictionary (Columns)** | `StudyLog.read()` outputs a **dictionary** of keys (`id`, `subject`, `hours`, `notes`, `date`).          |
| **JSON Formatting**    | Python `jsonify` returns dictionary data in JSON form to the client.                                      |

```python
def read(self):
    """
    Converts a StudyLog object into a dictionary format for easy API response handling.
    
    Returns:
        dict: A dictionary representation of the study log entry with relevant attributes.
    """
    return {
        "id": self.id,  # Unique identifier for the study log entry
        "user_id": self.user_id,  # The ID of the user who created the study log
        "subject": self.subject,  # The subject/topic the user studied
        "hours_studied": self.hours_studied,  # The number of hours the user studied
        "notes": self.notes,  # Any additional notes the user added for the study session
        "date": self.date.strftime('%Y-%m-%d %H:%M:%S')  # Formats the timestamp into a readable date-time format
    }
```

---

## **4. Algorithmic Code: API Methods**

Below is an example **POST** method, showing sequencing, selection, and iteration.

```python
@token_required()  # Ensures that only authenticated users can access this method
def post(self):
    """
    Handles the creation of a new study log entry.
    
    Steps:
    1. Retrieves JSON data from the request.
    2. Validates the input to ensure required fields are present.
    3. Creates a new StudyLog object and stores it in the database.
    4. Returns the newly created study log entry in JSON format.

    Returns:
        JSON response with the created study log entry or an error message.
    """

    # SEQUENCING: Steps to process the request
    data = request.get_json()  # Extract JSON data from the incoming request
    
    if not data:  # SELECTION: Checking if input data exists
        return {'message': 'No input data provided'}, 400  # Returns an error if data is missing

    # Extract required fields from the JSON request body
    user_id = data.get('user_id')  # The ID of the user creating the study log
    subject = data.get('subject')  # The subject the user studied
    hours_studied = data.get('hours_studied')  # Number of hours studied
    notes = data.get('notes')  # Any additional study notes

    # Additional validations to ensure required fields are provided
    if not user_id:
        return {'message': 'User ID is required'}, 400  # Returns an error if user ID is missing

    # CREATE: Construct a new StudyLog object with the provided data
    studylog = StudyLog(user_id, subject, hours_studied, notes)

    # Save the new study log entry to the database
    studylog.create()

    # Return the newly created study log entry in JSON format
    return jsonify(studylog.read())
```

- **Parameters**: Receives JSON body with `user_id`, `subject`, `hours_studied`, and `notes`.  
- **Return Type**: `jsonify` object containing the newly created study log (or error).

### **4.1 Calling the API (Frontend Fetch)**

```javascript
async function addStudyLog(subject, hours, notes) {
  const response = await fetch('http://127.0.0.1:8887/api/studylognew', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      user_id: 1,
      subject,
      hours_studied: parseFloat(hours),
      notes
    }),
    credentials: 'include',
  });

  if (response.ok) {
    const data = await response.json();
    console.log("New log added:", data);
  } else {
    const errMsg = await response.json();
    console.error("Error adding study log:", errMsg);
  }
}
```

- **Normal Condition**: 200 status + JSON data of the new log.  
- **Error Condition**: 4xx/5xx status + JSON error message.

---

## **5. Observations & Reflections**

1. **Collaboration**: Features integrated with other group modules (e.g., Grade Log) for a cohesive academic tracker.  
2. **Data Integrity**: Validation ensures each field is provided; errors returned as JSON.  
3. **Scalability**: RESTful design + SQLAlchemy facilitates robust, scalable data operations.  
4. **Future Enhancements**: Pagination for large logs, user-specific log filters.

---

## **6. Conclusion**

- **Achievement**: This feature meets the AP CSP Create Task guidelines by showing **purpose**, **input/output** methods, **data structures** (lists/dicts), and **algorithmic** logic.
- **Code Reusability**: Well-structured classes and methods (CRUD) make the Study Log extensible to other academic-tracking features.

> **Reference**: [AP Computer Science Principles Course and Exam Description](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-course-and-exam-description.pdf)

---

_This blog post demonstrates how the Study Log feature was designed, how it processes data, and how it aligns with the AP CSP requirements for creating and documenting software._