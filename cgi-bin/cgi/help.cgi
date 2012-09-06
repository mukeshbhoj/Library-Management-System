#!/usr/bin/perl -w

use warnings;

use HTML::Template;
use CGI;
my $query = CGI->new();

my $template1 = HTML::Template->new(filename => '/var/www/project/html/header.tmpl');   
my $template2 = HTML::Template->new(filename => '/var/www/project/html/help.tmpl'); 
my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 

print $query->header(), $template1->output,$template2->output,$template3->output;
