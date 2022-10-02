import util
import numpy as np

def evaluatePerformance(dataList, codeListOfASubcarrier, fftBinWithMag, fc):

    numberOfNodes = len(dataList)

    dataRecoveredList = []
    dataRecoveredInBitsList = []
    accuracyList = []

    for i in range(numberOfNodes):
        # print('code in despreading : ', codeListOfASubcarrier[i])
        code =  util.getDataCode(codeListOfASubcarrier[i], len(dataList[i]))

        #dataRecovered = util.despread(fftBinWithMag[util.getFrequencyMappingModified(fc, list(fftBinWithMag.keys()))], code, len(codeListOfASubcarrier[i]))
        dataRecovered = util.despread(fftBinWithMag[fc], code, len(codeListOfASubcarrier[i]))
        # dataRecovered = util.despread(util.conversionOfCompositeSignal(fftBinWithMag[fc]), code, len(codeListOfASubcarrier[i]))
        dataRecoveredList.append(dataRecovered)

    for i in range(numberOfNodes):
        dataRecoveredInBits = util.getBitsAfterDspread(dataRecoveredList[i])
        dataRecoveredInBitsList.append(dataRecoveredInBits)

    for i in range(numberOfNodes):
        accuracy = util.getAccuracy(dataList[i], dataRecoveredInBitsList[i])
        accuracyList.append(accuracy)


    # d0PacketError = util.packetError(d0_input, d0_bits)
    # d1PacketError = util.packetError(d1_input, d1_bits)
    # d2PacketError = util.packetError(d2_input, d2_bits)
    # d3PacketError = util.packetError(d3_input, d3_bits)
    # d4PacketError = util.packetError(d4_input, d4_bits)
    # d5PacketError = util.packetError(d5_input, d5_bits)
    # d6PacketError = util.packetError(d6_input, d6_bits)
    # d7PacketError = util.packetError(d7_input, d7_bits)
    # d8PacketError = util.packetError(d8_input, d8_bits)

    #print('Total packet error: ', d0PacketError + d1PacketError + d2PacketError + d3PacketError + d4PacketError + d5PacketError + d6PacketError + d7PacketError + d8PacketError)

    #print('Total error bit count for '+ str(numberOfNodes) + ' number of sensors: ', util.totalErrorBitCount)
    #print('Bit error per packet: ', util.totalErrorBitCount/(2240)
    # ber = util.totalErrorBitCount/(40*8*9*100)
    #ber = util.totalErrorBitCount/(40*8*numberOfNodes*100)
    #print('Bit error per packet: ', ber)
    #outfile = open('bitErrorRate.txt', "a")
    #outfile.writelines(str(ber) + "\n")

    # print('total error Bit: ', util.totalErrorBitCount)

    for i in range(numberOfNodes):
        print('accuracy of node ' + str(i+1) + ' is: ', accuracyList[i])


    totalAccuracy = sum(accuracyList)/numberOfNodes
    print('Average accuracy of ' +str(numberOfNodes) +  ' nodes is: ' , totalAccuracy)
    outfile = open('accuracy.txt', "a")
    outfile.writelines(str(totalAccuracy)+"\n")

