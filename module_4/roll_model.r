
# Load packages
library(reshape)
library(zoo)
library(ggplot2)

# Cost of dealers
c <- 1

# Simulated time index
time <- 1:100

# simulated spot price
epsilon <- rnorm(time)
prices <- cumsum(epsilon)

# timeseries teorethical values
m_t <- zoo(prices)

# add a transactions cost so we have bid and ask
b_t <- m_t - c
a_t <- m_t + c

# random trade ocurred 1 (a buy order) or -1 (a sell order)
q_t <- sign(rnorm(time))
# price movement affected by the random trade occurred
p_t <- m_t + (c * q_t)

# create a timeseries dataframe
x <- merge(b_t, a_t)
colnames(x) <- c("bid", "ask")

x.df <- data.frame(dates=index(x), coredata(x))
x.df <- melt(x.df, id="dates", variable="val")
ggplot(na.omit(x.df), aes(x=dates, y=value, group=val, colour=val)) + geom_line()
