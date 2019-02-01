class energy_conversion(object):

    def __init__(self):
        return

################################################################################
#Electricity Conversions
################################################################################

    #Watts & Hours to Watt-Hour
    def watt_hour_conversion(watts,min):
        """This function takes Watts and a given Time frame and converts to Watt-Hours.

        watts: Unit of Power.
        min: (in minutes) the timeframe that power is being transfered.
        """
        hours = min/60
        wH = watts * hours

        if watts < 1000:
            energy = 'The Watt-Hours are {}Wh'.format(wH)
        elif watts >=1000 and watts < 1000000:
            KWh = wH/1000
            energy = 'The Watt-Hours are {}KWh.'.format(KWh)
        elif watts >=1000000 and watts < 1000000000:
            MWh = wH/1000000
            energy = 'The Watt-Hours are {}MWh'.format(MWh)
        elif watts >=1000000000 and watts < 1000000000000:
            GWh = wH/1000000000
            energy = 'The Watt-Hours are {}GWh.'.format(GWh)
        elif watts >=1000000000000 and watts < 1000000000000000:
            TWh = wH/1000000000000
            energy = 'The Watt-Hours are {}TWh'.format(TWh)
        return energy

################################################################################
#Natural Gas Conversions
################################################################################

    #Cubic Feet to BTU or Therm
    def btu_conversion(cf):
        """This function takes Cubic Feet of Natural Gas and converts them to British Thermal Units (BTU).

        cf (Cubic Feet): Cubic Feet of Natural Gas.
        """
        btu = 1020 * cf
        if btu < 1000000:
            BTU = 'British Thermal Units (BTU): {}'.format(btu)
            return BTU
        else:
            mmBTU = "Million BTU's(mmBTU): {}".format(btu/1000000)
            return mmBTU

    def cubic_feet_conversion(BTU):
        """This function takes British Thermal Units (BTU) of Natural Gas and converts them to Cubic Feet of Natural Gas.

        BTU: British Thermal Units of Natural Gas.
        """
        CubicFt = BTU / 1020
        if CubicFt < 100:
            Cubic_Feet = "Cubic Feet: {}".format(CubicFt)
            return Cubic_Feet
        elif CubicFt >= 100 and CubicFt < 1000:
            CubicFt = CubicFt/100
            Hundred_Cubic_Feet = "Hundred Cubic Feet(CcF): {}".format(CubicFt)
            return Hundred_Cubic_Feet
        else:
            CubicFt = CubicFt/1000
            Comma_Cubic_Feet = "Thousand Cubic Feet (McF): {}".format(CubicFt)
            return Comma_Cubic_Feet

    def therm_conversion(BTU):
        """This function takes British Thermal Units (BTU) of Natural Gas and converts them to Therms of Natural Gas.

        BTU: British Thermal Units of Natural Gas.
        """
        if BTU < 1000000:
            therms = BTU/100000
            Therms = 'Therms: {}'.format(therms)
            return Therms
        elif BTU >= 1000000:
            decatherm = BTU/1000000
            Decatherms = '{} DecaTherms'.format(decatherm)
            return Decatherms
