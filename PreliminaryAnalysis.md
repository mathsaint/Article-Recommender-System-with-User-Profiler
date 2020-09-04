# Expository Analysis and Research

A background study and research was done as part of this project to understand various aspects that need to be considered during the modeling of the recommender system.

## **News Source Analysis**

### Selection
A reliable news source was chosen after considering and various site metrics for different news agency websites. This was a necessary step to create our source corpus. The scoring method used was:  
***Score = Normalized Visits * Average Visit Duration * Retention***  

The following images show the news agencies analyzed and their respective scores:
![scoring1](https://user-images.githubusercontent.com/25324641/92238181-4bc78380-eed6-11ea-9870-b57c33ed2f87.png)
![scoring2](https://user-images.githubusercontent.com/25324641/92238188-4cf8b080-eed6-11ea-90d5-ef00aacef9ed.png)

*Note: The attributes and their values were recorded in May, 2020.*

According to our scoring metric, **NDTV** was the best source for our news corpus.

### Cleaning
The corpus was generated using the **newspaper** package in Python. The resulting corpus was saved as a .csv file, and required extensive cleaning in the pre-processing stage.

## **News Consumption Analysis**

### Journalists' Understanding
We interacted with journalists from NDTV to understand how they make their news more accessible and exhaustive. We also got to understand the broad topics and how each news article can be classified into these categories.

### Targeted Questionnare among peers
To understand the news reading behaviour of our peers, we circulated a Google form. Over 550 working professionals/students belonging to the age group 21 - 40 had taken the survey. The key points from that study are listed below:

- Preference of topics to be read in news
![topics](https://user-images.githubusercontent.com/25324641/92238198-508c3780-eed6-11ea-8f65-a6988c0c301e.png)

- Total reading time spent on newsreading daily   
![total-time](https://user-images.githubusercontent.com/25324641/92243728-88e44380-eedf-11ea-9b9f-d294f1506345.png)

- Preferred article length for reading    
![article-length](https://user-images.githubusercontent.com/25324641/92243716-85e95300-eedf-11ea-9534-7d356144f269.png)

### Literature Review
- We went through various surveys and studies conducted by leading news agencies in the world to make their recommender systems better
- Literature survey of NLP professionals was conducted to search for the best machine learning algorithms available to model our system

The topic based recommendation was emphasized throughout various studies. Therefore, we decided to use **Latent Dirichlet Allocation (LDA)** as our model.


## Devising a Recommender System

The following flowchart explains our approach:
![flowchart](https://user-images.githubusercontent.com/25324641/92238177-49fdc000-eed6-11ea-8eff-c87fd87414a9.png)

A user profile can be used to enhance the blind recommendation step. As we did not have access to user profile data, we decided to generate our own user profiles.

## Modeling the User Profiler - A Markov Model
A user profile is a repository of user behaviour while using the system, and it might help us in better understanding patterns of reading articles and improving our recommender system.

We generated 1000 user profiles using a markov model.

### Assumptions:
- User reads the whole article completely and only once
- Reading speeds are comparable, normally distributed with mean 265 words per minute and the standard deviation as 10
- User selects an article after every recommendation

### Transition Matrix:
- Cosine Similarities saved as a matrix
- Values normalized over rows to sum up to 1, with values from articles to themselves changed to 0

### Parameters and proposed distributions:
- User ID: Unique for every new user, starts at 1 and increases sequentially, reading speed fixed for a user ID, user is classified into total time spent category based on the Google form data, with each category having appropriate normal distributions
- Session ID: Identification of recommendation sessions, starts at 1 for every new user
- Article Rank: The rank of the article as seen in the recommendations, generated randomly from uniform discrete distribution between 1 and 10
- Article ID: The ID of the chosen article as seen in the corpus, first article is randomly chosen (from the probability distribution obtained from google form data), then proceed based on transition matrix
- Time Spent = (number of words/reading speed) (calculated in seconds)


