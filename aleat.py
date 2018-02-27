#!/usr/bin/python3

import webapp
import random

class miwebapp(webapp.webApp):
    def process(self, parsedRequest):
        aux = random.randint(1,999999999)
        return ("200 ok","<html><body><h1>Hola. </h1>></body></html><a href ='http://localhost:1234/"+str(aux)+"'>Dame otra</a>")

if __name__ == "__main__":
    miapp = miwebapp("localhost", 1234)
