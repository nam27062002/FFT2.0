# import thư viện
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
# class
class speech_silence:
    # hàm khởi tạo
    def __init__(self,url) -> None:
        self.F, self.audio = wavfile.read(url) # mở file wav
        self.dentaTime = 0.01 # thời gian chia khoảng tín hiệus
        self.E_MAX = 3000000 # năng lượng tối đa khoảng lặng có thể đạt được trong dentaTime s
        self.SpeechSignal = self.setSpeechSignal() # tín hiệu tiếng nói
        self.StableSignal = self.setStableSignal() # tín hiệu ổn định trong tín hiệu tiếng nói 
        self.N_FFT = [512,1024,2048] # số chiều trích xuất vector
        self.vectorFFT = self.setVectorFFT() # list vector FFT
    
    # trả về tín hiệu gốc
    def getOriginSignal(self) -> list: 
        x = np.arange(len(self.audio))/self.F 
        y = self.audio
        return [x,y]

    # trả về tín hiệu lời nói
    def getSpeechSignal(self) -> list: 
        x = np.arange(len(self.SpeechSignal))/self.F 
        y = self.SpeechSignal
        return [x,y]
    
    # trả về tín hiệu ổn định
    def getStableSignal(self) -> list: 
        x = np.arange(len(self.StableSignal))/self.F 
        y = self.StableSignal
        return [x,y]
    
    # trả về vector FFT
    def getVectorFFT(self) -> list: 
        x = np.linspace(0.0, len(self.vectorFFT[1])/self.F, len(self.vectorFFT[1]))
        x_f = np.linspace(0.0, 1.0/(2.0/self.F), len(self.vectorFFT[1]))
        y_f = self.vectorFFT[1]
        return [x_f, y_f]

    # hàm tính năng lương tín hiệu
    def signalEnergy(self,arr) -> float: 
        E = 0
        for i in arr:
            E += pow(i,2)
        return E
    
    # Đầu vào là 1 tín hiệu âm thanh. Trả về tín hiệu chỉ chứa tiếng nói
    def setSpeechSignal(self) -> list:
        # chia tín hiệu thành những tín hiệu nhỏ hơn và lưu ở list arr 
        arr = [] 
        for i in range(len(self.audio)):
            if i%int(self.dentaTime * self.F) == 0:
                arr.append([]) # thêm list con vào arr sau mỗi dentaTime s
            arr[-1].append(self.audio[i]) 
        # tính năng lượng ở mỗi phần tử trong mảng vừa được tạo 
        Energy = []
        for i in arr:
            Energy.append(abs(self.signalEnergy(i)))
        # chỉ chọn những phần tử có năng lượng lớn hơn E_MAX (không phải khoảng lặng)
        ARR = []
        for i in range(len(Energy)):
            if (Energy[i] > self.E_MAX).any():
                ARR.append(arr[i])
        # chuyển ARR từ 2d sang 1d
        x = []
        for i in ARR:
            for j in i:
                x.append(j)
        # trả về tín hiệu tiếng nói
        return x
        
    # đánh dấu vùng ổn định (chia tín hiệu tiếng nói vừa thu được thành 3 phần và lấy phần ở giữa)
    def setStableSignal(self) -> list:
        x = len(self.SpeechSignal)
        arr = []
        for i in range(int(x/3),int(2*x/3),1):
            arr.append(self.SpeechSignal[i])
        return arr
    
    # lưu âm thanh ở vùng ổn định
    def SaveVoice(self):
        m = np.max(np.abs(self.SpeechSignal))
        sigf32 = (self.SpeechSignal/m).astype(np.float32)
        write('SpeechSignal.wav', self.F, np.asarray(sigf32))
    
    # Tính vector FFT với số chiều N_FFT
    def setVectorFFT(self):
        # chia khung tín hiệu ổn định với mỗi khung dài 20ms
        ms = 0.04
        FrameSignal = []
        a = []
        for i in range(len(self.StableSignal)):
            a.append(self.StableSignal[i])
            if i % int(ms*self.F) == 0 or i == len(self.StableSignal) - 1:
                FrameSignal.append(a)
                a = []
        arr = []
        for i in self.N_FFT: # i = 512,1024,2048
            x = []
            for j in FrameSignal:
                FFT = np.fft.fft(j,i)
                x.append(2/i * np.abs(FFT[:i//2]))
            v = []
            for i in range(len(x[0])):
                s = 0
                for j in range(len(x)):
                    s += x[j][i]
                v.append(s/len(x))
            arr.append(v)
        return arr