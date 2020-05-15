import unittest
import numpy as np
import colorPicker


class ColorPickerTest(unittest.TestCase):


    def test_imgNdarrayToColorNdarray(self):
        testcase = np.array([[[255,255,255],[0,0,0]],[[255,255,255],[0,0,0]]])
        test = colorPicker.imgNdarray2ColorNdarray(testcase)
        expected = np.array([[255,255,255],[0,0,0],[255,255,255],[0,0,0]])
        self.assertEqual(test.tolist(), expected.tolist())


    def test_abstraction(self):
        testcase = np.array([[255,255,255],[0,0,0],[255,255,255],[0,0,0]])
        expected = np.array([[17,11,11],[0,0,0],[17,11,11],[0,0,0]])
        self.assertEqual(colorPicker.abstraction(testcase).tolist(), expected.tolist())


    def test_getColorFeature(self):
        # abstraction()で値は11以下になっているようにする
        testcase = np.array([[11,11,11],[0,0,0],[11,11,11],[0,0,0]])
        # [hue, saturation, value]の配列に変換するために転置する
        testcase = testcase.T
        testcase = colorPicker.getColorFeature(testcase)
        # getColorFeature()の返り値の中身がNdarrayだからlistに変換する必要がある(要改善)
        testcase = [testcase[0].tolist(),testcase[1].tolist(),testcase[2].tolist()]
        expected = [
            [0.5, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.5],
            [0.5, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.5],
            [0.5, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.5]
            ]
        self.assertEqual(testcase,expected)


    def test_colorRatio(self):
        # 各要素の割合　どの色がどの程度使用されているかに使う
        testcase = np.array([0, 12, 28, 3, 57])
        expected = np.array([0, 0.12, 0.28, 0.03, 0.57])
        self.assertEqual(colorPicker.colorRatio(testcase).tolist(), expected.tolist())


    def test_fillZero(self):
        # colorRatioが0~11の順番で並んでほしいので間を「0.0」で埋める
        testcaseKind  = [0  ,1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,10  ,11  ]
        testcaseRatio = [0.2,0.1,0.5,0.3,0.7,0.6,0.8,0.9,0.4,0.11,0.12]
        expected      = [0.2,0.1,0.5,0.3,0.7,0.6,0.8,0.9,0.4,0.0 ,0.11,0.12]
        self.assertEqual(colorPicker.fillZero(testcaseKind, testcaseRatio).tolist(), expected)


    def test_getEntropy(self):
        testcase = np.array([0.5, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.5])
        expected = 1
        self.assertEqual(colorPicker.getEntropy(testcase), expected)


    def test_hueTojson(self):
        testcase = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        expected = {
            'red':0,
            'red-yellow':1,
            'yellow':2,
            'yellow-green':3,
            'green':4,
            'green-cyan':5,
            'cyan':6,
            'cyan-blue':7,
            'blue':8,
            'blue-purple':9,
            'purple':10,
            'purple-red':11,
        }
        self.assertEqual(colorPicker.hueTojson(testcase), expected)


    def test_saturationTojson(self):
        testcase = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        expected = {
            's0': 0,
            's1': 1,
            's2': 2,
            's3': 3,
            's4': 4,
            's5': 5,
            's6': 6,
            's7': 7,
            's8': 8,
            's9': 9,
            's10': 10,
            's10': 11,
        }
        self.assertEqual(colorPicker.saturationTojson(testcase), expected)


    def test_valueTojson(self):
        testcase = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        expected = {
            'v0': 0,
            'v1': 1,
            'v2': 2,
            'v3': 3,
            'v4': 4,
            'v5': 5,
            'v6': 6,
            'v7': 7,
            'v8': 8,
            'v9': 9,
            'v10': 10,
            'v11': 11,
        } 
        self.assertEqual(colorPicker.valueTojson(testcase), expected)
        

if __name__ == '__main__':
    unittest.main()