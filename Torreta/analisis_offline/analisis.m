close all
clear
fs = 40000;
error = zeros(0,22);
%se leen los archivos y se calcula el error de la fft obtenida y la
%calculada
for i = 0:21
    
    ficheroFft = "fft"+i+".txt";
    fileIdFft = fopen(ficheroFft,'r');
    datosFft = fscanf(fileIdFft,'%f',40000);
    fclose(fileIdFft);
    
    ficheroData = "data"+i+".txt";
    fileIdData = fopen(ficheroData,'r');
    datosTextoData = fscanf(fileIdData,'%s',40000);
   
    fclose(fileIdData);
    Fft = fs*fft(datosData)/length(datosData);
    Fft = fftshift(abs(Fft));
    % se calcula el error
    errorCuadratico = 0;
    for k =1:40001
        errorCuadratico = errorCuadratico + (datosFft(k)- Fft(k))^2;
    end
    error(i+1) = errorCuadratico;
    
end
mean(error)

