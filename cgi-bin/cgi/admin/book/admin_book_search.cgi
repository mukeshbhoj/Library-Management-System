#!/usr/bin/perl -w
use strict;
use CGI;
use HTML::Template;

my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');
my $template11 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');
my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_search.tmpl');
my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 

print "Content-Type:text/html\n\n", $template1->output,$template11->output,$template2->output,$template3->output;



