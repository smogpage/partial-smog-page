#!/bin/bash

#Input to the script is the [ pairs ] section consisting of LJ pairs.

#this is only convert from c6 and c12 to Gauss with type 5
awk '{
mu = ($5*2 / $4)^(1/6);
A = $5 / mu^12;
sigma =  mu * 0.2 / ( 2*log(2) )^(1/2)
print   $1,   $2,   5,   A,   mu,   sigma;
}' $1

exit
#this is only convert from c6 and c12 to Gauss with type 6
awk '{
mu = ($5*2 / $4)^(1/6);
A = $5 / mu^12;
sigma =  mu * 0.2 / ( 2*log(2) )^(1/2)
print   $1,   $2,   6,   A,   mu,   sigma,   0.17^12;
}' $1

exit
