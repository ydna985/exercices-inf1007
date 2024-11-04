#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	ouverture=[braket for index, braket in enumerate(brackets) if index%2 == 0]
	fermeture=[braket for index, braket in enumerate(brackets) if index%2 != 0]
	print(ouverture,"----",fermeture)
	# bracks=""
	# for letter in text:
	# 	if letter in brackets:
	# 		bracks+=letter

	# precedent_closure_index=len(bracks)-1
	# bracks_copy=bracks
	
	# for index, brack in enumerate(bracks):
	# 	if index == precedent_closure_index:
	# 		precedent_closure_index=len(bracks)-1
	# 		continue
	# 	if brackets.index(brack) % 2 == 0:
	# 		brack_closure_index=brackets.index(brack)+1
	# 		if brackets[brack_closure_index] in bracks_copy:
	# 			if bracks_copy.rfind(brackets[brack_closure_index]) > precedent_closure_index:
	# 				return False
	# 			precedent_closure_index=bracks_copy.rfind(brackets[brack_closure_index])
	# 			bracks_copy=bracks_copy[:precedent_closure_index]+bracks_copy[precedent_closure_index+1:]
	# 		else:
	# 			return False
	# 	else:
	# 		return False
	# return True

def remove_comments(full_text, comment_start, comment_end):
	return ""

def get_tag_prefix(text, opening_tags, closing_tags):
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):
	return False


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

