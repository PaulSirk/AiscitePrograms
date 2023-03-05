#!/usr/bin/perl

use strict;
use warnings;

print "Hello! My name is Perl! What is your name? ";
my $name = <>;

chomp($name);

print "\nHello ", $name,"!\n";
