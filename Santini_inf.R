library(gtools)
library(geiger)

tree <- read.nexus('../../8taxa.tre')

do_sims <- function(){
char <- list()
p <- rgamma(1, .5, .1)
q <-list(rbind(c(-p,p), c(p, -p)))
char <- c(p,sim.char(tree, q, model="discrete"))
return(char)
}
col_chars <- function() {
i <- 1
het_trx <- data.frame(do_sims())
while (i <= 219){
het_trx[,i] <- cbind(do_sims())
i <- i + 1
}
return(het_trx)
}
write_out <- function(i) {
txt<-"./d/"
f3<-paste(txt,i, ".csv", sep="")
trx <- col_chars()
names(trx) <- trx[1,]
trx <- trx[-1,]
trx <- trx[,order(names(trx))]
write.table(trx, row.names=T,col.names =T, file = f3, sep=",")
}
i <- 0
while (i< 100){
write_out(i)
i <- i+1
}
