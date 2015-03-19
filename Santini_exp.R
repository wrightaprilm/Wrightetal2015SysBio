library(gtools)
library(geiger)

tree <- read.nexus('../8taxa.tre')
vec_make <- function(){
p <- vector()
v <- dexp(1, rate = 1, log = FALSE)
p <- rdirichlet(219, c(v,v))

print(p)
for (value in p){
if (value >= 10){
p[value] <- rbeta(1, .35, .1)

}
}
return(p)
}
do_sims <- function(p){
value <- 1
while (value < 219 ){
print(value,1)
q<-list(rbind(c(-p[value,1], p[value,2]), c(p[value,1], -p[value,2])))
print(q)
s<-sim.char(tree, q, model="discrete")
value <- value + 1
return(s)
}
}
col_chars <- function() {
i <- 1
het_trx <- data.frame(do_sims(p))
while (i <= 219){
het_trx[,i] <- cbind(do_sims(p))
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
p<-vec_make()
while (i< 100){
write_out(i)
i <- i+1
}
