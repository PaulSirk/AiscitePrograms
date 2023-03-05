#!/usr/bin/perl

use strict;
use warnings;

my @test = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
# Or can be written as this.
my @nums = (1..10);

for(@nums){
	if ($_ % 2 == 1){
		print("$_", "\n");
	}
}
