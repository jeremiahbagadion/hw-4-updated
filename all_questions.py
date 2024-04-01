# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain-string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None

    # explain-string: explanation in english prose
    answers["(a) example"] = None
    answers["(b) example"] = None
    answers["(c) example"] = None

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.3

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "This value of K is more robust than K = 1, as it takes into account a larger neighborhood. It can help reduce the impact of outliers and provide more stable classifications, especially for the blue crosses that are more dispersed."
    answers["(b) explain"] = "It allows for a moderate level of smoothing while still preserving the separation between clusters, leading to better generalization performance."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "we need to find the probability of A=1 given that the class is '+'. This is done by counting the number of instances where A=1 and the class is '+', and dividing it by the total number of instances with class '+'. From the data, there are 5 instances with class '+' (instances 2, 5, 6, 9, and 10). Out of these, there are 3 instances where A=1 (instances 2, 5, and 10). Therefore, P(A=1|+) = 3/5 = 0.6"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.096
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "To predict the class label for the test sample R (A=1, B=1, C=1) using the naïve Bayes approach, we calculate the posterior probabilities P(+|R) and P(-|R) and choose the class with the higher probability. Since P(+|R) > P(-|R), the predicted class label for the test sample R is '+'."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "We found that P(A=1, B=1|Class=+) = 0.2 and P(A=1|Class=+) * P(B=1|Class=+) = 0.6 * 0.4 = 0.24. Since these values are not equal, we can conclude that A and B are not conditionally independent given the class +"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
