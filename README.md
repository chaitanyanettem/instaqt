#Instaqt



So I decided to create a quote database from wikiquote dumps.

##"Why?", you ask?

Mostly just for the kicks. Plus I have been wanting to test Twilio's messaging API for some time now. Well maybe I can create a database, hook it up with a phone number and wham bam! Instant inspiration via SMS. :)

##This is what I plan to do

#####Python script to parse mediawiki dumps for wikiquote

This will entail a lot of parsing. I have decided to use ````lxml```` along with the ````re```` module. Should not be too difficult but will be time consuming me thinks. So once I have the parsing worked out I can start dumping quotes into an RDBMS possibly postgres.

#####Ruby on Rails web app

Gives me the excuse to dip my legs in a little bit of RoR. The plan is to create a web app which works like so:

    GET http://instaqt.com/random?by=Albert+Einstein

would return a quote by Albert Einstein

#####Messaging service

Finally once I have the above functionality up I can hook the web app with the Twilio API to respond to messages from phones.
