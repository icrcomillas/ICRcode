
clear 
close all
ranges = linspace(0,5000,5000/0.1); % distancias
frecuencia= 2.4e9;
temperatura = 20;
presion_atmosferica = 101325;
humedad = 5;
c = physconst('LightSpeed');
antenna =design(horn,2400000000);

%%
loss_gas = gaspl(ranges,frecuencia,temperatura,presion_atmosferica,humedad);  %perdidas por los gases
lambda = c/frecuencia;
loss_fsp = fspl(ranges,lambda); %perdidas por el espacio libre
perdidas = pow2db(loss_fsp)+pow2db(loss_gas');

waveform = phased.LinearFMWaveform('SweepBandwidth',1e5,...
    'PulseWidth',5e-5,'OutputFormat','Pulses',...
    'NumPulses',1,'SampleRate',1e6);
transmitter = phased.Transmitter('PeakPower',1.1,'Gain',17);
radiator = phased.Radiator('Sensor',antenna,'OperatingFrequency',frecuencia);
channel = phased.FreeSpace('SampleRate',1e6,...
'TwoWayPropagation',false,'OperatingFrequency',frecuencia);

sensorpos = [0;0;0];
tgtpos = [0;10;10];
[tgtrng,tgtang] = rangeangle(sensorpos,tgtpos);
pulse = waveform();
senal_recepcion_drone = channel(pulse,sensorpos,tgtpos,[0;0;0],[0;0;0]);
%%
figure
plot(abs(senal_recepcion_drone))
figure
plot(ranges,perdidas);
title('Perdidas db/Km')