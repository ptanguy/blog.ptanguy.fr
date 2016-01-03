Title: Software Defined Radio PLC demonstrator
Date: 2016-01-03
Authors: ptanguy
Category: PLC
Tags: SDR, PLC, PHY, USRP2, GNURadio, Matlab 
Slug: software-defined-radio-plc-demonstrator
Summary: Rapid prototyping solutions are essential to test PHY/MAC layer algorithms in real situations. We propose an example of rapid prototyping for PLC communication with a SDR platform (USRP2) from Ettus Research.  
Status: published

## PHY rapid prototyping

It is important to evaluate digital communications algorithms in real-world.
To do that, it is essential to build a demonstrator to test the algorithm developed during the simulation phase.
This task is difficult, expensive and can take a lot of time.
Moreover, for a first prototype, engineers need a flexible demonstrator to change and modify the different parameters of the PHY layer.
			
            
Here, we propose an example of rapid prototyping for PLC communication with a SDR platform.
This kink of demonstrator are perfect to realize a rapid prototyping.
Indeed, all the functions of the PHY layer are software defined.
In our work, the implementation on a GPP brings the flexibility to our demonstrator.
        

## Testbed: Matlab, GNUradio and USRP2 card
			
For the hardware part we used the USRP2 card of the ETTUS Research society.
For the software part we used Matlab and GNUradio.
The demonstrator can achieve a maximum bandwidth of 12.5 MHz.

![Image of general demonstrator]({filename}/images/scheme_general_usrp.png)

		
## Results
        
Multi-carrier modulations have been proposed to achieve high data rates.
More precisely, adaptive multi-carrier modulations (bit-loading) seem to be a good choice allowing robust transmission on the power line channel.
We show here some results on a Peugeot 407SW for the path GF.

![Image of the car]({filename}/images/voiture.png)

Several frames are sent on the PLC channel at the point G.
The figure on the left shows the received frames at the point F.
We can observe several frames and different impulsive noises.
On the receiver part, time synchronization, phase error correction due to timing error, SNR estimation and bit-loading have been computed.
The figure on the right shows the results of the bit-loading algorithm for a target BER of 1e-3.
In this case, the bit rate will be 20.3 Mbps.


![Image of received signal]({filename}/images/Rx_GF_scenarioStatique1_Zoom.png)


![Image of bit-loading result]({filename}/images/Bitloading_GF_scenarioStatique1.png)
     

## Ongoing work

* PHY layer in GNUradio
* AGC control from GNUradio

