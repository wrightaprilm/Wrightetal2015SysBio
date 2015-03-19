
library(ape)
library(phytools)
library(diversitree)
thresh_vec <- vector()
asym_states <- vector()
sym_states <- vector()

tree <-read.tree('SimulationTree.tre')
i <- 0
while (i < 100){
Xl<-sim.corrs(tree,vcv=matrix(c(1,0.8*sqrt(2),0.8*sqrt(2),2), 2,2))
X<-Xl
X[Xl[,1]<0,1]<-0
X[Xl[,1]>0,1]<-1
thresh_vec <- append(thresh_vec, X)
}

while (i <- 100){
x1 <- runif(1, 0.05, .95)
x2 <- runif(1, 0.05, .95)
states <- sim.character(phy, c(x1, x2), x0=0, model="mk2")
asym_states <- append(asym_states, states)
}

while (i <- 100){
x1 <- runif(1, 0.05, .95)
states <- sim.character(phy, c(x1, x1), x0=0, model="mk")
sym_states <- append(sym_states, states)
}

big_mat <- cbind(thresh_vec, asym_states, sym_states)
write.nexus.data(bigmat, 'test', format = "protein", datablock = TRUE,
                 interleaved = TRUE, charsperline = NULL,
                 gap = NULL, missing = NULL)
