Youtube-Comment-Sonnet


Youtube Comment Sonnet Generator


List of global variables
Strings: RHYMESCHEMEA, RHYMESCHEMEB (three letter strings containing the rhyme schemes) 
Ints: ATIME, BTIME, (number of times current rhyme scheme has had rhyming words inserted(from 0 to 2)
, FILE_OFFSET (offset in sonnet file - presumably a txt file? )

List of Functions and inputs/outputs


1: Main(): 
IN VOID, RETURN 1
-Parses URL for first youtube link to be used
(Don't know how the first video will be generated)

-Calls website_retriever()

-Calls comment_collector() in an infinite loop

-Return 1


2: comment_collector()

IN VOID, RETURN VOID

-Read html file

-Parses list of comment strings

-Loops through sending strings to comment_parser()

-If comment parser returns string, insert string in sonnet file at FILE_OFFSET

-When loop has completed, call url_parser

-Call website_retriever

-Return void


3: comment_parser(STRING)

IN STRING, RETURN STRING OR FALSE

-If ATIME == 2, create new RHYMESCHEMEA and set ATIME to 0 

-If BTIME == 2, create new RHYMESCHEMEB and set BTIME to 0

-Do comment parsing(not sure exactly how this will get done)

-If OUT == STRING and last three letters of string == RHYMESCHEMEA, ATIME += 1

-If OUT == STRING and last three letters of string == RHYMESCHEMEB, BTIME += 1

-Return STRING or FALSE


4: url_parser()

IN VOID, OUT STRING

-Read html file

-Parse url string of the first related video

-Return STRING (the url of the related video)


5: website_retriever(STRING)

IN STRING, OUT VOID

-Save source file of given input URL

-Return void 
