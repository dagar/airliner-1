/************************************************************************
** Includes
*************************************************************************/

#include "ads1115.h"


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                                 */
/* Default constructor.                                            */
/*                                                                 */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
ADS1115::ADS1115()
{
    /* Set default values as initial values. */
    mConfig.mux = ADS1115_MUX_BITS_P0_N1;
    mConfig.pga = ADS1115_PGA_BITS_2P048;
    mConfig.mode = ADS1115_MODE_BITS_SINGLE;
    mConfig.rate = ADS1115_DATA_RATE_BITS_128;
    mConfig.compMode = ADS1115_COMP_MODE_BITS_HYSTERESIS;
    mConfig.compPolarity = ADS1115_COMP_POL_ACTIVE_LOW;
    mConfig.compLatching = ADS1115_COMP_LAT_BITS_NON_LATCHING;
    mConfig.compQueueMode = ADS1115_COMP_QUE_BITS_DISABLE;
    mConfig.mvMultiplier = ADS1115_MV_MULT_2P048;
}

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                                 */
/* Destructor constructor.                                         */
/*                                                                 */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
ADS1115::~ADS1115()
{

}


/* Configuration setters. */
boolean ADS1115::setMux(ADS1115_Bits_Mux_t mux)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bits. */
    value = setBits16(ADS1115_CONFIG_BITS_MUX0, ADS1115_BIT_LENGTH_MUX, value, mux);

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.mux = mux;

end_of_function:
    return returnBool;
}


boolean ADS1115::setGain(ADS1115_Bits_Pga_t pga)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bits. */
    value = setBits16(ADS1115_CONFIG_BITS_PGA0, ADS1115_BIT_LENGTH_PGA, value, pga);

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.pga = pga;

    switch (pga) 
    {
        case ADS1115_PGA_BITS_6P144:
        {
            mConfig.mvMultiplier = ADS1115_MV_MULT_6P144;
            break;
        }
        case ADS1115_PGA_BITS_4P096:
        {
            mConfig.mvMultiplier = ADS1115_MV_MULT_4P096;
            break;
        }
        case ADS1115_PGA_BITS_2P048:
        {
            mConfig.mvMultiplier = ADS1115_MV_MULT_2P048;
            break;
        }
        case ADS1115_PGA_BITS_1P024:
        {
            mConfig.mvMultiplier = ADS1115_MV_MULT_1P024;
            break;
        }
        case ADS1115_PGA_BITS_0P512:
        {
            mConfig.mvMultiplier = ADS1115_MV_MULT_0P512;
            break;
        }
        case ADS1115_PGA_BITS_0P256:
            /* Fall through. */
        case ADS1115_PGA_BITS_0P256B:
            /* Fall through. */
        case ADS1115_PGA_BITS_0P256C:
        {
            mConfig.mvMultiplier = ADS1115_MV_MULT_0P256;
            break;
        }
    }

end_of_function:
    return returnBool;
}


boolean ADS1115::setMode(ADS1115_Bits_Mode_t mode)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bit. */
    if(mode)
    {
        value |= 1 << ADS1115_CONFIG_BITS_MODE;
    }
    else
    {
        value &= ~(1 << ADS1115_CONFIG_BITS_MODE);
    }

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.mode = mode;

end_of_function:
    return returnBool;
}


boolean ADS1115::setRate(ADS1115_Bits_Data_Rate_t rate)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bits. */
    value = setBits16(ADS1115_CONFIG_BITS_COMP_DR0, ADS1115_BIT_LENGTH_DR, value, rate);

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.rate = rate;

end_of_function:
    return returnBool;
}


boolean ADS1115::setComparatorMode(ADS1115_Bits_Comp_Mode_t compMode)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bit. */
    if(compMode)
    {
        value |= 1 << ADS1115_CONFIG_BITS_COMP_MODE;
    }
    else
    {
        value &= ~(1 << ADS1115_CONFIG_BITS_COMP_MODE);
    }

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.compMode = compMode;

end_of_function:
    return returnBool;
}


boolean ADS1115::setComparatorPolarity(ADS1115_Bits_Comp_Polarity_t compPolarity)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bit. */
    if(compPolarity)
    {
        value |= 1 << ADS1115_CONFIG_BITS_COMP_POL;
    }
    else
    {
        value &= ~(1 << ADS1115_CONFIG_BITS_COMP_POL);
    }

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.compPolarity = compPolarity;

