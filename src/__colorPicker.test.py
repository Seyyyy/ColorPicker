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
        expected = [
            {
                'color': 'red',
                'hex': '#f04646',
                'ratio': 0
            },
            {
                'color': 'red-yellow',
                'hex': '#f09b46',
                'ratio': 1
            },
            {
                'color': 'yellow',
                'hex': '#f0f046',
                'ratio': 2
            },
            {
                'color': 'yellow-green',
                'hex': '#9bf046',
                'ratio': 3
            },
            {
                'color': 'green',
                'hex': '#46f046',
                'ratio': 4
            },
            {
                'color': 'green-cyan',
                'hex': '#46f09b',
                'ratio': 5
            },
            {
                'color': 'cyan',
                'hex': '#46f0f0',
                'ratio': 6
            },
            {
                'color': 'cyan-blue',
                'hex': '#469bf0',
                'ratio': 7
            },
            {
                'color': 'blue',
                'hex': '#4646f0',
                'ratio': 8
            },
            {
                'color': 'blue-purple',
                'hex': '#9b46f0',
                'ratio': 9
            },
            {
                'color': 'purple',
                'hex': '#f046f0',
                'ratio': 10
            },
            {
                'color': 'purple-red',
                'hex': '#f0469b',
                'ratio': 11
            },
        ]
        self.assertEqual(colorPicker.hueTojson(testcase), expected)

    def test_saturationTojson(self):
        testcase = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        expected = [
            {
                'color': 's0',
                'hex': '#ffffff',
                'ratio': 0
            },
            {
                'color': 's1',
                'hex': '#ffebeb',
                'ratio': 1
            },
            {
                'color': 's2',
                'hex': '#ffd6d6',
                'ratio': 2
            },
            {
                'color': 's3',
                'hex': '#ffc2c2',
                'ratio': 3
            },
            {
                'color': 's4',
                'hex': '#ffadad',
                'ratio': 4
            },
            {
                'color': 's5',
                'hex': '#ff9999',
                'ratio': 5
            },
            {
                'color': 's6',
                'hex': '#ff8585',
                'ratio': 6
            },
            {
                'color': 's7',
                'hex': '#ff7070',
                'ratio': 7
            },
            {
                'color': 's8',
                'hex': '#ff5c5c',
                'ratio': 8
            },
            {
                'color': 's9',
                'hex': '#ff4747',
                'ratio': 9
            },
            {
                'color': 's10',
                'hex': '#ff3333',
                'ratio': 10
            },
            {
                'color': 's11',
                'hex': '#ff1f1f',
                'ratio': 11
            },
        ]
        self.assertEqual(colorPicker.saturationTojson(testcase), expected)


    def test_valueTojson(self):
        testcase = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        expected = [
            {
                'color': 'v0',
                'hex': '#000000',
                'ratio': 0
            },
            {
                'color': 'v1',
                'hex': '#141414',
                'ratio': 1
            },
            {
                'color': 'v2',
                'hex': '#292929',
                'ratio': 2
            },
            {
                'color': 'v3',
                'hex': '#3d3d3d',
                'ratio': 3
            },
            {
                'color': 'v4',
                'hex': '#525252',
                'ratio': 4
            },
            {
                'color': 'v5',
                'hex': '#666666',
                'ratio': 5
            },
            {
                'color': 'v6',
                'hex': '#7a7a7a',
                'ratio': 6
            },
            {
                'color': 'v7',
                'hex': '#8f8f8f',
                'ratio': 7
            },
            {
                'color': 'v8',
                'hex': '#a3a3a3',
                'ratio': 8
            },
            {
                'color': 'v9',
                'hex': '#b8b8b8',
                'ratio': 9
            },
            {
                'color': 'v10',
                'hex': '#cccccc',
                'ratio': 10
            },
            {
                'color': 'v11',
                'hex': '#e0e0e0',
                'ratio': 11
            },
        ]
        self.assertEqual(colorPicker.valueTojson(testcase), expected)
        

if __name__ == '__main__':
    unittest.main()