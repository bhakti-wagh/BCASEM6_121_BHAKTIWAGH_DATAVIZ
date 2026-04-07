import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History', 'Geography']
marks = [85, 78, 92, 65, 70]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(marks, labels=subjects, autopct='%1.1f%%',
            colors=['gold','lightblue','lightgreen','pink','orange'])
axes[0].set_title('Marks Distribution - Pie Chart')

axes[1].bar(subjects, marks, color=['gold','lightblue','lightgreen','pink','orange'])
axes[1].set_title('Subject Marks - Bar Chart')
axes[1].set_xlabel('Subject')
axes[1].set_ylabel('Marks')

plt.tight_layout()
plt.show() 