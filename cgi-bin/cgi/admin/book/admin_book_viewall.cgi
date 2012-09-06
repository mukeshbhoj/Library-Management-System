#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use Data::Dumper;
my %fields;
my $i=0;
my @loop_data = ();
use SEARCH_BOOK;
use CGI::Session;

my $query = CGI->new();
my $session = CGI::Session->new();										
my $username1 = $session->param('ADMIN');
if($session->param('ADMIN')){
	my $query = CGI->new();
	my $query1;
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});



	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');
	my $template11= HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_viewall.tmpl');

	my $loop_data = SEARCH_BOOK::search_all();
	$template2->param(THIS_LOOP=>$loop_data);

	my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 
	$template11->param(username=>$username1);

	print $query->header(), $template1->output,$template11->output,$template2->output,$template3->output;

	undef($query);
	$conn->disconnect();
	$conn = undef;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
