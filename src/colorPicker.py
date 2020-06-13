import numpy as np
import cv2
import math
import json


def imgNdarray2ColorNdarray(imgNdarray):
    '''np.uniqueで使用されるカラーリストを抽出するための前処理'''
    return np.array([row for cell in imgNdarray for row in cell])


def abstraction(imgNdarray):
    '''hsvだと色数が多すぎるので扱いやすくするために抽象化をする'''
    img_array = []
    abstParam = [15, 21.33, 21.33]
    img_array = np.floor(imgNdarray / abstParam)
    return img_array.astype(np.int64)


def getColorFeature(uniqueColorNdarray):
    '''
    とっても重い処理(約３秒くらい)uniqueが重たいたぶん
    色相、彩度、明度ごとに割合を導出する
    '''
    hue, hueCount = np.unique(uniqueColorNdarray[0], return_counts=True)
    saturation, satuCount = np.unique(uniqueColorNdarray[1], return_counts=True)
    value, valueCount = np.unique(uniqueColorNdarray[2], return_counts=True)
    hueRatio = fillZero(hue, colorRatio(hueCount))
    satuRatio = fillZero(saturation, colorRatio(satuCount))
    valueRatio = fillZero(value, colorRatio(valueCount))
    return [hueRatio, satuRatio, valueRatio]


def colorRatio(colorCountNdarray):
    return np.round(colorCountNdarray / colorCountNdarray.sum(), 3)


def fillZero(colorKindNdarray, colorRatioNdarray):
    '''csvで扱いやすくするために列と対応させるように０で埋める'''
    abstractionNumber = 12
    ratioArray = np.zeros(abstractionNumber)
    for i, colorNumber in enumerate(colorKindNdarray):
        ratioArray[colorNumber] = colorRatioNdarray[i]
    return ratioArray


def getEntropy(ratioNdarray):
    H = 0
    for ratio in ratioNdarray:
        if ratio == 0:
            continue
        H -= ratio * math.log2(ratio)
    return H


def hueTojson(hueNdarray):
    hueDict = [
            {
                'color': 'red',
                'hex': '#f04646',
                'ratio': hueNdarray[0]
            },
            {
                'color': 'red-yellow',
                'hex': '#f09b46',
                'ratio': hueNdarray[1]
            },
            {
                'color': 'yellow',
                'hex': '#f0f046',
                'ratio': hueNdarray[2]
            },
            {
                'color': 'yellow-green',
                'hex': '#9bf046',
                'ratio': hueNdarray[3]
            },
            {
                'color': 'green',
                'hex': '#46f046',
                'ratio': hueNdarray[4]
            },
            {
                'color': 'green-cyan',
                'hex': '#46f09b',
                'ratio': hueNdarray[5]
            },
            {
                'color': 'cyan',
                'hex': '#46f0f0',
                'ratio': hueNdarray[6]
            },
            {
                'color': 'cyan-blue',
                'hex': '#469bf0',
                'ratio': hueNdarray[7]
            },
            {
                'color': 'blue',
                'hex': '#4646f0',
                'ratio': hueNdarray[8]
            },
            {
                'color': 'blue-purple',
                'hex': '#9b46f0',
                'ratio': hueNdarray[9]
            },
            {
                'color': 'purple',
                'hex': '#f046f0',
                'ratio': hueNdarray[10]
            },
            {
                'color': 'purple-red',
                'hex': '#f0469b',
                'ratio': hueNdarray[11]
            },
        ]
    return hueDict


