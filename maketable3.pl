#!/usr/bin/perl

###############################################################################
# maketable3.pl will make a table of 1/R^10, 1/R^12 and the appropriate       #                           
# second derivatives for use with the CA model in gromacs: VERSION 3          #
# Values not provided for distances under 0.1 Angstroms                       #
# WARNING: Always look at the table to ensure no precision issues are present #
# Written by Paul Whitford, 12/6/08                                           #
###############################################################################


#what is the length of the table? (in nm. 100 in this example)
        $Rtable=100;
       $Ntable=int($Rtable/0.0005);
	print "0.0 0.0 0.0 1.0 1.0 1.0 1.0\n";

for($i=2; $i<$Ntable;$i++){
       $R=$i*0.0005;

	if( $R > 0.01){
	       $R1=-1/$R**10;
	       $R2=-110/$R**12;
	       $R3=1/$R**12;
	       $R4=156.0/$R**14;
		print "$R 0.0 0.0 $R1 $R2 $R3 $R4\n";
	}
}	
