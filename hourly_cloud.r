library(XML)
library(wordcloud)

setwd('/var/www/twitter/mit')

for (i in 1:7) {
    infile <- paste('hourly_frequencies', i, '.txt', sep="")
    print(infile)
    d <- read.csv(infile)
    names(d) <- c('word', 'freq')
    d <- d[complete.cases(d),]

    filename <- paste("mit-wordcloud_h", i, ".png", sep="")
    png(filename, bg="transparent", width=700, height=500)
    pal2 <- brewer.pal(8,"Dark2")
    wordcloud(d$word,d$freq, scale=c(8,.2),min.freq=5,max.words=Inf, random.order=FALSE, rot.per=.15, colors=pal2)
    dev.off()


}

