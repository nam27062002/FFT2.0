import Speech_Silence
import threading
import numpy as np  
class Training:
    # hàm khởi tạo
    def __init__(self) -> None:
        self.vowels = ["a","e","i","o","u"]
        self.eigenvectors = [0,0,0]
        self.ThreadTrain()
        self.F = 16000
        self.Count, self.Statistical = self.ThreadTest()
        self.Percent = self.getPercent()
    
    # hàm huấn luyện
    def train_NFFT(self,NFFT):
        eigenvectors = [0,0,0,0,0]
        def threadChar(c,S): 
            eigenvector = []
            for index in range(1,22):
                url = f"Training/{index}/{c}.wav"
                Audio = Speech_Silence.speech_silence(url)
                eigenvector.append(Audio.vectorFFT[NFFT])
            average = []
            for i in range(len(eigenvector[0])):
                s = 0
                for j in range(len(eigenvector)):
                    s += abs(eigenvector[j][i])
                average.append(s/len(eigenvector))
            eigenvectors[S] = average
        T = []
        T.append(threading.Thread(target=threadChar,args=["a",0]))
        T.append(threading.Thread(target=threadChar,args=["e",1]))
        T.append(threading.Thread(target=threadChar,args=["i",2]))
        T.append(threading.Thread(target=threadChar,args=["o",3]))
        T.append(threading.Thread(target=threadChar,args=["u",4]))
        for i in T:
            i.start()
        for i in T:
            i.join()
        self.eigenvectors[NFFT] = eigenvectors
    
    def ThreadTrain(self):
        T = []
        T.append(threading.Thread(target=self.train_NFFT,args=[0]))
        T.append(threading.Thread(target=self.train_NFFT,args=[1]))
        T.append(threading.Thread(target=self.train_NFFT,args=[2]))
        for i in T:
            i.start()
        for i in T:
            i.join()
        
    def ThreadTest(self):
        S = [0,0,0]
        ARR = [0,0,0]
        def A():
            S[0],ARR[0] = self.statistical(512)
        def B():
            S[1],ARR[1] = self.statistical(1024)
        def C():
            S[2],ARR[2] = self.statistical(2048)
        T = []
        T.append(threading.Thread(target=A))
        T.append(threading.Thread(target=B))
        T.append(threading.Thread(target=C))
        for i in T:
            i.start()
        for i in T:
            i.join()
        return S,ARR
    
    def getEigenvectors(self):
        arr = []
        for i in range(5):
            x = np.linspace(0.0, len(self.eigenvectors[1][i])/self.F, len(self.eigenvectors[1][i]))
            x_f = np.linspace(0.0, 1.0/(2.0/self.F), len(self.eigenvectors[1][i]))
            y_f = self.eigenvectors[1][i]
            arr.append([x_f,y_f])
        return arr
    # hàm so sánh
    def compare(self,url,N_FFT):
        index = 0
        if N_FFT == 1024:
            index = 1
        elif N_FFT == 2048:
            index = 2
        audio = Speech_Silence.speech_silence(url)
        eigenvector = audio.vectorFFT[index]
        distances = []
        for i in self.eigenvectors[index]:
            distances.append(self.distanceTwoVector(eigenvector,i))
        return [self.vowels[self.indexMinInArr(distances)],f"Dự đoán đây là nguyên âm /{self.vowels[self.indexMinInArr(distances)]}/"]
    
    def indexMinInArr(self,arr):
        index = -1
        MIN = 100000000000000
        for i in range(len(arr)):
            if arr[i] < MIN:
                MIN = arr[i]
                index = i
        return index
    
    def distanceTwoVector(self,v1,v2):
        s = 0
        for i in range(len(v1)):
            s += pow((v1[i] - v2[i]),2)
        return s

    def statistical(self,N_FFT):
        arr =  [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]
        s = 0
        for vowel in self.vowels: 
            for index in range(1,22):
                url = f"Test/{index}/{vowel}.wav"
                character = self.compare(url,N_FFT=N_FFT)
                if character[0] == vowel:
                    s += 1
                if character[0] == vowel and vowel == "a":
                    arr[0][0] += 1
                elif character[0] == vowel and vowel == "e":
                    arr[1][1] += 1
                elif character[0] == vowel and vowel == "i":
                    arr[2][2] += 1
                elif character[0] == vowel and vowel == "o":
                    arr[3][3] += 1
                elif character[0] == vowel and vowel == "u":
                    arr[4][4] += 1

                elif character[0] == "e" and vowel == "a":
                    arr[1][0] += 1
                elif character[0] == "i" and vowel == "a":
                    arr[2][0] += 1
                elif character[0] == "o" and vowel == "a":
                    arr[3][0] += 1
                elif character[0] == "u" and vowel == "a":
                    arr[4][0] += 1
                
                elif character[0] == "a" and vowel == "e":
                    arr[0][1] += 1
                elif character[0] == "i" and vowel == "e":
                    arr[2][1] += 1
                elif character[0] == "o" and vowel == "e":
                    arr[3][1] += 1
                elif character[0] == "u" and vowel == "e":
                    arr[4][1] += 1
                
                elif character[0] == "a" and vowel == "i":
                    arr[0][2] += 1
                elif character[0] == "e" and vowel == "i":
                    arr[1][2] += 1
                elif character[0] == "o" and vowel == "i":
                    arr[3][2] += 1
                elif character[0] == "u" and vowel == "i":
                    arr[4][2] += 1
                
                elif character[0] == "a" and vowel == "o":
                    arr[0][3] += 1
                elif character[0] == "e" and vowel == "o":
                    arr[1][3] += 1
                elif character[0] == "i" and vowel == "o":
                    arr[2][3] += 1
                elif character[0] == "u" and vowel == "o":
                    arr[4][3] += 1
                
                elif character[0] == "a" and vowel == "u":
                    arr[0][4] += 1
                elif character[0] == "e" and vowel == "u":
                    arr[1][4] += 1
                elif character[0] == "i" and vowel == "u":
                    arr[2][4] += 1
                elif character[0] == "o" and vowel == "u":
                    arr[3][4] += 1
        return s,arr

    def getPercent(self):
        arr = []
        for i in self.Count:
            arr.append(round(i / 105 * 100,2))
        return arr
