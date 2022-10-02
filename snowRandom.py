import math
import numpy as np
import pylab as plt
from numpy import fft
import util
import gold
import timeit
# from scripts.mlsPaper.gold import getGoldCodesByWebExample, getGoldCodesByPaperExample
import time
import snowAccuracy

goldCodes, goldCodesSet2 = gold.getGoldCodesByWebExample3()

numberOfNodes = 3
numberOfSubcarriers = 3
subCarrierBinary40ByteDataList = []
subCarrierSpreadedDataList = []
compoSiteSignalListOfSubcarriers = []
compositeSignal = []
carrierFrequencyList = util.getCarrierFrequencyList(numberOfSubcarriers)
#samplingFrequencyList = util.getSamplingFrequencyList(carrierFrequencyList)


for i in range(numberOfSubcarriers):
    subCarrierBinary40ByteDataList.append(util.getBinary40byteDataList(numberOfNodes))

goldCodeList = []
for i in range(numberOfSubcarriers):
    goldCodeList = []
    if i%2 == 0:
        goldCodeList = goldCodes
    else:
        goldCodeList = goldCodesSet2
    #subCarrierSpreadedDataList.append(util.buildSpreadDataForASubcarrier(subCarrierBinary40ByteDataList[i], goldCodeList, carrierFrequencyList[i], samplingFrequencyList[i]))
    #subCarrierSpreadedDataList.append(util.buildSpreadDataForASubcarrier(subCarrierBinary40ByteDataList[i], goldCodeList, carrierFrequencyList[i], util.fs))
    subCarrierSpreadedDataList.append(util.buildSpreadDataForASubcarrier(subCarrierBinary40ByteDataList[i], goldCodeList, carrierFrequencyList[i], carrierFrequencyList[i]*2))

for i in range(numberOfSubcarriers):
    compoSiteSignalListOfSubcarriers.append(util.buildCompositeSignal(subCarrierSpreadedDataList[i], carrierFrequencyList[i]))

for i in range(numberOfSubcarriers):
    compositeSignal = compositeSignal + compoSiteSignalListOfSubcarriers[i]

# print(list(util.sumSpreadData))

fftBinWithMag, fftBinWithPhase = util.continuousFFT(compositeSignal)
# fftBinWithMag, fftBinWithPhase = util.continuousFFT(compoSiteSignalListOfSubcarriers[0]+compoSiteSignalListOfSubcarriers[1])


#print(fftBinWithMag)



for i in range(numberOfSubcarriers):
    goldCodeList = []
    if i%2 == 0:
        goldCodeList = goldCodes
    else:
        goldCodeList = goldCodesSet2

    goldCodeList = goldCodeList[0: numberOfNodes]

    #print('code again: ', goldCodeList[0])

    print('Accuracy for subcarrier: ', i+1)
    snowAccuracy.evaluatePerformance(subCarrierBinary40ByteDataList[i], goldCodeList,fftBinWithMag, carrierFrequencyList[i])

    # if numberOfNodes == 1:
    #     carrier3Node7.nodeNumber1onEachSubcarrier(goldCodeList[0], len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 2:
    #     carrier3Node7.nodeNumber2onEachSubcarrier(goldCodeList[0], goldCodeList[1], len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 3:
    #     carrier3Node7.nodeNumber3onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], len(goldCodeList[0]),
    #                                               fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 4:
    #     carrier3Node7.nodeNumber4onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], goldCodeList[3],len(goldCodeList[0]),
    #                                               fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 5:
    #     carrier3Node7.nodeNumber5onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], goldCodeList[3], goldCodeList[4],
    #                                               len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 6:
    #     carrier3Node7.nodeNumber6onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], goldCodeList[3], goldCodeList[4], goldCodeList[5],
    #                                                len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 7:
    #     carrier3Node7.nodeNumber7onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], goldCodeList[3], goldCodeList[4], goldCodeList[5],
    #                                               goldCodeList[6], len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 8:
    #     carrier3Node7.nodeNumber8onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], goldCodeList[3], goldCodeList[4], goldCodeList[5],
    #                                               goldCodeList[6], goldCodeList[7], len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])
    # if numberOfNodes == 9:
    #     carrier3Node7.nodeNumber9onEachSubcarrier(goldCodeList[0], goldCodeList[1], goldCodeList[2], goldCodeList[3], goldCodeList[4], goldCodeList[5],
    #                                               goldCodeList[6], goldCodeList[7], goldCodeList[8], len(goldCodeList[0]), fftBinWithMag, carrierFrequencyList[i])







