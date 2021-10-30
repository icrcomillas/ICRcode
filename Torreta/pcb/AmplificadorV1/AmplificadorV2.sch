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
P 4350 3800
F 0 "J1" H 4450 3775 50  0000 L CNN
F 1 "Conn_Coaxial" H 4450 3684 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount" H 4350 3800 50  0001 C CNN
F 3 " ~" H 4350 3800 50  0001 C CNN
	1    4350 3800
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J3
U 1 1 606C714D
P 8900 4150
F 0 "J3" H 9000 4032 50  0000 L CNN
F 1 "Conn_Coaxial" H 9000 4123 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount" H 8900 4150 50  0001 C CNN
F 3 " ~" H 8900 4150 50  0001 C CNN
	1    8900 4150
	-1   0    0    1   
$EndComp
Wire Wire Line
	4150 3800 4150 4200
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
10v\n
Text Notes 6550 2200 0    50   ~ 0
GND
Wire Wire Line
	7650 4100 7650 4200
Wire Wire Line
	7650 4200 7250 4200
Wire Wire Line
	7250 4100 7650 4100
Connection ~ 7650 4100
Wire Wire Line
	6200 4200 6350 4200
Wire Wire Line
	6200 4200 6200 4100
Wire Wire Line
	6200 4100 6350 4100
Wire Wire Line
	6550 2500 6550 2450
$Comp
L Device:R R1
U 1 1 60A758F7
P 5750 3700
F 0 "R1" V 5543 3700 50  0000 C CNN
F 1 "7.5K" V 5634 3700 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5680 3700 50  0001 C CNN
F 3 "~" H 5750 3700 50  0001 C CNN
	1    5750 3700
	0    1    1    0   
$EndComp
Wire Wire Line
	6350 3700 5900 3700
Wire Wire Line
	5600 3700 5400 3700
$Comp
L pspice:INDUCTOR 15nH1
U 1 1 60B36AD0
P 7850 4850
F 0 "15nH1" V 7804 4928 50  0000 L CNN
F 1 "INDUCTOR" V 7895 4928 50  0000 L CNN
F 2 "Inductor_SMD:L_0402_1005Metric" H 7850 4850 50  0001 C CNN
F 3 "~" H 7850 4850 50  0001 C CNN
	1    7850 4850
	0    1    1    0   
$EndComp
$Comp
L Device:C 100pF1
U 1 1 60B38D69
P 8200 5300
F 0 "100pF1" V 7948 5300 50  0000 C CNN
F 1 "C" V 8039 5300 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 8238 5150 50  0001 C CNN
F 3 "~" H 8200 5300 50  0001 C CNN
	1    8200 5300
	0    1    1    0   
$EndComp
Text GLabel 6550 2500 3    50   BiDi ~ 0
GND
Text GLabel 8900 3950 1    50   BiDi ~ 0
GND
Text GLabel 4350 4000 2    50   BiDi ~ 0
GND
Wire Wire Line
	8300 4100 8300 4350
Wire Wire Line
	7650 4100 7850 4100
Connection ~ 7850 4100
Text Notes 8000 4850 0    50   ~ 0
Inductor para que la señal RF no pase hasta la fuente de alimentación
Wire Wire Line
	7850 5100 7850 5300
Wire Wire Line
	8050 5300 7850 5300
Connection ~ 7850 5300
Text GLabel 8350 5300 2    50   BiDi ~ 0
GND
Text GLabel 8300 5750 2    50   BiDi ~ 0
GND
Wire Wire Line
	8300 4350 8800 4350
$Comp
L Device:C 18pF1
U 1 1 60B38441
P 8950 4350
F 0 "18pF1" V 8698 4350 50  0000 C CNN
F 1 "C" V 8789 4350 50  0000 C CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 8988 4200 50  0001 C CNN
F 3 "~" H 8950 4350 50  0001 C CNN
	1    8950 4350
	0    1    1    0   
$EndComp
Wire Wire Line
	7850 4100 7850 4600
Text GLabel 7850 5850 3    50   BiDi ~ 0
VDD
Text GLabel 6450 2500 3    50   BiDi ~ 0
VDD
Wire Wire Line
	7850 4100 8300 4100
Wire Wire Line
	6450 2450 6450 2500
Text GLabel 5400 3700 0    50   BiDi ~ 0
VDD
Text Notes 5650 3850 0    50   ~ 0
100mA
$Comp
L pspice:INDUCTOR 33nH1
U 1 1 60B61711
P 5650 4200
F 0 "33nH1" V 5604 4278 50  0000 L CNN
F 1 "INDUCTOR" V 5695 4278 50  0000 L CNN
F 2 "Inductor_SMD:L_0402_1005Metric" H 5650 4200 50  0001 C CNN
F 3 "~" H 5650 4200 50  0001 C CNN
	1    5650 4200
	-1   0    0    1   
$EndComp
Wire Wire Line
	5750 4350 5750 4300
$Comp
L Device:C 0.1uF1
U 1 1 60B39A86
P 8150 5750
F 0 "0.1uF1" V 7898 5750 50  0000 C CNN
F 1 "C" V 7989 5750 50  0000 C CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 8188 5600 50  0001 C CNN
F 3 "~" H 8150 5750 50  0001 C CNN
	1    8150 5750
	0    1    1    0   
$EndComp
Wire Wire Line
	7850 5300 7850 5750
Wire Wire Line
	8000 5750 7850 5750
Connection ~ 7850 5750
Wire Wire Line
	7850 5750 7850 5850
Text GLabel 8250 4100 1    50   Input ~ 0
señal
Text GLabel 4850 4200 1    50   Input ~ 0
señal
Text GLabel 6550 3550 1    50   Input ~ 0
GND
Text GLabel 7350 3850 2    50   Input ~ 0
GND
Text GLabel 7350 3750 2    50   Input ~ 0
GND
Text GLabel 6500 4400 3    50   Input ~ 0
GND
Text GLabel 6650 4400 3    50   Input ~ 0
GND
Text GLabel 7100 4400 3    50   Input ~ 0
GND
Text GLabel 6900 4400 3    50   Input ~ 0
GND
Text GLabel 6750 3550 1    50   Input ~ 0
GND
Text GLabel 6950 3550 1    50   Input ~ 0
GND
Text GLabel 7150 3550 1    50   Input ~ 0
GND
Text GLabel 6250 3900 0    50   Input ~ 0
GND
$Comp
L Amplifier_Instrumentation2:Amplificador_2_4Ghz U1
U 1 1 606CB00D
P 6800 3900
F 0 "U1" H 6800 3036 50  0000 C CNN
F 1 "Amplificador_2_4Ghz" H 6800 2945 50  0000 C CNN
F 2 "Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm" H 6850 4400 50  0001 C CNN
F 3 "" H 6850 4400 50  0001 C CNN
	1    6800 3900
	1    0    0    -1  
$EndComp
Text GLabel 5100 4500 3    50   Input ~ 0
GND
$Comp
L Device:C 1.8pF1
U 1 1 60B60ED2
P 5100 4350
F 0 "1.8pF1" H 5215 4396 50  0000 L CNN
F 1 "C" H 5215 4305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5138 4200 50  0001 C CNN
F 3 "~" H 5100 4350 50  0001 C CNN
	1    5100 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 4200 5900 4200
Connection ~ 6200 4200
Wire Wire Line
	5400 4200 5100 4200
Wire Wire Line
	5100 4200 4150 4200
Connection ~ 5100 4200
$EndSCHEMATC
