from django.db import models
import numpy as np
import matplotlib.mlab as mlab


class Bloco(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo;

class Graficator(models.Model):
    dominio = models.IntegerField()
    fourierSize = models.IntegerField()
    graus = models.IntegerField()

class Acelerometro(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo;

class Aceleracao(models.Model):
    id = models.AutoField(primary_key=True)
    dataInicio = models.DateTimeField()
    acrescimoSegundos = models.FloatField()
    dataReal = models.DateTimeField()
    orientacao = models.CharField(max_length=1)
    aceleracao = models.FloatField()
    leitura = models.BigIntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, related_name='aceleracao_bloco')
    acelerometro = models.ForeignKey(Acelerometro, on_delete=models.CASCADE, related_name='aceleracao_acelerometro')

class ArquivoFdd(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='fdd_files')
    canais = models.SmallIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    dataInicio = models.DateTimeField()
    frequencia = models.CharField(max_length=20)

    def __str__(self):
        return self.codigo

class FDD(models.Model):
    id = models.AutoField(primary_key=True)

    def power_spectral_density( degrees, fourier_transform_size, stream_file,delta ):
        cross_spectral_density = np.zeros((degrees, degrees,  int((fourier_transform_size / 2)+1)),dtype=complex)  # Store the data 01 by means of a three-dimensional matrix 5 * 5 * 1025
        frequency = np.zeros((degrees, degrees, int((fourier_transform_size / 2)+1)),dtype=complex) # build the matrix...
        n = stream_file.shape  # dimensions of stream file lines x columns
        stream_file = stream_file[1:]
        if n[0] > n[1]:
            acceleration = stream_file #acceleration receives the data from the read file
        else:
            acceleration = np.transpose(stream_file)#acceleration receives the data from the reading file in a transposed way
        for i in range(0, degrees): #
            for j in range(0, degrees): #
                cross_spectral_density[:][i, j],frequency[:][i, j]= mlab.csd( #  applying welch in matrix padding: cross spectral density and frequency
                                          acceleration[:, i],
                                          acceleration[:, j],
                                          NFFT=fourier_transform_size,
                                          Fs=delta,
                                          detrend=mlab.detrend_none,
                                          window=np.hanning(fourier_transform_size),
                                          noverlap =( int(fourier_transform_size / 2)),
                                          pad_to=None,
                                          sides='default',
                                          scale_by_freq=True
                                          )
        return cross_spectral_density, frequency

    def spectral_value_decomposition( degrees, fourier_transform_size, cross_spectral_density):
        #Determines the frequencies in relation to the singular values of the matrix SPECTRAL DENSITY OF POWER
        eigen_values = np.zeros((int((fourier_transform_size / 2)+1), degrees),dtype=complex) # build a new matrix
        size =  int((fourier_transform_size / 2)+1) #loop parameter
        for i in range(0, size):
            U, s, V = np.linalg.svd(cross_spectral_density[:, :, i], full_matrices=True, compute_uv=True) #applies SVD
            eigen_values[i] = s #
            eigen_vectors = U[:, 0] #
        return eigen_values, eigen_vectors

    def system_frequency(self, degrees, fourier_transform_size, stream_file, delta):
        cross_spectral_density, frequency = FDD.power_spectral_density(degrees, fourier_transform_size, stream_file, delta) #call power spectral density power function flame
        eigen_values, eigen_vectors = FDD.spectral_value_decomposition(degrees, fourier_transform_size,cross_spectral_density) # call spectral value decomposition function
        return frequency, eigen_values

    def frequency_position( frequency_peaks, degrees, fourier_transform_size, stream_file, delta):
        cross_spectral_density, frequency = FDD.power_spectral_density(degrees, fourier_transform_size, stream_file,delta) #call power spectral density power function flame
        frequency_positions = np.zeros((1, len(peaks))) # creates a matrix based on peaks
        len_peak = len(peaks) # was NP
        size =  int((fourier_transform_size / 2)+1)#loop parameter
        for i in range(0, len_peak):
            cont = 0
        for k in range(0, size):
            if(frequency[1, 1, k] >= frequency_peaks[i]):
                frequency_positions[0, i] = cont
            else:
                cont = cont + 1
        return frequency_positions

    def vibration_mode_shapes(degrees, fourier_transform_size, stream_file, delta, position):
        cross_spectral_density, frequency = power_spectral_density(degrees, fourier_transform_size, stream_file,delta)
        con = 0
        print (len(str(position[:][:])))
        phi = np.zeros((len(str(position[:][:])), degrees, 1))
        phi = np.zeros((len(str(position[:][:])), degrees, 1))
        for i in range(0, len(position[0])):
            con = con + 1
            U, S, V = np.linalg.svd(cross_spectral_density[:, :, int(position[0][i])], full_matrices=False, compute_uv=True)
            phi[i][:, 0] = U[:, 0]
        return phi
