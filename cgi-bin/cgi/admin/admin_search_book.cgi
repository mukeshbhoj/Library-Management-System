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
	my $title = $query->param('title');
	my $author = $query->param('author');
	my $publisher = $query->param('publisher');
	my $subject = $query->param('subject');
	my $id = $query->param('id');
	my $tag = $query->param('tag');
	my $search='';
	my $query1;
	my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

	$title =~ s/'/\\'/g;
	$author =~ s/'/\\'/g;
	$publisher =~ s/'/\\'/g;
	$subject =~ s/'/\\'/g;
	$id =~ s/'/\\'/g;
	$tag =~ s/'/\\'/g;
		
	if($title)
	{	$search = "$search title ilike \'%$title%\' ";				}
	
	if($author)
	{	if($search){$search = "$search and ";}	$search = "$search author ilike \'%$author%\' ";			}
	
	if($publisher)
	{	if($search){$search = "$search and ";}	$search = "$search publisher ilike \'%$publisher%\' ";	}
	
	if($subject)
	{	if($search){$search = "$search and ";}	$search = "$search subject ilike \'%$subject%\' ";		}
	
	if($id)
	{	if($search){$search = "$search and ";}	$search = "$search group_id = \'$id\' ";		}
	
	if($tag)
	{	if($search){$search = "$search and ";}	$search = "$search tag ilike \'%$tag%\' ";		}


	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');
	my $template11= HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_search.tmpl');

	if($search && $id =~ m/^\d*$/){
	my $loop_data = SEARCH_BOOK::search($search);
	$template2->param(THIS_LOOP=>$loop_data);
	$i = @$loop_data;
	}

	if($i != 0){	
		$template2->param(RECORDS=>"$i records are found.");	
	}
	else{		
		$template2->param(RECORDS=>"Please insert proper value for the best search.");
		$template2->param(search_table=>"hidden");
	}

	my $template3 = HTML::Template->new(filename => '/var/www/project/html/footer.tmpl'); 
	$template11->param(username=>$username1);

	print "Content-Type:text/html\n\n", $template1->output,$template11->output,$template2->output,$template3->output;

	undef($query);
	$conn->disconnect();
	$conn = undef;
}
else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
