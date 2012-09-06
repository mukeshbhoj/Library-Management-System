#!/usr/bin/perl -w
use strict;

use CGI;
use HTML::Template;

my $template1 = HTML::Template->new(filename => '/var/www/project/html/header.tmpl');
my $template2 = HTML::Template->new(filename => '/var/www/project/html/search.tmpl');
$template2->param('search_table'=>'hidden');
my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 

print "Content-Type:text/html\n\n", $template1->output,$template2->output,$template3->output;



