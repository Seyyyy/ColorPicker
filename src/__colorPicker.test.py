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


    # def test_getColorFeature(self):
    #     testcase = np.array([[255,255,255],[0,0,0],[255,255,255],[0,0,0]])
    #     testcase = testcase.T
    #     expected = np.array([[255,255,255,255],[255,255,255,255],[255,255,255,255]])
    #     expected = expected.T
    #     self.assertEqual(colorPicker.getColorFeature(testcase), expected.tolist())


    def test_hueTojson(self):
        testcase = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
        hueDict = {
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
        self.assertEqual(colorPicker.hueTojson(testcase), hueDict)


if __name__ == '__main__':
    unittest.main()