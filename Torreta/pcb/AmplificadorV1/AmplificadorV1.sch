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
L Connector:Conn_Coaxial J?
U 1 1 606C5EED
P 3700 3900
F 0 "J?" H 3800 3875 50  0000 L CNN
F 1 "Conn_Coaxial" H 3800 3784 50  0000 L CNN
F 2 "" H 3700 3900 50  0001 C CNN
F 3 " ~" H 3700 3900 50  0001 C CNN
	1    3700 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J?
U 1 1 606C714D
P 8900 4150
F 0 "J?" H 9000 4032 50  0000 L CNN
F 1 "Conn_Coaxial" H 9000 4123 50  0000 L CNN
F 2 "" H 8900 4150 50  0001 C CNN
F 3 " ~" H 8900 4150 50  0001 C CNN
	1    8900 4150
	-1   0    0    1   
$EndComp
$Comp
L Amplifier_Instrumentation2:Amplificador_2_4Ghz U?
U 1 1 606CB00D
P 6800 3900
F 0 "U?" H 6800 3036 50  0000 C CNN
F 1 "Amplificador_2_4Ghz" H 6800 2945 50  0000 C CNN
F 2 "" H 6850 4400 50  0001 C CNN
F 3 "" H 6850 4400 50  0001 C CNN
	1    6800 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Female J?
U 1 1 606CCFBE
P 6850 2900
F 0 "J?" V 6696 2948 50  0000 L CNN
F 1 "Conn_01x02_Female" V 6787 2948 50  0000 L CNN
F 2 "" H 6850 2900 50  0001 C CNN
F 3 "~" H 6850 2900 50  0001 C CNN
	1    6850 2900
	0    1    1    0   
$EndComp
$Comp
L power:+5V #PWR0101
U 1 1 606CDC4F
P 6750 2700
F 0 "#PWR0101" H 6750 2550 50  0001 C CNN
F 1 "+5V" H 6765 2873 50  0000 C CNN
F 2 "" H 6750 2700 50  0001 C CNN
F 3 "" H 6750 2700 50  0001 C CNN
	1    6750 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6750 2750 6600 2750
Wire Wire Line
	6600 2750 6600 3250
$Comp
L power:GND #PWR?
U 1 1 606D277F
P 6850 2700
F 0 "#PWR?" H 6850 2450 50  0001 C CNN
F 1 "GND" H 6855 2527 50  0000 C CNN
F 2 "" H 6850 2700 50  0001 C CNN
F 3 "" H 6850 2700 50  0001 C CNN
	1    6850 2700
	-1   0    0    1   
$EndComp
Wire Wire Line
	6850 2750 8050 2750
Wire Wire Line
	8050 4700 6600 4700
Wire Wire Line
	6600 4700 6600 4300
Wire Wire Line
	8900 3950 8900 3700
Wire Wire Line
	8900 3700 8050 3700
Wire Wire Line
	8050 2750 8050 3700
Connection ~ 8050 3700
Wire Wire Line
	8050 3700 8050 4700
Wire Wire Line
	3700 4100 5450 4100
Wire Wire Line
	5450 4100 5450 3250
Wire Wire Line
	5450 3250 6600 3250
Connection ~ 6600 3250
Wire Wire Line
	6600 3250 6600 3650
Wire Wire Line
	3500 3900 3500 4300
Wire Wire Line
	5900 4300 5900 3850
Wire Wire Line
	5900 3850 6350 3850
Wire Wire Line
	3500 4300 5900 4300
Wire Wire Line
	6600 3250 7050 3250
Wire Wire Line
	7050 3250 7050 3650
Wire Wire Line
	7700 3250 7700 3750
Wire Wire Line
	7700 3750 7250 3750
Wire Wire Line
	7050 3250 7700 3250
Connection ~ 7050 3250
Wire Wire Line
	7250 4050 8450 4050
Wire Wire Line
	8450 4050 8450 4350
Wire Wire Line
	8450 4350 9100 4350
Wire Wire Line
	9100 4350 9100 4150
$EndSCHEMATC
