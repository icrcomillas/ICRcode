<Qucs Schematic 0.0.15>
<Properties>
  <View=-70,80,1461,745,1,185,0>
  <Grid=10,10,1>
  <DataSet=simulacion2.dat>
  <DataDisplay=simulacion2.dpl>
  <OpenDisplay=1>
  <showFrame=0>
  <FrameText0=T\x00EDtulo>
  <FrameText1=Dibujado por:>
  <FrameText2=Fecha:>
  <FrameText3=Revisi\x00F3n:>
</Properties>
<Symbol>
  <.ID -20 -16 SUB>
  <Line -20 20 40 0 #000080 2 1>
  <Line 20 20 0 -40 #000080 2 1>
  <Line -20 -20 40 0 #000080 2 1>
  <Line -20 20 0 -40 #000080 2 1>
</Symbol>
<Components>
  <Pac P1 1 210 300 18 -26 0 1 "1" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <GND * 1 210 330 0 0 0 0>
  <GND * 1 640 280 0 0 0 0>
  <SPfile X1 1 640 250 -26 -65 0 0 "C:/Users/gonza/Documents/GitHub/ICRcode/Torreta/pcb/GRF5020_SPARS/5020_10_160.s2p" 1 "rectangular" 0 "linear" 0 "open" 0 "2" 0>
  <L L1 1 580 250 -26 10 0 0 "0.878336nH" 1 "" 0>
  <C C1 1 510 320 17 -26 0 1 "2.71065pF" 1 "" 0 "neutral" 0>
  <GND * 1 510 350 0 0 0 0>
  <SUBST Subst1 1 460 480 -30 24 0 0 "4.5" 1 "0.2 mm" 1 "35 um" 1 "2e-4" 1 "0.022e-6" 1 "0.15e-6" 1>
  <L L2 1 800 250 -26 10 0 0 "1.85925nH" 1 "" 0>
  <L L3 1 720 310 17 -26 0 1 "67.7638nH" 1 "" 0>
  <.SP SP1 1 660 550 0 65 0 0 "lin" 1 "2 GHz" 1 "2.5 GHz" 1 "10000" 1 "no" 0 "1" 0 "2" 0 "no" 0 "no" 0>
  <GND * 1 780 380 0 0 0 0>
  <GND * 1 780 460 0 0 0 0>
  <Pac P2 1 1330 280 18 -26 0 1 "2" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <GND * 1 1330 310 0 0 0 0>
  <C C2 1 750 380 -26 17 0 0 "10 pF" 1 "" 0 "neutral" 0>
  <C C3 1 750 460 -26 17 0 0 "0.1 uF" 1 "" 0 "neutral" 0>
  <C C4 1 1040 250 -26 17 0 0 "18 pF" 1 "" 0 "neutral" 0>
  <MLIN MS1 1 390 250 -26 15 0 0 "Subst1" 1 "0.34mm" 1 "10 mm" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MLIN MS2 1 950 250 -26 15 0 0 "Subst1" 1 "0.34mm" 1 "5 mm" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MLIN MS3 1 1100 250 -26 15 0 0 "Subst1" 1 "0.3mm" 1 "5 mm" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
</Components>
<Wires>
  <510 250 550 250 "" 0 0 0 "">
  <510 250 510 290 "" 0 0 0 "">
  <720 250 720 280 "" 0 0 0 "">
  <720 250 770 250 "" 0 0 0 "">
  <670 250 720 250 "" 0 0 0 "">
  <420 250 510 250 "" 0 0 0 "">
  <210 250 210 270 "" 0 0 0 "">
  <210 250 360 250 "" 0 0 0 "">
  <830 250 920 250 "" 0 0 0 "">
  <720 340 720 380 "" 0 0 0 "">
  <1130 250 1330 250 "" 0 0 0 "">
  <720 380 720 460 "" 0 0 0 "">
  <980 250 1010 250 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
  <Text 820 230 12 #000000 0 "Port 2">
</Paintings>
