#!/usr/bin/perl use strict; 

use warnings; 
use HTTP::Tiny; 

my $url = 'http://192.168.178.67/kubectl'; 
my $file = 'kubectl'; 
my $response = HTTP::Tiny->new->get($url); 

if ($response->{success}) { 
    open my $fh, '>', $file or die "Cannot open $file: $!"; 
    print $fh $response->{content}; close $fh;
 } else { 
    die "Failed to get $url\n"; 
}
