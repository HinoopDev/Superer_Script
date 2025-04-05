import parser
import tokenizer
import constants


run = True
while run:
    ui = input("> ")
    pui = parser.parse(ui)
    print(pui)
    print(parser.parse("hello-world(was up)\n"))