def saturationTojson(satuNdarray):
    satuDict = [
            {
                'color': 's0',
                'hex': '#ffffff',
                'ratio': satuNdarray[0]
            },
            {
                'color': 's1',
                'hex': '#ffebeb',
                'ratio': satuNdarray[1]
            },
            {
                'color': 's2',
                'hex': '#ffd6d6',
                'ratio': satuNdarray[2]
            },
            {
                'color': 's3',
                'hex': '#ffc2c2',
                'ratio': satuNdarray[3]
            },
            {
                'color': 's4',
                'hex': '#ffadad',
                'ratio': satuNdarray[4]
            },
            {
                'color': 's5',
                'hex': '#ff9999',
                'ratio': satuNdarray[5]
            },
            {
                'color': 's6',
                'hex': '#ff8585',
                'ratio': satuNdarray[6]
            },
            {
                'color': 's7',
                'hex': '#ff7070',
                'ratio': satuNdarray[7]
            },
            {
                'color': 's8',
                'hex': '#ff5c5c',
                'ratio': satuNdarray[8]
            },
            {
                'color': 's9',
                'hex': '#ff4747',
                'ratio': satuNdarray[9]
            },
            {
                'color': 's10',
                'hex': '#ff3333',
                'ratio': satuNdarray[10]
            },
            {
                'color': 's11',
                'hex': '#ff1f1f',
                'ratio': satuNdarray[11]
            },
        ]
    return satuDict


def valueTojson(valueNdarray):
    valueDict = [
            {
                'color': 'v0',
                'hex': '#000000',
                'ratio': valueNdarray[0]
            },
            {
                'color': 'v1',
                'hex': '#141414',
                'ratio': valueNdarray[1]
            },
            {
                'color': 'v2',
                'hex': '#292929',
                'ratio': valueNdarray[2]
            },
            {
                'color': 'v3',
                'hex': '#3d3d3d',
                'ratio': valueNdarray[3]
            },
            {
                'color': 'v4',
                'hex': '#525252',
                'ratio': valueNdarray[4]
            },
            {
                'color': 'v5',
                'hex': '#666666',
                'ratio': valueNdarray[5]
            },
            {
                'color': 'v6',
                'hex': '#7a7a7a',
                'ratio': valueNdarray[6]
            },
            {
                'color': 'v7',
                'hex': '#8f8f8f',
                'ratio': valueNdarray[7]
            },
            {
                'color': 'v8',
                'hex': '#a3a3a3',
                'ratio': valueNdarray[8]
            },
            {
                'color': 'v9',
                'hex': '#b8b8b8',
                'ratio': valueNdarray[9]
            },
            {
                'color': 'v10',
                'hex': '#cccccc',
                'ratio': valueNdarray[10]
            },
            {
                'color': 'v11',
                'hex': '#e0e0e0',
                'ratio': valueNdarray[11]
            },
        ]
    return valueDict


def mainFunction(imageFileName):
    '''とりあえず繰り返し処理しやすいようにまとめる'''
    # img = cv2.imread(imageFileName, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(imageFileName, cv2.COLOR_BGR2HSV)
    img_array = imgNdarray2ColorNdarray(img)
    img_array = abstraction(img_array)
    # Hue, Saturation, Valueをまとめた２次元配列
    uniqueColorArray = img_array.T
    hsvColorKind = getColorFeature(uniqueColorArray)
    # エントロピー用の配列を作る
    hueEntropy = getEntropy(hsvColorKind[0])
    satuEntropy = getEntropy(hsvColorKind[1])
    valueEntropy = getEntropy(hsvColorKind[2])
    entropy = [hueEntropy, satuEntropy, valueEntropy]
    #１次元配列に平滑化（もっといい方法あると思う）
    csvArray = np.append(hsvColorKind[0], hsvColorKind[1])
    csvArray = np.append(csvArray, hsvColorKind[2])
    csvArray = np.append(csvArray, entropy)
    #配列をjsonに直したい
    colorDict = {
        'hue': hueTojson(hsvColorKind[0]),
        'saturation': saturationTojson(hsvColorKind[1]),
        'value': valueTojson(hsvColorKind[2]),
        'entropy': {
            'hue': hueEntropy,
            'saturation': satuEntropy,
            'value': valueEntropy
        }
    }
    return colorDict