library(MASS)
library(ISLR)

data(Carseats)
attach(Carseats)


regplot = function(x,y,...){
  fit = lm(y~x)
  plot(x,y,...)
  abline(fit, col="red")
}

regplot(Price, Sales, xlab = "Price", ylab = "Sales", col = "blue", pch = 20)


