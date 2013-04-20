library(XML)
library(wordcloud)

setwd('/var/www/twitter/mit')

d <- read.csv('frequencies.txt')
names(d) <- c('word', 'freq')
d <- d[complete.cases(d),]

png("mit-wordcloud.png", bg="transparent", width=700, height=500)
pal2 <- brewer.pal(8,"Dark2")
wordcloud(d$word,d$freq, scale=c(8,.2),min.freq=30,max.words=Inf, random.order=FALSE, rot.per=.15, colors=pal2)
dev.off()


