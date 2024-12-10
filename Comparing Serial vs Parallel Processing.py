#!/usr/bin/env python
# coding: utf-8

# # Comparing Serial vs Parallel Processing:

# In[2]:


import pandas as pd
import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

data = {
    "student_id": [1, 2, 3, 4, 5],
    "status": [True, False, True, True, False]
}

students_df = pd.DataFrame(data)

student_payment_dates = {
    1: "2024-01-01",
    2: "2024-01-02",
    3: "2024-01-03",
    4: "2024-01-04",
    5: "2024-01-05"
}

def process_student(student_id, status):
    if status:
        return student_payment_dates.get(student_id, None)
    return None

start_time = time.time()
matched_dates_serial = [process_student(row["student_id"], row["status"]) for _, row in students_df.iterrows()]
matched_dates_serial = [date for date in matched_dates_serial if date is not None]
serial_time = time.time() - start_time

start_time = time.time()
with ThreadPoolExecutor() as executor:
    matched_dates_parallel = list(executor.map(process_student, students_df["student_id"], students_df["status"]))
matched_dates_parallel = [date for date in matched_dates_parallel if date is not None]
parallel_time = time.time() - start_time

print(f"Serial Processing Time: {serial_time:.5f} seconds")
print(f"Parallel Processing Time: {parallel_time:.5f} seconds")

times = [serial_time * 1000, parallel_time * 1000]  # Convert to milliseconds

labels = ['Serial Processing', 'Parallel Processing']

plt.figure(figsize=(8, 5))
plt.bar(labels, times, color=['blue', 'orange'])

plt.title('Comparison of Serial vs Parallel Processing')
plt.ylabel('Time (milliseconds)')
plt.xlabel('Processing Method')

plt.tight_layout() 
plt.show()

