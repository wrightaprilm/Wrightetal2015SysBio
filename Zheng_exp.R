library(gtools)
library(geiger)

tree <- read.tree('Zheng.tre')


vec_make <- function(){
p <-rbeta(50, .2,.2)
return(p)
}
do_sims <- function(v){
for (value in v){
q<-list(rbind(c(-value, value), c(value, -value)))
s<-sim.char(tree, q, model="discrete")
return(s)
}
}
col_chars <- function() {
i <- 1
v <- vec_make()
het_trx <- data.frame(do_sims(v))
while (i <= 50){
het_trx[,i] <- cbind(do_sims(v))
i <- i + 1
}
return(het_trx)
}
write_out <- function(i) {
txt<-"./e/"
f3<-paste(txt,i,".csv", sep="")
write.table(col_chars(), row.names=T,col.names =F, file = f3, sep=",")
}

i <- 0
while (i< 100){
write_out(i)
i <- i+1
}
