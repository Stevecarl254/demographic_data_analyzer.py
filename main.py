```python
import pandas as pd

def analyze_data():
    # Load dataset
    df = pd.read_csv('adult.csv')

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'].value_counts(normalize=True)['Bachelors']) * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_earning_adv_edu = round((advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_earning_non_adv_edu = round((non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0] / non_advanced_education.shape[0]) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    minimum_hours_per_week = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_people = df[df['hours-per-week'] == minimum_hours_per_week]
    percentage_high_earning_min_hours = round((min_hours_people[min_hours_people['salary'] == '>50K'].shape[0] / min_hours_people.shape[0]) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_total = df.groupby('native-country').size()
    percentage_high_earning_by_country = (country_salary / country_total * 100).fillna(0)
    highest_earning_country = percentage_high_earning_by_country.idxmax()
    highest_percentage = round(percentage_high_earning_by_country.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    popular_occupation_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()

    # Print results
    print("Race count:")
    print(race_count)
    print("\nAverage age of men:", average_age_men)
    print("Percentage of people with a Bachelor's degree:", percentage_bachelors)
    print("Percentage of people with advanced education earning more than 50K:", percentage_high_earning_adv_edu)
    print("Percentage of people without advanced education earning more than 50K:", percentage_high_earning_non_adv_edu)
    print("Minimum hours worked per week:", minimum_hours_per_week)
    print("Percentage of those working minimum hours earning more than 50K:", percentage_high_earning_min_hours)
    print("Country with highest percentage earning >50K:", highest_earning_country, "-", highest_percentage)
    print("Most popular occupation for those earning >50K in India:", popular_occupation_india)

if __name__ == "__main__":
    analyze_data()
```

