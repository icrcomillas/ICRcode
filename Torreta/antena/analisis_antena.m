clear;
close all;

%load('2_4ghz.mat');
% Design antenna at frequency 2400000000Hz
antennaObject = design(horn,2400000000);
% show for horn
figure;
show(antennaObject) 

impedancia_referencia = 50;
ancho_banda = 12e6;
frecuencia_central = 2.4e9;
paso_frecuencia = 1e3; %intervalo entre muestras del vector de frecuencia

eje_frecuencias = (frecuencia_central-(ancho_banda/2)):paso_frecuencia:(frecuencia_central+(ancho_banda/2));
%%
% calcula la impedancia de la antena
impedancia = impedance(Design,eje_frecuencias);
figure
plot(eje_frecuencias,impedancia)
title('impedancia de la antena');



%se calculan los parametros s de la antena
parametros_s = sparameters(Design, eje_frecuencias,impedancia_referencia);
% se guardan los parametros s de la antena
rfwrite(parametros_s,'parametros.s2p');
%%
% se calcula la red de adaptacion de la antena
red_adaptacion = matchingnetwork('SourceImpedance','parametros.s2p','LoadImpedance',impedancia_referencia,'CenterFrequency',frecuencia_central,'Bandwidth',ancho_banda);
[circuit_list, performance] = circuitDescriptions(red_adaptacion);
rfplot(red_adaptacion,eje_frecuencias,1)
smithplot(red_adaptacion)
parametros_s_adaptado = sparameters(red_adaptacion,eje_frecuencias,impedancia_referencia,1);
figure
rfplot(parametros_s_adaptado)

%%
%se exporta la antena
stlwrite(mesh(antennaObject),'antena_v1.stl')