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


my $query = CGI->new();
my $title = $query->param('title');
my $author = $query->param('author');
my $publisher = $query->param('publisher');
my $subject = $query->param('subject');
my $search='';
my $query1;
my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

if($title)
{	$search = "$search title = \'$title\' ";				}

if($author)
{	if($search){$search = "$search and ";}	$search = "$search author = \'$author\' ";			}

if($publisher)
{	if($search){$search = "$search and ";}	$search = "$search publisher = \'$publisher\' ";	}

if($subject)
{	if($search){$search = "$search and ";}	$search = "$search subject = \'$subject\' ";		}



my $template1 = HTML::Template->new(filename => '/var/www/project/html/header.tmpl');
my $template2 = HTML::Template->new(filename => '/var/www/project/html/search.tmpl');

if($search){	
	my $loop_data = SEARCH_BOOK::search($search);	
	$template2->param(THIS_LOOP=>$loop_data);
	$i = @$loop_data;
}

if($i != 0)
{	$template2->param(RECORDS=>"$i records are found.");	}

else
{	$template2->param(RECORDS=>"Please insert proper value for the best search.");	}

my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 

print $query->header(), $template1->output,$template2->output,$template3->output;

undef($query);
$conn->disconnect();
$conn = undef;


