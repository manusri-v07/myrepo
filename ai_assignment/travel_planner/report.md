# AI Travel Planner Report

## 1. Introduction

This project implements an AI-based Travel Planner that provides personalized travel recommendations using an existing knowledge base. The system considers user preferences such as budget, interest, and food choices to suggest suitable destinations.

---

## 2. Objective

The objective of this project is to:

* Design a travel recommendation system
* Use a predefined knowledge base
* Provide personalized and ranked suggestions

---

## 3. Knowledge Base

The system uses a structured dataset (dictionary) containing information about different tourist destinations.

### Example:

```python
places = {
    "Goa": {"type": "beach", "budget": 5000, "food": ["seafood"]},
    "Manali": {"type": "mountain", "budget": 7000, "food": ["north indian"]}
}
```

### Attributes:

* Type (beach, mountain, historical)
* Budget
* Food options

---

## 4. System Design

### Input:

* Budget
* Interest (type of place)
* Food preference

### Processing:

* Each place is evaluated using a scoring function
* Scores are assigned based on matching conditions

### Output:

* Ranked list of recommended places
* Detailed information for each place

---

## 5. AI Logic (Scoring Function)

```python
def calculate_score(details, budget, interest, food_pref):
    score = 0
```

### Criteria:

* Budget match → +3
* Interest match → +4
* Food match → +2

This scoring mechanism allows the system to make intelligent decisions.

---

## 6. Features

* Personalized recommendations
* Multiple preference handling
* Ranking of results
* Cost estimation
* Food suggestions

---

## 7. Example Output

Input:

* Budget: 6000
* Interest: beach
* Food: seafood

Output:

* Goa (Score: 9)
* Kerala (Score: 9)

---

## 8. Advantages

* Simple and efficient
* Easy to extend
* Uses knowledge-based reasoning

---

## 9. Limitations

* Limited dataset
* Static knowledge base
* No real-time data

---

## 10. Conclusion

The AI Travel Planner successfully provides personalized recommendations using a knowledge-based approach. The use of scoring and ranking improves decision-making and enhances user experience.

---

## 11. GitHub Repository

The full source code is available in the submitted GitHub repository.

