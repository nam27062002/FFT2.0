import Training
import threading 
class statistical:
    def __init__(self,training) -> None:
        self.training = training
        self.vowels = ["a","e","i","o","u"]
        self.Correct,self.ARR = self.processPercent()
    def processPercent(self):
        S = [0,0,0]
        ARR = [0,0,0]
        def nfft512():
            nfft = 512
            arr = [ [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
            s = 0
            for vowel in self.vowels:
                for index in range(1,22):
                    url = f"Test/{index}/{vowel}.wav"
                    C  = self.training.compare(url,nfft)[0]
                    if C == vowel:
                        s += 1
                    if C == vowel and vowel == "a":
                        arr[0][0] += 1
                    elif C == vowel and vowel == "e":
                        arr[1][1] += 1
                    elif C == vowel and vowel == "i":
                        arr[2][2] += 1
                    elif C == vowel and vowel == "o":
                        arr[3][3] += 1
                    elif C == vowel and vowel == "u":
                        arr[4][4] += 1
                    elif C == "e" and vowel == "a":
                        arr[1][0] += 1
                    elif C == "i" and vowel == "a":
                        arr[2][0] += 1
                    elif C == "o" and vowel == "a":
                        arr[3][0] += 1
                    elif C == "u" and vowel == "a":
                        arr[4][0] += 1             
                    elif C == "a" and vowel == "e":
                        arr[0][1] += 1
                    elif C == "i" and vowel == "e":
                        arr[2][1] += 1
                    elif C == "o" and vowel == "e":
                        arr[3][1] += 1
                    elif C == "u" and vowel == "e":
                        arr[4][1] += 1                
                    elif C == "a" and vowel == "i":
                        arr[0][2] += 1
                    elif C == "e" and vowel == "i":
                        arr[1][2] += 1
                    elif C == "o" and vowel == "i":
                        arr[3][2] += 1
                    elif C == "u" and vowel == "i":
                        arr[4][2] += 1                
                    elif C == "a" and vowel == "o":
                        arr[0][3] += 1
                    elif C == "e" and vowel == "o":
                        arr[1][3] += 1
                    elif C == "i" and vowel == "o":
                        arr[2][3] += 1
                    elif C == "u" and vowel == "o":
                        arr[4][3] += 1               
                    elif C == "a" and vowel == "u":
                        arr[0][4] += 1
                    elif C == "e" and vowel == "u":
                        arr[1][4] += 1
                    elif C == "i" and vowel == "u":
                        arr[2][4] += 1
                    elif C == "o" and vowel == "u":
                        arr[3][4] += 1
            S[0] = s
            ARR[0] = arr
        def nfft1024():
            nfft = 2014
            arr = [ [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
            s = 0
            for vowel in self.vowels:
                for index in range(1,22):
                    url = f"Test/{index}/{vowel}.wav"
                    C  = self.training.compare(url,nfft)[0]
                    if C == vowel:
                        s += 1
                    if C == vowel and vowel == "a":
                        arr[0][0] += 1
                    elif C == vowel and vowel == "e":
                        arr[1][1] += 1
                    elif C == vowel and vowel == "i":
                        arr[2][2] += 1
                    elif C == vowel and vowel == "o":
                        arr[3][3] += 1
                    elif C == vowel and vowel == "u":
                        arr[4][4] += 1
                    elif C == "e" and vowel == "a":
                        arr[1][0] += 1
                    elif C == "i" and vowel == "a":
                        arr[2][0] += 1
                    elif C == "o" and vowel == "a":
                        arr[3][0] += 1
                    elif C == "u" and vowel == "a":
                        arr[4][0] += 1             
                    elif C == "a" and vowel == "e":
                        arr[0][1] += 1
                    elif C == "i" and vowel == "e":
                        arr[2][1] += 1
                    elif C == "o" and vowel == "e":
                        arr[3][1] += 1
                    elif C == "u" and vowel == "e":
                        arr[4][1] += 1                
                    elif C == "a" and vowel == "i":
                        arr[0][2] += 1
                    elif C == "e" and vowel == "i":
                        arr[1][2] += 1
                    elif C == "o" and vowel == "i":
                        arr[3][2] += 1
                    elif C == "u" and vowel == "i":
                        arr[4][2] += 1                
                    elif C == "a" and vowel == "o":
                        arr[0][3] += 1
                    elif C == "e" and vowel == "o":
                        arr[1][3] += 1
                    elif C == "i" and vowel == "o":
                        arr[2][3] += 1
                    elif C == "u" and vowel == "o":
                        arr[4][3] += 1               
                    elif C == "a" and vowel == "u":
                        arr[0][4] += 1
                    elif C == "e" and vowel == "u":
                        arr[1][4] += 1
                    elif C == "i" and vowel == "u":
                        arr[2][4] += 1
                    elif C == "o" and vowel == "u":
                        arr[3][4] += 1
            S[1] = s
            ARR[1] = arr
        def nfft2048():
            nfft = 2048
            arr = [ [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
            s = 0
            for vowel in self.vowels:
                for index in range(1,22):
                    url = f"Test/{index}/{vowel}.wav"
                    C  = self.training.compare(url,nfft)[0]
                    if C == vowel:
                        s += 1
                    if C == vowel and vowel == "a":
                        arr[0][0] += 1
                    elif C == vowel and vowel == "e":
                        arr[1][1] += 1
                    elif C == vowel and vowel == "i":
                        arr[2][2] += 1
                    elif C == vowel and vowel == "o":
                        arr[3][3] += 1
                    elif C == vowel and vowel == "u":
                        arr[4][4] += 1
                    elif C == "e" and vowel == "a":
                        arr[1][0] += 1
                    elif C == "i" and vowel == "a":
                        arr[2][0] += 1
                    elif C == "o" and vowel == "a":
                        arr[3][0] += 1
                    elif C == "u" and vowel == "a":
                        arr[4][0] += 1             
                    elif C == "a" and vowel == "e":
                        arr[0][1] += 1
                    elif C == "i" and vowel == "e":
                        arr[2][1] += 1
                    elif C == "o" and vowel == "e":
                        arr[3][1] += 1
                    elif C == "u" and vowel == "e":
                        arr[4][1] += 1                
                    elif C == "a" and vowel == "i":
                        arr[0][2] += 1
                    elif C == "e" and vowel == "i":
                        arr[1][2] += 1
                    elif C == "o" and vowel == "i":
                        arr[3][2] += 1
                    elif C == "u" and vowel == "i":
                        arr[4][2] += 1                
                    elif C == "a" and vowel == "o":
                        arr[0][3] += 1
                    elif C == "e" and vowel == "o":
                        arr[1][3] += 1
                    elif C == "i" and vowel == "o":
                        arr[2][3] += 1
                    elif C == "u" and vowel == "o":
                        arr[4][3] += 1               
                    elif C == "a" and vowel == "u":
                        arr[0][4] += 1
                    elif C == "e" and vowel == "u":
                        arr[1][4] += 1
                    elif C == "i" and vowel == "u":
                        arr[2][4] += 1
                    elif C == "o" and vowel == "u":
                        arr[3][4] += 1
            S[2] = s
            ARR[2] = arr
        T = []
        T.append(threading.Thread(target=nfft512))
        T.append(threading.Thread(target=nfft1024))
        T.append(threading.Thread(target=nfft2048))
        for i in T:
            i.start()
        for i in T:
            i.join()
        return S,ARR
X = Training.Training()
y = statistical(X)
print(y.processPercent())