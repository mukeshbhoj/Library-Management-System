#!/usr/bin/perl -w

use warnings;
use HTML::Template;
use CGI;
use Data::Dumper;

my $template1 = HTML::Template->new(filename => '/var/www/project/html/header.tmpl');   
my $template2 = HTML::Template->new(filename => '/var/www/project/html/login.tmpl'); 
my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 
print "Content-Type:text/html\n\n", $template1->output,$template2->output,$template3->output;
	