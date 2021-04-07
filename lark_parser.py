from lark import Lark

with open("grammer.lark",encoding="utf-8") as grammar:
    LP = Lark(grammar.read(),start="start")

tree = LP.parse("""say OPTION_A 日本語 英語 OPTION_B Japanese English OPTION_C りんご,ばなな
say OPTION_A 日本語 英語 OPTION_B Japanese English OPTION_C りんご,ばなな
multilinesay 
OPTION_A 日本語 # COMMENT1 
# COMMENT1 
# COMMENT3
OPTION_B Japanese
""")
print(tree)