end_of_function:
    return returnBool;
}


boolean ADS1115::setComparatorLatchEnabled(ADS1115_Bits_Comp_Latching_t compLatching)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bit. */
    if(compLatching)
    {
        value |= 1 << ADS1115_CONFIG_BITS_COMP_LAT;
    }
    else
    {
        value &= ~(1 << ADS1115_CONFIG_BITS_COMP_LAT);
    }

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.compLatching = compLatching;

end_of_function:
    return returnBool;
}


boolean ADS1115::setComparatorQueueMode(ADS1115_Bits_Comp_Queue_t compQueueMode)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bits. */
    value = setBits16(ADS1115_CONFIG_BITS_COMP_QUE0, ADS1115_BIT_LENGTH_COMP_QUE, value, compQueueMode);

    /* Write the new value. */
    returnBool = ADS1115_writeBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    mConfig.compQueueMode = compQueueMode;

end_of_function:
    return returnBool;
}


/* Configuration getters. */
boolean ADS1115::getMux(ADS1115_Bits_Mux_t *mux)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *mux = getBits16(ADS1115_CONFIG_BITS_MUX0, ADS1115_BIT_LENGTH_MUX, value);

end_of_function:
    return returnBool;
}


boolean ADS1115::getGain(ADS1115_Bits_Pga_t *pga)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    /* Set the new value of just the desired bits. */
    *pga = getBits16(ADS1115_CONFIG_BITS_PGA0, ADS1115_BIT_LENGTH_PGA, value);

end_of_function:
    return returnBool;
}


boolean ADS1115::getMode(ADS1115_Bits_Mode_t *mode)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *mode = value & (1 << ADS1115_CONFIG_BITS_MODE);

end_of_function:
    return returnBool;
}


boolean ADS1115::getRate(ADS1115_Bits_Data_Rate_t *rate)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *rate = getBits16(ADS1115_CONFIG_BITS_COMP_DR0, ADS1115_BIT_LENGTH_DR, value);

end_of_function:
    return returnBool;

}


boolean ADS1115::getComparatorMode(ADS1115_Bits_Comp_Mode_t *compMode)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *compMode = value & (1 << ADS1115_CONFIG_BITS_COMP_MODE);

end_of_function:
    return returnBool;
}


boolean ADS1115::getComparatorPolarity(ADS1115_Bits_Comp_Polarity_t *compPolarity)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *compPolarity = value & (1 << ADS1115_CONFIG_BITS_COMP_POL);

end_of_function:
    return returnBool;
}


boolean ADS1115::getComparatorLatchEnabled(ADS1115_Bits_Comp_Latching_t *compLatching)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *compLatching = value & (1 << ADS1115_CONFIG_BITS_COMP_LAT);

end_of_function:
    return returnBool;
}


boolean ADS1115::getComparatorQueueMode(ADS1115_Bits_Comp_Queue_t *compQueueMode)
{
    boolean returnBool = FALSE;
    uint16 value = 0;

    /* Get the existing value. */
    returnBool = ADS1115_readBlock(ADS1115_REG_CONFIG, &value, sizeof(value));
    if(returnBool == FALSE)
    {
        goto end_of_function;
    }

    *compQueueMode = getBits16(ADS1115_CONFIG_BITS_COMP_QUE0, ADS1115_BIT_LENGTH_COMP_QUE, value);

end_of_function:
    return returnBool;
}


uint16 ADS1115::setBits16(uint8 bitStart, uint8 length, uint16 originalValue, uint16 data)
{
    uint16 word = originalValue;
    uint16 mask = ((1 << length) - 1) << (bitStart - length + 1);
    data <<= (bitStart - length + 1);
    data &= mask;
    word &= ~(mask);
    word |= data;
    return word;
}


uint16 ADS1115::getBits16(uint8 bitStart, uint8 length, uint16 originalValue)
{
    uint16 word = originalValue;
    uint16 mask = ((1 << length) - 1) << (bitStart - length + 1);
    word &= mask;
    word >>= (bitStart - length + 1);
    return word;
}


boolean ADS1115::getConfiguration(ADS1115_Configuration_t *config)
{
    return FALSE;
}


boolean ADS1115::setConfiguration(const ADS1115_Configuration_t *config)
{
    return FALSE;
}

/************************/
/*  End of File Comment */
/************************/