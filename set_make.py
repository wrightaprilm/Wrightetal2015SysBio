tree<-read.nexus("/home/april/projectfiles/plausibility/Zheng.tre")
vec_make <- function(){
v <- dexp(1, rate = 1, log = FALSE)
p <-rdirichlet(82, v)
for (value in p){
if (value >= 10){
p[value] <- rgamma(1, .35, .1)
return(p)
}
}
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
while (i <= 219){
het_trx[,i] <- cbind(do_sims(p))
i <- i + 1
}
return(het_trx)
}
write_out <- function(i) {
txt<-"/home/april/projectfiles/plausibility/simulations/Abella/exp/"
f3<-paste(txt,i, ".csv")
write.table(col_chars(), row.names=T,col.names =F, file = f3, sep=",")
}

i <- 0
while (i< 100){
write_out(i)
i <- i+1
}
