clear
%se leen los archivos
fichero = 'fft57.txt';
fileId = fopen(fichero,'r');
datos = fscanf(fileId,'%f',5000);
fclose(fileId);
figure
plot(datos)