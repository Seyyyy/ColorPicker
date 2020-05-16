import numpy as np
import cv2
import math
import json

# np.uniqueで使用されるカラーリストを抽出するための前処理
def imgNdarray2ColorNdarray(imgNdarray):
    img_array = []
    for cell in imgNdarray:
        for row in cell:
            img_array.append(row)
    img_array = np.array(img_array)
    return img_array

# hsvだと色数が多すぎるので扱いやすくするために抽象化をする
def abstraction(imgNdarray):
    img_array = []
    abstParam = [15, 21.33, 21.33]
    img_array = np.floor(imgNdarray / abstParam)
    img_array = img_array.astype(np.int64)
    return img_array

# とっても重い処理(約３秒くらい)uniqueが重たいたぶん
# 色相、彩度、明度ごとに割合を導出する
def getColorFeature(uniqueColorNdarray):
    hue, hueCount = np.unique(uniqueColorNdarray[0], return_counts=True)
    saturation, satuCount = np.unique(uniqueColorNdarray[1], return_counts=True)
    value, valueCount = np.unique(uniqueColorNdarray[2], return_counts=True)
    hueRatio = fillZero(hue, colorRatio(hueCount))
    satuRatio = fillZero(saturation, colorRatio(satuCount))
    valueRatio = fillZero(value, colorRatio(valueCount))
    ratio = [hueRatio, satuRatio, valueRatio]
    return ratio

def colorRatio(colorCountNdarray):
    ratio = np.round(colorCountNdarray / colorCountNdarray.sum(), 3)
    return ratio

# csvで扱いやすくするために列と対応させるように０で埋める
def fillZero(colorKindNdarray, colorRatioNdarray):
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
    hueDict = {
        'red':hueNdarray[0],
        'red-yellow':hueNdarray[1],
        'yellow':hueNdarray[2],
        'yellow-green':hueNdarray[3],
        'green':hueNdarray[4],
        'green-cyan':hueNdarray[5],
        'cyan':hueNdarray[6],
        'cyan-blue':hueNdarray[7],
        'blue':hueNdarray[8],
        'blue-purple':hueNdarray[9],
        'purple':hueNdarray[10],
        'purple-red':hueNdarray[11],
    }
    return hueDict

def saturationTojson(satuNdarray):
    satuDict = {
        's0': satuNdarray[0],
        's1': satuNdarray[1],
        's2': satuNdarray[2],
        's3': satuNdarray[3],
        's4': satuNdarray[4],
        's5': satuNdarray[5],
        's6': satuNdarray[6],
        's7': satuNdarray[7],
        's8': satuNdarray[8],
        's9': satuNdarray[9],
        's10': satuNdarray[10],
        's10': satuNdarray[11],
    }
    return satuDict

def valueTojson(valueNdarray):
    valueDict = {
        'v0': valueNdarray[0],
        'v1': valueNdarray[1],
        'v2': valueNdarray[2],
        'v3': valueNdarray[3],
        'v4': valueNdarray[4],
        'v5': valueNdarray[5],
        'v6': valueNdarray[6],
        'v7': valueNdarray[7],
        'v8': valueNdarray[8],
        'v9': valueNdarray[9],
        'v10': valueNdarray[10],
        'v11': valueNdarray[11],
    } 
    return valueDict

# とりあえず繰り返し処理しやすいようにまとめる
def mainFunction(imageFileName):
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