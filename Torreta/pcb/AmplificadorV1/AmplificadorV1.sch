EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_Coaxial J1
U 1 1 606C5EED
P 3700 3900
F 0 "J1" H 3800 3875 50  0000 L CNN
F 1 "Conn_Coaxial" H 3800 3784 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Amphenol_132289_EdgeMount" H 3700 3900 50  0001 C CNN
F 3 " ~" H 3700 3900 50  0001 C CNN
	1    3700 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J3
U 1 1 606C714D
P 8900 4150
F 0 "J3" H 9000 4032 50  0000 L CNN
F 1 "Conn_Coaxial" H 9000 4123 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Amphenol_132289_EdgeMount" H 8900 4150 50  0001 C CNN
F 3 " ~" H 8900 4150 50  0001 C CNN
	1    8900 4150
	-1   0    0    1   
$EndComp
Wire Wire Line
	3500 3900 3500 4300
Wire Wire Line
	9100 4350 9100 4150
$Comp
L Connector:Conn_01x02_Female J2
U 1 1 60A4F3F0
P 6450 2250
F 0 "J2" V 6388 2062 50  0000 R CNN
F 1 "Conn_01x02_Female" V 6297 2062 50  0000 R CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6450 2250 50  0001 C CNN
F 3 "~" H 6450 2250 50  0001 C CNN
	1    6450 2250
	0    -1   -1   0   
$EndComp
Text Notes 6400 2200 0    50   ~ 0
5v\n
Text Notes 6550 2200 0    50   ~ 0
GND
Wire Wire Line
	7050 3300 7050 3650
Wire Wire Line
	6600 3650 6600 3300
$Comp
L Amplifier_Instrumentation2:Amplificador_2_4Ghz U1
U 1 1 606CB00D
P 6800 3900
F 0 "U1" H 6800 3036 50  0000 C CNN
F 1 "Amplificador_2_4Ghz" H 6800 2945 50  0000 C CNN
F 2 "Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm" H 6850 4400 50  0000 C CNN
F 3 "" H 6850 4400 50  0001 C CNN
	1    6800 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7650 4100 7650 4200
Wire Wire Line
	7650 4200 7250 4200
Wire Wire Line
	7250 4100 7650 4100
Connection ~ 7650 4100
Wire Wire Line
	7650 4100 7700 4100
Wire Wire Line
	6200 4300 6200 4200
Wire Wire Line
	6200 4200 6350 4200
Wire Wire Line
	3500 4300 6200 4300
Wire Wire Line
	6200 4200 6200 4100
Wire Wire Line
	6200 4100 6350 4100
Connection ~ 6200 4200
Wire Wire Line
	9100 4350 8200 4350
Wire Wire Line
	8200 4350 8200 4000
Wire Wire Line
	8200 4000 7700 4000
Wire Wire Line
	7700 4000 7700 4100
Wire Wire Line
	8900 3950 7850 3950
Wire Wire Line
	7850 3950 7850 2500
Wire Wire Line
	7850 2500 6550 2500
Wire Wire Line
	6550 2500 6550 2450
Wire Wire Line
	3750 4100 5200 4100
Wire Wire Line
	5200 4100 5200 2500
Wire Wire Line
	5200 2500 6550 2500
Connection ~ 6550 2500
Wire Wire Line
	6450 2450 6450 3200
Wire Wire Line
	6450 3200 5400 3200
Wire Wire Line
	5400 3200 5400 3700
$Comp
L Device:R R?
U 1 1 60A758F7
P 5750 3700
F 0 "R?" V 5543 3700 50  0000 C CNN
F 1 "R" V 5634 3700 50  0000 C CNN
F 2 "" V 5680 3700 50  0001 C CNN
F 3 "~" H 5750 3700 50  0001 C CNN
	1    5750 3700
	0    1    1    0   
$EndComp
Wire Wire Line
	6350 3700 5900 3700
Wire Wire Line
	5600 3700 5400 3700
$EndSCHEMATC
