import gold
import numpy as np
import util
import snowAccuracy

# from scripts.mlsPaper.gold import getGoldCodesByWebExample, getGoldCodesByPaperExample

goldCodes, goldCodesSet2 = gold.getGoldCodesByWebExample3()

numberOfNodes = 4

numberOfSubcarriers = 2
nodesNumberOnSubcarriers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subCarrierBinary40ByteDataList = []
subCarrierSpreadedDataList = []
compoSiteSignalListOfSubcarriers = []

fs = 1120
fr = fs/2240
centerFrequency = 520
carrierFrequencyList = util.getCarrierFrequencyListRevised(numberOfSubcarriers, 519.5, 520, 0.5)
subcarrierFFTIndexMapping = util.getSubcarriersFFTIndex(carrierFrequencyList, centerFrequency, fs, fr)



for i in range(numberOfSubcarriers):
    subCarrierBinary40ByteDataList.append(util.getBinary40byteDataList(numberOfNodes))

goldCodeList = []
for i in range(numberOfSubcarriers):
    goldCodeList = []
    if i%2 == 0:
        goldCodeList = goldCodes
    else:
        goldCodeList = goldCodesSet2
    subCarrierSpreadedDataList.append(util.buildSpreadDataForSubcarrierRevised(subCarrierBinary40ByteDataList[i],
                                                                               goldCodeList, carrierFrequencyList[i], fs))

for i in range(numberOfSubcarriers):
    compoSiteSignalListOfSubcarriers.append(util.mergeSignalsOfSubcarrier(subCarrierSpreadedDataList[i]))

compositeSignal = np.zeros(len(compoSiteSignalListOfSubcarriers[0][0]))
centerSignal = util.getSignal(centerFrequency, fs, len(compositeSignal))
subcarriesrBits = []
for i in range(len(compositeSignal)):
    compositeSignal = np.zeros(len(compoSiteSignalListOfSubcarriers[0][0]))
    compositeByCenterMultiplication = []
    fftResult = []

    for compositeSignalOfEachSubcarrier in compoSiteSignalListOfSubcarriers:
        compositeSignal = compositeSignal + compositeSignalOfEachSubcarrier[i]

    compositeByCenterMultiplication = np.multiply(compositeSignal, centerSignal)

    fftResult = util.fftRevised(compositeByCenterMultiplication, fs, len(compositeByCenterMultiplication))
    subcarriesrBits.append(fftResult[list(subcarrierFFTIndexMapping.values())])

subcarriersCompositeSignal = util.getSubcarriersCompositeSignal(subcarriesrBits, subcarrierFFTIndexMapping)

for freq in carrierFrequencyList:
    cSignal = subcarriersCompositeSignal[str(freq)]
    maxValue = np.max(cSignal)
    cSignal = [ (bit*1) + (maxValue-bit)*-1 for bit in cSignal]
    subcarriersCompositeSignal[str(freq)] = cSignal

util.getSystemAccuracy(numberOfSubcarriers, numberOfNodes, subCarrierBinary40ByteDataList,
                       goldCodes, goldCodesSet2,subcarriersCompositeSignal, carrierFrequencyList)


