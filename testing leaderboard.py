import csv
import pandas as pd
import matplotlib.pyplot as plt

data = [['Mo', 6, 'Fruits'], ['Bob', 7, 'Occupations']]
        
filepath = 'leaderboard.csv'
        
with open(filepath, 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Score', 'Category'])
            
    for row in data:
        writer.writerow(row)

names = []
scores = []
categories = []
        
with open("leaderboard.csv", mode='r') as scores_file:
    score_reader = csv.reader(scores_file)
    for row in score_reader:
        names.append(row[0])
        scores.append(row[1])
        categories.append(row[2])
                
ax = plt.subplots()
ax.bar(names, scores)
ax.set_xlabel('Names')
ax.set_ylabel('Scores')
ax.set_title('Scores by Category')
ax.set_xticklabels(categories)
plt.show()