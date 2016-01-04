import sys
from math import log,exp,lgamma,pow
import scipy.stats, scipy.optimize
#This script calculates the likelihood of a character on a four taxon tree with various values of the symmetric Dirichlet (hyper)prior. It was written by Paul Lewis (minor edits, such as taking in user input by April Wright)
#It is called like so:
# python test_symDir.py alpha_value beta_value

def Pr(from_state, to_state, pi0, exp_minus_mu_t):
    # compute transition probability from state from_state to state to_state
    # with exp_minus_mu_t = exp(-mu*t), where mu*t is computed from the branch
    # length v and relative frequencies of state 0 (pi0) and state 1 (pi1) by
    # solving the following equation for mu*t:
    #     v = 2*pi0*pi1*mu*t
    pi1 = 1.0 - pi0
    if from_state == to_state:
        if from_state == 0:
            return pi0 + pi1*exp_minus_mu_t
        else:
            return pi1 + pi0*exp_minus_mu_t
    else:
        if from_state == 0:
            return pi1 - pi1*exp_minus_mu_t
        else:
            return pi0 - pi0*exp_minus_mu_t

def logLikelihood(pi0, v, state1, state2, state3, state4):
    # computes log-likelihood assuming tree (1,2,(3,4)) with all 5 branch lengths equal to v
    # and assuming relative equilibrium frequency of state 0 is pi0
    pi1 = 1.0 - pi0
    mu_t = v/(2.0*pi0*pi1)
    eterm = exp(-mu_t)
    condlike0 = Pr(0, state3, pi0, eterm) * Pr(0, state4, pi0, eterm)
    condlike1 = Pr(1, state3, pi0, eterm) * Pr(1, state4, pi0, eterm)
    condlikesum0 = Pr(0, 0, pi0, eterm) * condlike0 + Pr(0, 1, pi0, eterm) * condlike1
    condlikesum1 = Pr(1, 0, pi0, eterm) * condlike0 + Pr(1, 1, pi0, eterm) * condlike1
    root0 = Pr(0, state1, pi0, eterm) * Pr(0, state2, pi0, eterm) * condlikesum0
    root1 = Pr(1, state1, pi0, eterm) * Pr(1, state2, pi0, eterm) * condlikesum1
    loglike = log(pi0*root0 + pi1*root1)
    return loglike

if __name__ == '__main__':
    ncateg = 5      # number of beta categories used for discrete beta frequency distribution

    # if prset Symdirihyperpr = Fixed(x), then alpha = beta = x
    alpha  = float(sys.argv[1])
    beta   = float(sys.argv[2])

    # starting tree = (1:0.1,2:0.1,(3:0.1,4:0.1):0.1)
    v      = 0.1    # all branch lengths equal v

    # states for one character are hard-coded in this example
    state1 = 0      # state for tip 1
    state2 = 0      # state for tip 2
    state3 = 1      # state for tip 3
    state4 = 1      # state for tip 4

    print 'pi0 ~ Beta(%.5f, %.5f) divided into %d equal-volume categories' % (alpha, beta, ncateg)

    likelihood = 0.0
    for i in range(ncateg):
        # Find point on x-axis (pi0) that represents the median of the (i+1)th category
        category_median = (0.5+i)/ncateg
        pi0 = scipy.stats.beta.ppf(category_median, alpha, beta)

        loglike = logLikelihood(pi0, v, state1, state2, state3, state4)
        likelihood += exp(loglike)

        print '  categ %d: pi0 = %.5f, pi1 = %.5f, logLike = %.5f' % (i+1, pi0, 1.0-pi0, loglike)

    # the likelihood for each category (likelihood) is multiplied by the
    # probability of being in that category (1/ncateg)
    loglikelihood = log(likelihood) - log(ncateg)

    print 'log-likelihood =',loglikelihood
