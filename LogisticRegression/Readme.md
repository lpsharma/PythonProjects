Logistics regression is a type of classification algo because it attempts to classify observations from a dataset into distinct categories

Example 
1. Customer will default on a loan (Response variable "Default" or "No default").  The logic can be build on variable like "credit score" and bank balance

2. Basket ball player will get drafted into NBA(response "Drafter" or "Not Drafter").  you can use average rebounds per game and average points per game to predict.


p(x) = e(beta0) + (beta1X) + ...... (betan*Betan)/(1 + e(beta0) + (beta1X) + ...... (betan*Betan))


Probability more than .5 is 1 or else it is 0.  

Example 
P(Drafted) = e-2.8690 + 0.0698*(rebs) + 0.1694*(points) / (1+e-2.8690 + 0.0698*(rebs) + 0.1694*(points))


Assumption 

1. response variable is binary and it is assumed that response variable can take on two possibility outcome (0 or 1)

2. Observations are independent of each other.

3. None of the predictor variable are highly correlated with each other 

4. No extreme outliers 

5. sample size is sufficiently large.
