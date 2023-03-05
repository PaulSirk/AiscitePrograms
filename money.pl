#!/usr/bin/perl

use strict;
use warnings;

my %values = (penny => 0.01,
	nickel => 0.05,
	dime => 0.1,
	quarter => 0.25,
	one => 1,
	two => 2,
	five => 5,
	ten => 10,
	twenty => 20,
	fifty => 50,
	hundred => 100
);

my $sum = 0;

while (my($k, $v) = each %values){
	print("How many $k", "s do you have? ");
	my $answer = <>;

	$sum += ($v * $answer);
}

print("\n$sum\n");
