
:one: How would you predict revenue tomorrow given daily revenue from the past few
years?

To predict revenue tomorrow based on daily revenue from the past few years,
I would use time series forecasting techniques such as ARIMA.

I personally got acquainted with this model on my previous project,
the essence of which was to issue forecasts for the stocks price.

:two: Let’s say we play a game where I keep flipping a coin until I get heads. If the first
time I get heads is on the n-th coin, then I pay you 2n-1 dollars. How much would you
pay me to play this game?

To give an answer to this question,
it is necessary to calculate the probability of the head falling N number of times
and compare the trend of the probabilities of favorable events with the trend
of the growth of winning earnings in the event of a favorable event.

Well, let's do an experiment (since it's a fair coin):
In this game, the probability of getting heads on the first coin flip is 1/2 .
If this happens, I would win 2*1 - 1 = 1 dollar.

The probability of getting heads on the second coin flip is (1/2) * (1/2) = 1/4.
In this case, I would win 2*2 - 1 = 3 dollar.

Similarly, for the third coin flip, the probability is (1/2) * (1/2) * (1/2) = 1/8,
and I would win 2*3 - 1 = 5 dollars.

In general, the probability of getting heads on the n-th flip is (1/2)*n, and you would pay me 2*n-1 dollars.

To calculate the expected value, we multiply the probability of each outcome by its corresponding payoff and sum them up.
Therefore, the expected value is the sum of (1/2)*n * (2*n-1) for all possible values of n.
This sum converges to 1.

Well, in the conclusion we get that with the highest probability I will get no more than $1!

:three: In an A/B test, how can you check if assignment to the various buckets was truly
random?

I would check, if assignment to the various buckets in an A/B test was truly random 
by comparing the distribution of key variables between the buckets. 
Calculate summary statistics or perform visualizations to assess if 
the proportions or means are similar across the buckets. 
This provides a quick assessment of randomness, 
but further statistical analysis may be needed for more conclusive results.