import os
import pandas
import seaborn
import matplotlib.pyplot as plt


# Reading the data
pandas.set_option('display.max_columns', None)
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'support_data.csv')
data = pandas.read_csv(file_path)


print("--- Validation of Time Intervals ---")
interval = data['interval'].unique()
print(interval)

print("\n--- Distribution of Records by Periods ---")
interval_count = data['interval'].value_counts()
print(interval_count)

print("\n--- Unique User Segments ---")
unique_names = data['segment'].unique()
print(unique_names)

print("\n--- Number of Clients in Each Segment ---")
segment_counts = data.groupby('segment')['customer_id'].count()
print(segment_counts)

# 2. Testing the hypothesis of segmentation by the number of robocats
robocats_counts = data.groupby('segment')['robocats'].sum()
client_counts = data.groupby('segment')['segment'].count()
segment_means = robocats_counts / client_counts

print("\n--- Average Number of Robocats by Segment ---")
print(segment_means)

names = ['Segment 0', 'Segment 1', 'Segment 2'] 
seaborn.barplot(x=names, y=segment_means)#, annot=True)

plt.title('Average Number of Robocats by Segment') 
plt.xlabel('names')
plt.ylabel('segment_means')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()

# 3. Analysis of support metrics: Before and After the introduction of robots
segments_new = [ 'Potential Customers', 'Regular Customers', 'VIP Customers' ] 
intervals = ['Before the Introduction of Robots', 'After the Introduction of Robots']

# А) Heatmap of average ratings (Satisfaction)
scores_sum = data.groupby(['segment', 'interval'])['score'].sum() 
scores_count = data.groupby(['segment', 'interval'])['score'].count()
mean_scores = scores_sum / scores_count 

seaborn.heatmap(mean_scores.unstack('interval'),
                annot=True,
                cmap='RdYlGn')

plt.title('Satisfaction') 
plt.xlabel('Intervals')
plt.ylabel('Segments')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()

# B) Heatmap of consultation duration
duration_sum = data.groupby(['segment', 'interval'])['duration'].sum() 
duration_count = data.groupby(['segment', 'interval'])['duration'].count()
mean_duration = duration_sum / duration_count 

seaborn.heatmap(mean_duration.unstack('interval'), 
                    annot=True, 
                    cmap='RdYlGn')

plt.gcf().set_size_inches(8, 6)
plt.gca().set_xticklabels(plt.gca().get_xticklabels(), rotation=0)
plt.gca().set_yticklabels(plt.gca().get_yticklabels(), rotation=0)

plt.title('Duration of consultation') 
plt.xlabel('Intervals')
plt.ylabel('Segments')
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()


# C) Heatmap of promo code distribution
promo_sum = data.groupby(['segment', 'interval'])['promo'].sum() 
promo_count = data.groupby(['segment', 'interval'])['promo'].count() 
mean_promo = promo_sum / promo_count 

 
seaborn.heatmap(mean_duration.unstack('interval'), 
                    annot=True, 
                    cmap='RdYlGn')

plt.gcf().set_size_inches(8, 6) 
plt.gca().set_xticklabels(plt.gca().get_xticklabels(), rotation=0)
plt.gca().set_yticklabels(plt.gca().get_yticklabels(), rotation=0)

plt.title('Probability of promo code') 
plt.xlabel('Intervals')
plt.ylabel('Segments')
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()

# 4. Relationship between ratings and promo codes (Robot training)
sum_promo = data.groupby(['interval', 'score'])['promo'].sum() 
count_promo = data.groupby(['interval', 'score'])['promo'].count() 
promo_chance = sum_promo / count_promo

scores = sorted(data['score'].unique()) 

seaborn.heatmap(
    promo_chance.unstack('interval'),  
    annot=True, 
    cmap='RdYlGn'
) 

plt.title('Relationship between ratings and promo codes') 
plt.xlabel('Intervals')
plt.ylabel('Scores')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()