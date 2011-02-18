===================
Django IP Filter
===================

A pluggable Django application that allows you to set individual IP addresses, and/or IP networks to be included or excluded from certain operations. The idea, yet to be implemented, is to have a signal sent from the apps middleware that other apps can catch if an IP should be filtered for whatever reason. Nothing is set as to what "excluded" and "included" mean for any given application, but it is designed to be specific enough to allow the app do give other applications some generic directives.

Flow
=====

Once you create some IPs or IP networks to filter on, the middleware shoots out a signal whenever an ip address should be excluded. An app then just hast to look for the signal if it wants to check for IPs to exclude.

