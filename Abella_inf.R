library(gtools)
library(geiger)

tree <- read.tree('Abella.tre')

vec_make <- function(){
p <- rgamma(82, .5, .1)
for (value in p){
if (value >= 10){
p[value] <- rgamma(1, .35, .1)
}
}
return(p)
}
do_sims <- function(p){
for (value in p){
q<-list(rbind(c(-value, value), c(value, -value)))
s<-sim.char(tree, q, model="discrete")
return(s)
}
}
col_chars <- function() {
i <- 1
het_trx <- data.frame(do_sims(p))
while (i <= 82){
het_trx[,i] <- cbind(do_sims(p))
i <- i + 1
}
return(het_trx)
}
write_out <- function(i) {
txt<-"./Abella/inf/"
f3<-paste(txt,i, ".csv")
write.table(col_chars(), row.names=T,col.names =F, file = f3, sep=",")
}
