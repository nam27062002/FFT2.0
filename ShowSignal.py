import matplotlib.pyplot as plt
import Speech_Silence
class ShowSignal:
    def __init__(self,url,text) -> None:       
        self.Audio = Speech_Silence.speech_silence(url)
        self.text = text
    def show(self):
        figure, axis = plt.subplots(2,2)
        axis[0][0].plot(self.Audio.getOriginSignal()[0],self.Audio.getOriginSignal()[1])
        axis[0][0].set_title(self.text)
        axis[0][0].set_xlabel("Time (s)")
        axis[0][0].set_ylabel("Frequency (Hz)")
        axis[0][1].plot(self.Audio.getSpeechSignal()[0],self.Audio.getSpeechSignal()[1])
        axis[0][1].set_title("Tính hiệu tiếng nói")
        axis[0][1].set_xlabel("Time (s)")
        axis[0][1].set_ylabel("Frequency (Hz)")
        axis[1][0].plot(self.Audio.getStableSignal()[0],self.Audio.getStableSignal()[1])
        axis[1][0].set_title("Tính hiệu tiếng nói ổn định")
        axis[1][0].set_xlabel("Time (s)")
        axis[1][0].set_ylabel("Frequency (Hz)")
        axis[1][1].plot(self.Audio.getVectorFFT()[0],self.Audio.getVectorFFT()[1])
        axis[1][1].set_title(f"Vector FFT với {self.Audio.N_FFT[1]} chiều")
        axis[1][1].set_xlabel("Frequency (Hz)")
        axis[1][1].set_ylabel("amplitude (g)")
        plt.show()
