#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <math.h> 

static const int64_t COIN = 100000000;

int64_t static GetBlockBaseValue(int nBits, int nHeight)
{

 int64_t nSubsidy = 1.044921875 * COIN;

    if (nHeight == 1)
    {
       nSubsidy = 1160950 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 50)
    {
       nSubsidy = 1 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 10000)
    {
       nSubsidy = 535 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 30000)
    {
       nSubsidy = 267.5 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 70000)
    {
       nSubsidy = 133.75 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 150000)
    {
       nSubsidy = 66.875 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 310000)
    {
       nSubsidy = 33.4375 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 630000)
    {
       nSubsidy = 16.71875 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 1270000)
    {
       nSubsidy = 8.359375 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 2550000)
    {
       nSubsidy = 4.1796875 * COIN;
       return nSubsidy;
    }

    else if (nHeight <= 5110000)
    {
       nSubsidy = 2.08984375 * COIN;
       return nSubsidy;
    }
    
    else if (nHeight <= 10230000)
    {
       nSubsidy = 1.044921875 * COIN;
       return nSubsidy;
    }

//    nSubsidy >>= (nHeight / 50000); // Old Halving

    return nSubsidy;

}


#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;
 
BOOST_PYTHON_MODULE(juggalocoin_subsidy)
{
    def("GetBlockBaseValue", GetBlockBaseValue);
}

