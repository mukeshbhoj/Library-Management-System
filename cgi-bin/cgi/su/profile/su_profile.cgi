#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use Data::Dumper;
use HTML::Template;
use CGI::Session;
use Search_mem;
use SEARCH_BOOK;

my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('LIBRARIAN'))
{
	my $username1 = $session->param('LIBRARIAN');
	my $template1 = HTML::Template->new(filename => '/var/www/project/html/su/su_header.tmpl');   	##	su_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/su/su_pageheader.tmpl');	##	su_footer.tmpl
	$template2->param(username=>$username1);																	##
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/su/su_footer.tmpl'); 		##

		my $id = Search_mem::search_id($username1);
		
		my @member = Search_mem::search_mem($id);
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/su/profile/su_profile.tmpl'); 
		$template3->param(THIS_LOOP=>\@member);

		my $issued_book = SEARCH_BOOK::search_issued($id);
		$template3->param(issued_book=>$issued_book);
		$template3->param(total_book=>$member[0]->{name}." has issued ".@$issued_book." book(s).");
		
		$template3->param(SUCCESS=>$session->param('profile'));
		$session->param('profile','');

		print "Content-Type:text/html\n\n";
		print $template1->output;
		print $template2->output;
		print $template3->output;
		print $template4->output;

}
else
{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
