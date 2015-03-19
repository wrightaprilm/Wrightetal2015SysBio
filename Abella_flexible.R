library(gtools)
library(geiger)

tree <- read.tree('Abella.tre')


vec_make <- function(){
p <-rdirichlet(82, 2)
for (value in p){
if (value >= 10){
p[value] <- rdirichlet(82, 2)

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
txt<-"./Abella/2/"
f3<-paste(txt,i, ".csv", sep="")
write.table(col_chars(), row.names=T,col.names =F, file = f3, sep=",")
}
i <- 0
p<-vec_make()
while (i< 100){
write_out(i)
i <- i+1
}
