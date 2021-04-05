close all
clear
fs = 40000;
threshold = 8;
%se leen los archivos y se calcula el error de la fft obtenida y la
%calculada
for i = 0:5
    
    ficheroFft = "fft"+i+".txt";
    fileIdFft = fopen(ficheroFft,'r');
    datosFft = fscanf(fileIdFft,'%f',40000);
    fclose(fileIdFft);
    figure
    hold on
    for k = 1:length(datosFft)
        if abs(datosFft(k))< threshold
            datosFft(k) = 0;
        end
    end
    
    stem(datosFft)
    %plot(20*log10(datosFft),'*')
    
end

