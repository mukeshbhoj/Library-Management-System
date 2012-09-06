#!/usr/bin/perl -w
use strict;
use DBI;
use CGI;
use HTML::Template;
use CGI::Session;
use Check_add_book;
use SEARCH_BOOK;

my $flag = 0;
my $query = CGI->new();
my $session = CGI::Session->new();																		##	and call
if($session->param('ADMIN')){
	my $username1 = $session->param('ADMIN');
	my $id = $query->param("txtid");
	my $title = $query->param("txttitle");
	my $subject = $query->param("txtsubject");
	my $tag = $query->param("txttag");
	my $author = $query->param("txtauthor");
	my $edition = $query->param("txtedition");
	my $publisher = $query->param("txtpublisher");
	my $copy = $query->param("txtcopy");
	my $price = $query->param("txtprice");

	my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
	my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
	my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
	$template2->param(username=>$username1);
	my $template5 = HTML::Template->new(filename => '/var/www/project/html/admin/book/admin_book_update_submit.tmpl');
	
	if(!($title))
		{$template5->param('vartitle'=>"Title is required");$flag = 1;}
	if(!($subject))
		{$template5->param('varsubject'=>"Subject is required");$flag = 1;}
	if(!($tag))
		{$template5->param('vartag'=>"Tag is required");$flag = 1;}
	if(!($author))
		{$template5->param('varauthor'=>"Author is required");$flag = 1;}
	if(!($edition))
		{$template5->param('varedition'=>"Edition is required");$flag = 1;}
	if(!($publisher))
		{$template5->param('varpublisher'=>"Publisher is required");$flag = 1;}
	if(!($copy))
		{$template5->param('varcopy'=>"Number of Copy is required");$flag = 1;}
	if(!($price))
		{$template5->param('varprice'=>"Price is required");$flag = 1;}
	if(!($edition =~ m/^\d*$/)){
		$template5->param('varedition'=>'Edition must be in numeric.');
		$flag = 1;
	}
	if(!($copy =~ m/^\d*$/)){
		$template5->param('varcopy'=>'Number of Copies must be in numeric.');
		$flag = 1;
	}
	if(!($price =~ m/^\d*$/)){
		$template5->param('varprice'=>'Price must be in numeric.');
		$flag = 1;
	}

	my @book=SEARCH_BOOK::search_for_update($id);
	my $old_copy = $book[7];
	if($old_copy > $copy ){
		$template5->param('varcopy'=>'You can\'t decrease number of copies.');
		$flag = 1;
	}

	if ($flag == 1){
		my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
		my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
		my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
		$template2->param(username=>$username1);		
					
		$template5->param(txtid=>$id);
		$template5->param(txttitle=>$title);
		$template5->param(txtsubject=>$subject);
		$template5->param(txttag=>$tag);
		$template5->param(txtauthor=>$author);
		$template5->param(txtpublisher=>$publisher);
		$template5->param(txtedition=>$edition);
		$template5->param(txtcopy=>$copy);
		$template5->param(txtprice=>$price);

		print $query->header();
		print $template1->output,$template2->output,$template5->output,$template4->output;
	}

	else{
		$title =~ s/'/\\'/g;
		$subject =~ s/'/\\'/g;
		$tag =~ s/'/\\'/g;
		$author =~ s/'/\\'/g;
		$publisher =~ s/'/\\'/g;


		my $conn = DBI->connect( 'dbi:Pg:dbname=postgres;host=127.0.0.1','postgres','mangeskaray',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
		my $query1 = $conn->prepare("update book_info set title = '$title' , subject = '$subject' , tag='$tag' , author='$author' , publisher='$publisher' , edition='$edition' , copy='$copy' , price='$price' where group_id = '$id'");
		my $query2 = $conn->prepare("insert into book values ('$id' , 'available') ");
		$query1->execute();
		for(1..$copy-$old_copy)
		{$query2->execute();}

		
		my $template1 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_header.tmpl');   	##	admin_pageheader.tmpl
		my $template2 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_pageheader.tmpl');	##	admin_footer.tmpl
		my $template4 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_footer.tmpl'); 		##
		my $template3 = HTML::Template->new(filename => '/var/www/project/html/admin/admin_home.tmpl'); 
		$template2->param(username=>$username1);		
					
		$template3->param('SUCCESS'=>'Book updated successfully.');

		print $query->header();

	#	print "$id, $name , $birthdate ,$address , $city , $state , $sex , $phno , $joindate , $username , $password , $confpassword";
		print $template1->output,$template2->output,$template3->output,$template4->output;
	}
}

else{
	print $query->redirect(-url=>'/cgi-bin/library.cgi');
}
