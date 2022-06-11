# coinSim

Was inspired by this youtube video https://www.youtube.com/watch?v=rwvIGNXY21Y&ab_channel=singingbanana 

and tried to simulate his experience. 

Either I have failed to find a logical error - or it seems that the number of attempts tends to around 2000. Rather than the predicted ((1/2)^10 = 1/1024))


Edit:
Okay there isn't a problem with the code - https://courses.cit.cornell.edu/info2950_2012sp/mh.pdf

I just happen to coincdently show what this paper says. Isn't that funny?


A slight explanation from a friend:
```
  I think he was modelling the coin flips using a geometric distribution
  X~Geo(p) if p is the probability of getting 10 heads (p = 0.5^10) then Exp[X] = 2^10 = 1024
  The problem with this is that the success trial can overlap with other trials. 

  A better way to model it would be to use a Markov process since it takes into account the previous 9 flips. 
